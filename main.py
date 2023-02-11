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

        # create tkinter ui
        self.window = self.tk.Tk()
        # this hides the default window
        self.window.withdraw()

        # sets the logging level to debug
        self.logging_flag = True
        if self.logging_flag:
            self.logging.getLogger().setLevel(self.logging.DEBUG)

        # this should be set in the UI, call function set_crop_box
        self.set_crop_box((960, 0, 2880, 1080))
        self.crop_image(self.open_image(), self.get_crop_box())

    def __repr__(self):
        return self.repr

    def get_crop_box(self):
        self.logging.debug(f"get_crop_box: {self.crop_box}")
        return self.crop_box

    def set_crop_box(self, box: tuple[int, int, int, int]):
        self.logging.debug(f"set_crop_box: {box}")
        self.crop_box = box

    def open_image(self):
        image_file_path = self.filedialog.askopenfilename(initialdir=self.working_dir)
        self.logging.debug(f"image_file_path: {image_file_path}")
        return image_file_path

    # TODO: get this working with multiple images at the same time
    def open_images(self):
        return self.filedialog.askopenfilenames(initialdir=self.working_dir)

    def crop_image(self, image_file_path: str, crop_box: tuple[int, int, int, int]):
        with self.PIL.Image.open(image_file_path) as im:
            im = im.crop(crop_box)
            base_name = self.os.path.basename(image_file_path)
            im.save(f"output\\{base_name}")


cropper = Cropper()
