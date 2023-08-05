import gradio as gr
import torch
from diffusers import DDIMScheduler, StableDiffusionImg2ImgPipeline
from PIL import Image

from diffusion_webui.utils.model_list import stable_model_list


class StableDiffusionImage2ImageGenerator:
    def __init__(self):
        self.pipe = None

    def load_model(self, model_path):
        self.pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
            model_path, safety_checker=None, torch_dtype=torch.float16
        ).to("cuda")

        self.pipe.scheduler = DDIMScheduler.from_config(
            self.pipe.scheduler.config
        )
        self.pipe.enable_xformers_memory_efficient_attention()

    def generate_image(
        self,
        model_path: str,
        prompt: str,
        negative_prompt: str,
        num_images_per_prompt: int,
        guidance_scale: int,
        num_inference_step: int,
        image_path: str,
    ):
        pipe = self.load_model(model_path)
        image = Image.open(image_path)
        images = pipe(
            prompt,
            image=image,
            negative_prompt=negative_prompt,
            num_images_per_prompt=num_images_per_prompt,
            num_inference_steps=num_inference_step,
            guidance_scale=guidance_scale,
        ).images

        return images

    def app(self):
        with gr.Blocks():
            with gr.Row():
                with gr.Column():
                    image2image_model_path = gr.Dropdown(
                        choices=stable_model_list,
                        value=stable_model_list[0],
                        label="Image-Image Model Id",
                    )

                    image2image_image_file = gr.Image(
                        type="filepath", label="Image"
                    )

                    image2image_prompt = gr.Textbox(
                        lines=1, value="Prompt", label="Prompt"
                    )

                    image2image_negative_prompt = gr.Textbox(
                        lines=1,
                        value="Negative Prompt",
                        label="Negative Prompt",
                    )

                    image2image_num_images_per_prompt = gr.Slider(
                        minimum=1,
                        maximum=30,
                        step=1,
                        value=10,
                        label="Num Images Per Prompt",
                    )

                    with gr.Accordion("Advanced Options", open=False):
                        image2image_guidance_scale = gr.Slider(
                            minimum=0.1,
                            maximum=15,
                            step=0.1,
                            value=7.5,
                            label="Guidance Scale",
                        )

                        image2image_num_inference_step = gr.Slider(
                            minimum=1,
                            maximum=100,
                            step=1,
                            value=50,
                            label="Num Inference Step",
                        )

                    image2image_predict_button = gr.Button(value="Generator")

                with gr.Column():
                    output_image = gr.Gallery(
                        label="Generated images",
                        show_label=False,
                        elem_id="gallery",
                    ).style(grid=(1, 2))

        image2image_predict_button.click(
            fn=StableDiffusionImage2ImageGenerator().generate_image,
            inputs=[
                image2image_model_path,
                image2image_prompt,
                image2image_negative_prompt,
                image2image_num_images_per_prompt,
                image2image_guidance_scale,
                image2image_num_inference_step,
                image2image_image_file,
            ],
            outputs=[self.output_image],
        )
