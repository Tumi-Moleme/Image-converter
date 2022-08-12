from tkinter import image_names
from PIL import Image
import glob

images = glob.glob('*.png')

print(images)

for image in images:
  img = Image.open(image)
  rgb_img = img.convert('RGB')
  rgb_img.save(image.replace("png","jpg"), quality=95)