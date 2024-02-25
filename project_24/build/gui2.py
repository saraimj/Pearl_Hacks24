
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/saraimora/Documents/project_24/build/assets/frame2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("586x1648")
window.configure(bg = "#212121")


canvas = Canvas(
    window,
    bg = "#212121",
    height = 1648,
    width = 586,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    455.0,
    25.0,
    566.5500030517578,
    66.4000015258789,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    24.0,
    24.0,
    562.0,
    86.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    24.0,
    106.0,
    562.0,
    267.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    24.0,
    287.0,
    562.0,
    450.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    24.0,
    470.0,
    562.0,
    633.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    24.0,
    653.0,
    562.0,
    828.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    24.0,
    848.0,
    562.0,
    1023.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    24.0,
    1043.0,
    562.0,
    1206.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    24.0,
    1226.0,
    562.0,
    1336.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    24.0,
    1356.0,
    562.0,
    1518.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    24.0,
    1538.0,
    562.0,
    1624.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    0.0,
    0.0,
    538.0,
    110.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    0.0,
    0.0,
    538.0,
    110.0,
    fill="#000000",
    outline="")
window.resizable(False, False)
window.mainloop()
