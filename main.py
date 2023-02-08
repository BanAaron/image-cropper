import os
import uuid
import glob
from PIL import Image

current_working_directory = os.getcwd()

# for images in glob.glob(f"{current_working_directory}\\test_images\\*.jpg"):
#     with Image.open(images) as im:
#         im.rotate(180).show()

with Image.open("C:\\Users\\aaron\\Documents\\Code\\pyImageCropper\\test_images\\20230125182337_1.jpg") as im:
    im.crop((960, 0, 2880, 1080)).save(f"output\\{uuid.uuid4()}.jpg")
