
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/saraimora/Documents/project_24/build/assets/frame5")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1512x982")
window.configure(bg = "#EFEFEF")


canvas = Canvas(
    window,
    bg = "#EFEFEF",
    height = 982,
    width = 1512,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    135.0,
    106.0,
    1377.0,
    383.0,
    fill="#DFD9E2",
    outline="")

canvas.create_rectangle(
    135.0,
    588.0,
    1377.0,
    865.0,
    fill="#615D6C",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    333.0,
    230.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    709.0,
    714.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    616.0,
    244.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    894.0,
    241.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    1103.0,
    720.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    1190.0,
    243.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    333.0,
    741.0,
    image=image_image_7
)

canvas.create_text(
    291.0,
    335.0,
    anchor="nw",
    text="Cleanser",
    fill="#000000",
    font=("WorkSansRoman Regular", 20 * -1)
)

canvas.create_text(
    1072.0,
    820.0,
    anchor="nw",
    text="Lotion",
    fill="#DFD9E2",
    font=("WorkSansRoman Regular", 20 * -1)
)

canvas.create_text(
    667.0,
    821.0,
    anchor="nw",
    text="Cleanser",
    fill="#DFD9E2",
    font=("WorkSansRoman Regular", 20 * -1)
)

canvas.create_text(
    257.0,
    822.0,
    anchor="nw",
    text="Cleansing Balm",
    fill="#DFD9E2",
    font=("WorkSansRoman Regular", 20 * -1)
)

canvas.create_text(
    1145.0,
    339.0,
    anchor="nw",
    text="Sunscreen",
    fill="#000000",
    font=("WorkSansRoman Regular", 20 * -1)
)

canvas.create_text(
    863.0,
    337.0,
    anchor="nw",
    text="Lotion",
    fill="#000000",
    font=("WorkSansRoman Regular", 20 * -1)
)

canvas.create_text(
    532.0,
    334.0,
    anchor="nw",
    text="Vitamin C Serum",
    fill="#000000",
    font=("WorkSansRoman Regular", 20 * -1)
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    391.0,
    520.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    400.0,
    53.0,
    image=image_image_9
)
window.resizable(False, False)
window.mainloop()
