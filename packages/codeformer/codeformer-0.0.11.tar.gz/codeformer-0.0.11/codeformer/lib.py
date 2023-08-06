import cv2
import numpy as np
import torch
from torchvision.transforms.functional import normalize
from basicsr.utils import img2tensor, tensor2img
from basicsr.utils.download_util import load_file_from_url
from basicsr.utils.misc import gpu_is_available, get_device
from facelib.utils.face_restoration_helper import FaceRestoreHelper
from facelib.utils.misc import is_gray
from pathlib import Path

from basicsr.utils.registry import ARCH_REGISTRY

pretrain_model_url = {
    "restoration": "https://github.com/sczhou/CodeFormer/releases/download/v0.1.0/codeformer.pth",
}


class CodeFormer:
    def __init__(
        self,
        fidelity_weight=0.5,
        upscale=2,
        has_aligned=False,
        only_center_face=False,
        draw_box=False,
        detection_model="retinaface_resnet50",
        bg_enhance=False,
        bg_upsampler="realesrgan",
        face_enhance=False,
        bg_tile=400,
        suffix=None,
        save_video_fps=None,
        weights=Path(__file__).parent / "weights/CodeFormer/codeformer.pth",
    ) -> None:
        """
        Args:
            input_path (str): Input image, video or folder. Default: inputs/whole_imgs
            output_path (str): Output folder. Default: results/<input_name>_<w>
            fidelity_weight (float): Balance the quality and fidelity. Default: 0.5
            upscale (int): The final upsampling scale of the image. Default: 2
            has_aligned (bool): Input are cropped and aligned faces. Default: False
            only_center_face (bool): Only restore the center face. Default: False
            draw_box (bool): Draw the bounding box for the detected faces. Default: False
            weights (str): Path to the pretrained model
            detection_model (str): Face detector. Optional: retinaface_resnet50, retinaface_mobile0.25, YOLOv5l, YOLOv5n, dlib.
                Default: retinaface_resnet50
            bg_enhance (bool): Background enhancement. Default: False
            bg_upsampler (str): Choices: Background upsampler. Optional: realesrgan
            face_enhance (bool): Face upsampler after enhancement. Default: False
            bg_tile (int): Tile size for background sampler. Default: 400
            suffix (str): Suffix of the restored faces. Default: None
            save_video_fps (float): Frame rate for saving video. Default: None
        """

        self.device = get_device()
        self.fidelity_weight = fidelity_weight
        self.upscale = upscale
        self.has_aligned = has_aligned
        self.only_center_face = only_center_face
        self.draw_box = draw_box
        self.detection_model = detection_model
        self.bg_enhance = bg_enhance
        self.bg_upsampler = bg_upsampler
        self.face_enhance = face_enhance
        self.bg_tile = bg_tile
        self.suffix = suffix
        self.save_video_fps = save_video_fps
        self.weights = weights

        # ------------------ set up background upsampler ------------------
        if self.bg_enhance and self.bg_upsampler == "realesrgan":
            self.bg_upsampler = self.get_realesrgan(bg_tile)
        else:
            self.bg_upsampler = None

        # ------------------ set up face upsampler ------------------
        if self.face_enhance:
            if self.bg_upsampler is not None:
                self.face_upsampler = self.bg_upsampler
            else:
                self.face_upsampler = self.get_realesrgan()
        else:
            self.face_upsampler = None

        # ------------------ set up CodeFormer restorer -------------------
        self.model = ARCH_REGISTRY.get("CodeFormer")(
            dim_embd=512,
            codebook_size=1024,
            n_head=8,
            n_layers=9,
            connect_list=["32", "64", "128", "256"],
        ).to(self.device)

        self.ckpt_path = load_file_from_url(
            url=pretrain_model_url["restoration"],
            model_dir=str(weights.parent),
            progress=True,
            file_name=weights.name,
        )
        checkpoint = torch.load(self.ckpt_path)["params_ema"]
        self.model.load_state_dict(checkpoint)
        self.model.eval()

        # ------------------ set up FaceRestoreHelper -------------------
        # large det_model: 'YOLOv5l', 'retinaface_resnet50'
        # small det_model: 'YOLOv5n', 'retinaface_mobile0.25'
        # if not self.has_aligned:
        #     print(f"Face detection model: {self.detection_model}")
        # if self.bg_upsampler is not None:
        #     print(f"Background upsampling: True, Face upsampling: {self.face_enhance}")
        # else:
        #     print(
        #         f"Background upsampling: False, Face upsampling: {self.face_enhance}"
        #     )

        self.face_helper = FaceRestoreHelper(
            self.upscale,
            face_size=512,
            crop_ratio=(1, 1),
            det_model=self.detection_model,
            save_ext="png",
            use_parse=True,
            device=self.device,
        )

    def upscale_image(self, image):
        # ----------------------- input & output -----------------------
        w = self.fidelity_weight
        img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        # ------------------------ processing --------------------------
        # clean all the intermediate results to process the next image
        self.face_helper.clean_all()

        if self.has_aligned:
            # the input faces are already cropped and aligned
            img = cv2.resize(img, (512, 512), interpolation=cv2.INTER_LINEAR)
            self.face_helper.is_gray = is_gray(img, threshold=10)
            if self.face_helper.is_gray:
                print("Grayscale input: True")
            self.face_helper.cropped_faces = [img]
        else:
            self.face_helper.read_image(img)
            # get face landmarks for each face
            num_det_faces = self.face_helper.get_face_landmarks_5(
                only_center_face=self.only_center_face,
                resize=640,
                eye_dist_threshold=5,
            )
            # print(f"\tdetect {num_det_faces} faces")
            # align and warp each face
            self.face_helper.align_warp_face()

            # face restoration for each cropped face
            for idx, cropped_face in enumerate(self.face_helper.cropped_faces):
                # prepare data
                cropped_face_t = img2tensor(
                    cropped_face / 255.0, bgr2rgb=True, float32=True
                )
                normalize(
                    cropped_face_t, (0.5, 0.5, 0.5), (0.5, 0.5, 0.5), inplace=True
                )
                cropped_face_t = cropped_face_t.unsqueeze(0).to(self.device)

                try:
                    with torch.no_grad():
                        output = self.model(cropped_face_t, w=w, adain=True)[0]
                        restored_face = tensor2img(
                            output, rgb2bgr=True, min_max=(-1, 1)
                        )
                    del output
                    torch.cuda.empty_cache()
                except Exception as error:
                    print(f"\tFailed inference for CodeFormer: {error}")
                    restored_face = tensor2img(
                        cropped_face_t, rgb2bgr=True, min_max=(-1, 1)
                    )

                restored_face = restored_face.astype("uint8")
                self.face_helper.add_restored_face(restored_face, cropped_face)

            # paste_back
            if not self.has_aligned:
                # upsample the background
                if self.bg_upsampler is not None:
                    # Now only support RealESRGAN for upsampling background
                    bg_img = self.bg_upsampler.enhance(img, outscale=self.upscale)[0]
                else:
                    bg_img = None
                self.face_helper.get_inverse_affine(None)
                # paste each restored face to the input image
                if self.face_enhance and self.face_upsampler is not None:
                    restored_img = self.face_helper.paste_faces_to_input_image(
                        upsample_img=bg_img,
                        draw_box=self.draw_box,
                        face_upsampler=self.face_upsampler,
                    )
                else:
                    restored_img = self.face_helper.paste_faces_to_input_image(
                        upsample_img=bg_img, draw_box=self.draw_box
                    )

        img_encode = cv2.imencode(".jpg", restored_img)[1]

        # Converting the image into numpy array
        data_encode = np.array(img_encode)

        # Converting the array to bytes.
        byte_encode = data_encode.tobytes()

        # print(f"\nAll results are saved in {result_root}")
        return byte_encode

    def get_realesrgan(self, bg_tile):
        from basicsr.archs.rrdbnet_arch import RRDBNet
        from basicsr.utils.realesrgan_utils import RealESRGANer

        use_half = False
        if torch.cuda.is_available():  # set False in CPU/MPS mode
            # set False for GPUs that don't support f16
            no_half_gpu_list = ["1650", "1660"]
            if not True in [
                gpu in torch.cuda.get_device_name(0) for gpu in no_half_gpu_list
            ]:
                use_half = True

        model = RRDBNet(
            num_in_ch=3,
            num_out_ch=3,
            num_feat=64,
            num_block=23,
            num_grow_ch=32,
            scale=2,
        )
        upsampler = RealESRGANer(
            scale=2,
            model_path="https://github.com/sczhou/CodeFormer/releases/download/v0.1.0/RealESRGAN_x2plus.pth",
            model=model,
            tile=bg_tile,
            tile_pad=40,
            pre_pad=0,
            half=use_half,
        )

        if not gpu_is_available():  # CPU
            import warnings

            warnings.warn(
                "Running on CPU now! Make sure your PyTorch version matches your CUDA."
                "The unoptimized RealESRGAN is slow on CPU. "
                "If you want to disable it, please remove `--bg_enhance` and `--face_enhance` in command.",
                category=RuntimeWarning,
            )
        return upsampler
