class PyImageCropper:
    import sys
    import logic
    import logging
    import tkinter as tk

    def __init__(self):
        self.repr = "Main class for pyImageCropper"
        self.logging.debug(f"initializing")

        # image processing logic
        self.logging.debug(f"load:logic.ImageHandler")
        self.image_handler = self.logic.ImageHandler()

        if self.image_handler.logging_flag:
            self.logging.getLogger().setLevel(self.logging.DEBUG)

        self.logging.debug(f"load:tkinter window")
        # create UI
        self.window = self.tk.Tk()
        self.window.title(self.__class__.__name__)
        self.window.wm_geometry("500x175")
        self.window.resizable(False, False)

        self.logging.debug(f"load:tkinter buttons")
        # create ui buttons
        self.button_exit = self.tk.Button(text="Exit", command=self.button_exit_func)
        self.button_exit.place(x=450, y=135)

        self.button_get_images = self.tk.Button(
            text="Select", command=lambda: self.button_get_images_func()
        )
        self.button_get_images.place(x=10, y=10)

        self.button_crop = self.tk.Button(text="Crop", command=self.button_crop_func)
        self.button_crop.place(x=60, y=10)

        self.logging.debug(f"load:tkinter entries and labels")
        # crop box entries
        self.crop_box_default_values = self.image_handler.get_crop_box()
        self.entry_box_offset = 50

        # left
        self.entry_left_string = self.tk.StringVar()
        self.entry_left_string.set(self.crop_box_default_values[0])
        self.entry_left_label = self.tk.Label(text="Left:")
        self.entry_left_label.place(x=10, y=50)
        self.entry_left = self.tk.Entry(textvariable=self.entry_left_string)
        self.entry_left.place(
            x=int(self.entry_left_label.place_info().get("x")) + self.entry_box_offset,
            y=int(self.entry_left_label.place_info().get("y")),
        )
        # top
        self.entry_top_string = self.tk.StringVar()
        self.entry_top_string.set(self.crop_box_default_values[1])
        self.entry_top_label = self.tk.Label(text="Top:")
        self.entry_top_label.place(x=10, y=75)
        self.entry_top = self.tk.Entry(textvariable=self.entry_top_string)
        self.entry_top.place(
            x=int(self.entry_top_label.place_info().get("x")) + self.entry_box_offset,
            y=int(self.entry_top_label.place_info().get("y")),
        )
        # right
        self.entry_right_string = self.tk.StringVar()
        self.entry_right_string.set(self.crop_box_default_values[2])
        self.entry_right_label = self.tk.Label(text="Right:")
        self.entry_right_label.place(x=10, y=100)
        self.entry_right = self.tk.Entry(textvariable=self.entry_right_string)
        self.entry_right.place(
            x=int(self.entry_right_label.place_info().get("x")) + self.entry_box_offset,
            y=int(self.entry_right_label.place_info().get("y")),
        )
        # bottom
        self.entry_bottom_string = self.tk.StringVar()
        self.entry_bottom_string.set(self.crop_box_default_values[3])
        self.entry_bottom_label = self.tk.Label(text="Bottom:")
        self.entry_bottom_label.place(x=10, y=125)
        self.entry_bottom = self.tk.Entry(textvariable=self.entry_bottom_string)
        self.entry_bottom.place(
            x=int(self.entry_bottom_label.place_info().get("x"))
            + self.entry_box_offset,
            y=int(self.entry_bottom_label.place_info().get("y")),
        )

        # start program loop
        self.logging.debug(f"load:tkinter mainloop")
        self.window.mainloop()

    def button_get_images_func(self):
        self.logging.debug(f"button_get_images_func:called")
        self.image_handler.set_image_file_paths()

    def button_crop_func(self):
        self.logging.debug(f"button_crop_func:called")
        self.image_handler.set_crop_box(
            (
                int(self.entry_left_string.get()),
                int(self.entry_top_string.get()),
                int(self.entry_right_string.get()),
                int(self.entry_bottom_string.get()),
            )
        )
        self.image_handler.crop_images(
            self.image_handler.get_image_file_paths(), self.image_handler.get_crop_box()
        )

    def button_exit_func(self):
        self.logging.debug(f"button_exit_func:called")
        self.sys.exit()


if __name__ == "__main__":
    cropper = PyImageCropper()
