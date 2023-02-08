import os
import glob
from PIL import Image

current_working_directory = os.getcwd()

for images in glob.glob(f"{current_working_directory}\\test_images\\*.jpg"):
    with Image.open(images) as im:
        im.rotate(180).show()
