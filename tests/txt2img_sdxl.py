#!/usr/bin/env python3
from util import post_request


if __name__ == '__main__':
    payload = {
        "input": {
            "api": {
                "method": "POST",
                "endpoint": "/sdapi/v1/txt2img"
            },
            "payload": {
                "override_settings": {
                    "sd_model_checkpoint": "sd_xl_base_1.0",
                    "sd_vae": "sdxl_vae.safetensors"
                },
                "refiner_checkpoint": "sd_xl_refiner_1.0",
                "refiner_switch_at": 0.8,
                "prompt": "an astronaut riding a green horse",
                "negative_prompt": "",
                "seed": -1,
                "batch_size": 1,
                "steps": 30,
                "cfg_scale": 7,
                "width": 1024,
                "height": 1024,
                "sampler_name": "DPM++ SDE Karras",
                "sampler_index": "DPM++ SDE Karras",
                "restore_faces": False
            }
        }
    }

    post_request(payload)
