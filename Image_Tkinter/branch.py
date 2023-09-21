import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def create_image_viewer():
    def open_image():
        file_path = filedialog.askopenfilename()
        if file_path:
            image = Image.open(file_path)
            photo = ImageTk.PhotoImage(image)
            label.config(image=photo)
            label.image = photo


    root = tk.Tk()
    root.title("Display Image")


    label = tk.Label(root)
    label.pack()


    open_button = tk.Button(root, text="Open Image", command=open_image)
    open_button.pack()

    root.mainloop()


