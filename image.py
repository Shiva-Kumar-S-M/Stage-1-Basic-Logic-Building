import torch
from torch import nn
from torchvision.utils import save_image
from torchvision import transforms
from PIL import Image
import os

# image.py


# Simple Generator model (DCGAN-like)
class Generator(nn.Module):
    def __init__(self, latent_dim, img_shape):
        super(Generator, self).__init__()
        self.img_shape = img_shape
        self.model = nn.Sequential(
            nn.Linear(latent_dim, 128),
            nn.ReLU(True),
            nn.Linear(128, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(True),
            nn.Linear(256, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(True),
            nn.Linear(512, int(torch.prod(torch.tensor(img_shape)))),
            nn.Tanh()
        )

    def forward(self, z):
        img = self.model(z)
        img = img.view(img.size(0), *self.img_shape)
        return img

# Function to generate and save images
def generate_images(generator, latent_dim, num_images, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    z = torch.randn(num_images, latent_dim)
    with torch.no_grad():
        generated_imgs = generator(z)
        generated_imgs = (generated_imgs + 1) / 2  # Rescale to [0,1]
        for i, img in enumerate(generated_imgs):
            save_image(img, os.path.join(output_dir, f"generated_{i+1}.png"))

if __name__ == "__main__":
    latent_dim = 100
    img_shape = (1, 28, 28)  # Example: grayscale 28x28 images
    generator = Generator(latent_dim, img_shape)
    
    # For demonstration, use untrained generator
    generate_images(generator, latent_dim, num_images=5, output_dir="generated_images")
    print("Images generated in 'generated_images' folder.")