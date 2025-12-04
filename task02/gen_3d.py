
import torch
import os
import trimesh
import numpy as np
from PIL import Image
import argparse

from shap_e.diffusion.sample import sample_latents
from shap_e.diffusion.gaussian_diffusion import diffusion_from_config
from shap_e.util.notebooks import decode_latent_mesh 
from shap_e.models.download import load_model, load_config

class ShapE3DGenerator:
    def __init__(self):
        if torch.cuda.is_available():
            self.device = torch.device('cuda') # 
        else:
            self.device = torch.device('cpu')
        print(f"device: {self.device}")
        
        self.xm = load_model('transmitter', device=self.device)
        self.model = load_model('image300M', device=self.device)
        self.diffusion = diffusion_from_config(load_config('diffusion'))
        # print("models loaded")

    def generate(self, input_image, output_path="output.glb", guidance_scale=3.0, karras_steps=64):
        print("Preprocessing image...")
        if input_image.mode != "RGB":
            input_image = input_image.convert("RGB")
        input_image = input_image.resize((256, 256))

        batch_size = 1

        print(f"{karras_steps} steps")
        
        latents = sample_latents(
            batch_size=batch_size,
            model=self.model,
            diffusion=self.diffusion,
            guidance_scale=guidance_scale,
            model_kwargs=dict(images=[input_image] * batch_size),
            progress=True,
            clip_denoised=True,
            use_fp16=(self.device.type == 'cuda'), 
            use_karras=True,
            karras_steps=karras_steps,
            sigma_min=1e-3,
            sigma_max=160,
            s_churn=0,
        )

        # print("decoding mesh")
        mesh = decode_latent_mesh(self.xm, latents[0]).tri_mesh()
        # print("exporting glb")
        vertices = np.array(mesh.verts)
        faces = np.array(mesh.faces)
        vertex_colors = np.stack([
            mesh.vertex_channels['R'],
            mesh.vertex_channels['G'],
            mesh.vertex_channels['B']
        ], axis=1)
        vertex_colors = (vertex_colors * 255).astype(np.uint8)
        final_mesh = trimesh.Trimesh(
            vertices=vertices,
            faces=faces,
            vertex_colors=vertex_colors
        )
        # as shapE gives rotated output s owe re rotate
        final_mesh.apply_transform( trimesh.transformations.rotation_matrix(-np.pi / 2, [1, 0, 0]) )
        
        output_dir = os.path.dirname(output_path)
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)

        final_mesh.export(output_path)
        return output_path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', type=str, required=True)
    parser.add_argument('--output', '-o', type=str, default='output/model.glb')
    parser.add_argument('--steps', '-s', type=int, default=64)
    
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Input file not found: {args.input}")
        return

    try:
        gen = ShapE3DGenerator()
        img = Image.open(args.input)
        path = gen.generate(img, args.output, karras_steps=args.steps)
        print(f"\nSuccess! Saved to: {path}")
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
