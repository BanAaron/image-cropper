import os
import uuid
import glob
from PIL import Image

current_working_directory = os.getcwd()

for images in glob.glob(f"{current_working_directory}\\test_images\\*.jpg"):
    with Image.open(images) as im:
        base_name = os.path.basename(images)
        im.crop((960, 0, 2880, 1080)).save(f"output\\{base_name}")
