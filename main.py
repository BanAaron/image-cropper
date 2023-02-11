class Cropper:
    import os
    import logging
    import tkinter as tk
    from tkinter import filedialog
    import PIL.Image

    def __init__(self):
        self.repr = "Class to handle the logic of cropping images"
        self.file_path: str
        self.working_dir = self.os.getcwd()
        self.crop_box = (0, 0, 0, 0)
        self.run = True

        # create tkinter ui
        self.window = self.tk.Tk()
        # hide the default window
        self.window.withdraw()

        # sets the logging level to debug
        self.logging_flag = True
        if self.logging_flag:
            self.logging.getLogger().setLevel(self.logging.DEBUG)

        self.set_crop_box((960, 0, 2880, 1080))
        self.crop_image(self.open_image(), self.get_crop_box())

    def __repr__(self):
        return self.repr

    def get_crop_box(self):
        self.logging.debug(f"get_crop_box: {self.crop_box}")
        return self.crop_box

    def set_crop_box(self, box: tuple[int, int, int, int]):
        for x in box:
            if x < 0:
                raise Exception("Values must be 0 or above")

        self.logging.debug(f"set_crop_box: {box}")
        self.crop_box = box

    def get_logging_flag(self):
        return self.get_logging_flag()

    def set_logging_flag(self, boolean: bool):
        self.logging_flag = boolean
        return self.logging_flag

    def open_image(self):
        image_file_path = self.filedialog.askopenfilenames(initialdir=self.working_dir)
        if not image_file_path:
            pass
        self.logging.debug(f"image_file_paths: {image_file_path}")
        return image_file_path

    def crop_image(self, image_file_paths: str, crop_box: tuple[int, int, int, int]):
        for image_file in image_file_paths:
            with self.PIL.Image.open(image_file) as im:
                im = im.crop(crop_box)
                base_name = self.os.path.basename(image_file)
                im.save(f"output\\{base_name}")


cropper = Cropper()
