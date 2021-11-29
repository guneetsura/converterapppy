# Import Module
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilenames, asksaveasfile
import img2pdf
from tkinter.messagebox import showinfo
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets_img")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


imga = Tk()

imga.geometry("800x400")
imga.configure(bg = "#FFFFFF")

def select_file():
	global file_names
	file_names = askopenfilenames(initialdir = "/",
								title = "Select File",
                                filetypes=[('image files!', '*.png;*.jpg')])

# IMAGE TO PDF
def image_to_pdf():
	for index, file_name in enumerate(file_names):
		with open(f"Image_to_pdf-file {index}.pdf", "wb") as f:
			f.write(img2pdf.convert(file_name))
			showinfo("Done","Successfully Converted to PDF!")
			

# IMAGES TO PDF
def images_to_pdf():
	fn = asksaveasfile(mode='w',defaultextension=".pdf", filetypes=[("pdf file","*.pdf")]).name
	with open(f"" + fn, "wb") as f:
		f.write(img2pdf.convert(file_names))
		showinfo("Done","Successfully Converted and combined to PDF!")


canvas = Canvas(
    imga,
    bg = "#FFFFFF",
    height = 400,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    800.0,
    400.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    252.0,
    35.0,
    anchor="nw",
    text="Image Converter",
    fill="#000000",
    font=("Sen Bold", 36 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=image_to_pdf,
    relief="flat"
)
button_1.place(
    x=164.0,
    y=176.0,
    width=473.0,
    height=39.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=images_to_pdf,
    relief="flat"
)
button_2.place(
    x=164.0,
    y=247.0,
    width=473.0,
    height=39.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=imga.destroy,
    relief="flat"
)
button_3.place(
    x=350.0,
    y=327.0,
    width=100.0,
    height=36.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=select_file,
    relief="flat"
)
button_4.place(
    x=340.0,
    y=109.0,
    width=120.0,
    height=36.0
)
imga.resizable(False, False)
imga.mainloop()
