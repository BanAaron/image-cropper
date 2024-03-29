class ImageHandler:
    import os
    import logging
    from PIL import Image
    from tkinter import filedialog

    def __init__(self):
        self.repr = "Class to handle the logic of cropping images"
        self.image_file_paths = ""
        self.working_dir = self.os.getcwd()
        self.crop_box = (960, 0, 2880, 1080)
        self.pil_image = self.Image

        # sets the logging level to debug
        self.logging_flag = False
        if self.logging_flag:
            self.logging.getLogger().setLevel(self.logging.DEBUG)

    def __repr__(self):
        return self.repr

    def get_crop_box(self):
        self.logging.debug(f"get_crop_box: {self.crop_box}")
        return self.crop_box

    def set_crop_box(self, box: tuple[int, int, int, int]):
        self.logging.debug(f"set_crop_box: params: {box}")
        self.crop_box = box
        return self.crop_box

    def set_image_file_paths(self):
        self.image_file_paths = self.filedialog.askopenfilenames(
            initialdir=self.working_dir,
            filetypes=[("image files", (".png", ".jpg", ".jpeg"))],
        )
        self.logging.debug(
            f"set_image_file_paths: files selected: {self.image_file_paths}"
        )

    def get_image_file_paths(self):
        self.logging.debug(self.image_file_paths)
        return self.image_file_paths

    # TODO: make output configurable
    # TODO: make paths system agnostic
    def crop_images(self, image_file_path: str, crop_box: tuple[int, int, int, int]):
        self.logging.debug(f"cropping images")
        for image_file in image_file_path:
            with self.pil_image.open(image_file) as im:
                im = im.crop(crop_box)
                base_name = self.os.path.basename(image_file)
                im.save(f"output\\{base_name}")
                self.logging.debug(f"saved to: output\\{base_name}")


if __name__ == "__main__":
    image_handler = ImageHandler()
