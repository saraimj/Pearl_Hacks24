
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/saraimora/Documents/project_24/build/assets/frame4")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1512x982")
window.configure(bg = "#DFD9E2")


canvas = Canvas(
    window,
    bg = "#DFD9E2",
    height = 982,
    width = 1512,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    755.5,
    366.5,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    756.0,
    557.5,
    image=image_image_2
)

canvas.create_rectangle(
    575.5,
    605.5,
    936.5,
    681.5,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    509.0,
    681.5,
    1003.0,
    757.5,
    fill="#000000",
    outline="")
window.resizable(False, False)
window.mainloop()
