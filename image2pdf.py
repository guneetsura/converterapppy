# Import Module
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilenames
import img2pdf
from tkinter.messagebox import showinfo

# Create Object
imgc = tk.Tk()
imgc.title("IMAGE TO PDF converter")
# set Geometry
imgc.geometry('1100x300')

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
	with open(f"Image_to_pdf-file.pdf", "wb") as f:
		f.write(img2pdf.convert(file_names))
		showinfo("Done","Successfully Converted and combined to PDF!")

# Add Labels and Buttons
Label(imgc, text = "IMAGE CONVERSION",
	font = "italic 15 bold").pack(pady = 10)

Button(imgc, text = "Select Images",
	command = select_file, font = 14).pack(pady = 10)

frame = Frame()
frame.pack(pady = 20)

Button(frame, text = "Image to PDF(Separate pdf of every image inserted)",
	command = image_to_pdf,
	relief = "solid",
	bg = "white", font = 15).pack(side = LEFT, padx = 10)

Button(frame, text = "Images to PDF(combined pdf of every image inserted)",
	command = images_to_pdf, relief = "solid",
	bg = "white", font = 15).pack()

quit_btn = Button(imgc, text="Quit", command=imgc.destroy)
quit_btn.pack(pady=10, padx=10, ipadx=10)
# Execute Tkinter
imgc.mainloop()