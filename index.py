from tkinter import *
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("568x382")
window.configure(bg="#FFFFFF")


def imgtopdf():
    window.destroy()
    import i2p


def p2w():
    window.destroy()
    import os
    # use pip install pdf2docx
    stream = os.popen('pdf2docx gui')
    output = stream.read()
    output


def wordtopdf():
    window.destroy()
    import w2p


canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=382,
    width=568,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_rectangle(
    0.0,
    0.0,
    568.0,
    382.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    82.0,
    140.0,
    anchor="nw",
    text=" Each of these buttons will take you to a different GUI for operations.",
    fill="#000000",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    83.0,
    122.0,
    anchor="nw",
    text="Please click any of the conversion method buttons provided below.",
    fill="#000000",
    font=("Poppins Regular", 12 * -1)
)

canvas.create_text(
    199.0,
    31.0,
    anchor="nw",
    text="Welcome!",
    fill="#000000",
    font=("Sen Bold", 36 * -1)
)

canvas.create_text(
    118.0,
    89.0,
    anchor="nw",
    text="This is a converter application developed using python.",
    fill="#000000",
    font=("Poppins Regular", 12 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=wordtopdf,
    relief="flat"
)
button_1.place(
    x=36.0,
    y=200.0,
    width=124.0,
    height=29.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=window.destroy,
    relief="flat"
)
button_2.place(
    x=249.0,
    y=306.0,
    width=69.0,
    height=29.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=p2w,
    relief="flat"
)
button_3.place(
    x=222.0,
    y=200.0,
    width=124.0,
    height=29.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=imgtopdf,
    relief="flat"
)
button_4.place(
    x=408.0,
    y=200.0,
    width=124.0,
    height=29.0
)
window.resizable(False, False)
window.mainloop()
