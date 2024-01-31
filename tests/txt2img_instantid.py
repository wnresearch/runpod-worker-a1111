#!/usr/bin/env python3
from util import *


if __name__ == '__main__':
    image_content = encode_image_to_base64('../data/src.jpg')

    payload = {
        "input": {
            "api": {
                "method": "POST",
                "endpoint": "/sdapi/v1/txt2img"
            },
            "payload": {
                "override_settings":{
                    "sd_model_checkpoint":"turboDiffusionXL_v112",
                    "sd_vae":"Automatic"
                },
                "prompt": "watercolor painting, vibrant, beautiful, painterly, detailed, textural, artistic",
                "negative_prompt": "(lowres, low quality, worst quality:1.2), (text:1.2), watermark, anime, photorealistic, 35mm film, deformed, glitch, low contrast, noisy",
                "seed": -1,
                "batch_size": 1,
                "steps": 15,
                "cfg_scale": 5,
                "width": 960,
                "height": 1280,
                "sampler_name": "DPM++ SDE Karras",
                "sampler_index": "DPM++ SDE Karras",
                "restore_faces": False,
                "alwayson_scripts": {
                    "controlnet": {
                        "args": [
                            {
                                "input_image": image_content,
                                "module": "instant_id_face_embedding",
                                "model": "ip-adapter_instant_id_sdxl",
                                "weight": 1,
                                "resize_mode": "Crop and Resize",
                                "lowvram": False,
                                "processor_res": 1024,
                                "threshold_a": 75,
                                "threshold_b": 75,
                                "guidance": 1,
                                "guidance_start": 0,
                                "guidance_end": 1,
                                "control_mode": "Balanced",
                                "pixel_perfect": False
                            },
                            {
                                "input_image": image_content,
                                "module": "instant_id_face_keypoints",
                                "model": "control_instant_id_sdxl",
                                "weight": 1,
                                "resize_mode": "Crop and Resize",
                                "lowvram": False,
                                "processor_res": 1024,
                                "threshold_a": 75,
                                "threshold_b": 75,
                                "guidance": 1,
                                "guidance_start": 0,
                                "guidance_end": 1,
                                "control_mode": "Balanced",
                                "pixel_perfect": False
                            }
                        ]
                    }
                }
            }
        }
    }

    post_request(payload)
