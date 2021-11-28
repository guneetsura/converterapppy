
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo
from docx2pdf import convert
from tkinter.filedialog import askopenfilename,asksaveasfile
from PyPDF2 import PdfFileReader
import PyPDF2
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("568x382")
window.configure(bg = "#FFFFFF")

def imgtopdf():
	window.destroy()
	import image2pdf
	

def wordtopdf():
	win=tk.Tk()
	win.title("Word to Pdf Converter App")

	def openfile():
		file = askopenfile(initialdir = "/", filetypes=[('Word Files', '*.docx')])
		def savename():
			convert(
			file.name,    
			r'.../' + fname.get() + '.pdf'
			)  
			fname.delete(0, END) 
			showinfo("Done", "File successfully converted ")
		fname = Entry(win, width=30)
		fname.grid(row=30, column=5)
		fname_label = Label(win, text='Save file name')
		fname_label.grid(row=30, column=4)
		sname = Button(win, text="Save Name", command=savename)
		sname.grid(row=40,column=5)
		

	label=tk.Label(win,text="Choose a file!")
	label.grid(row=10,column=5,padx=5,pady=5)

	button=ttk.Button(win,text="Select",width=30,command=openfile)
	button.grid(row=20,column=5,padx=5,pady=5)

	qb = ttk.Button(win, text="Quit", command=win.destroy)
	qb.grid(row=50, column=5, padx=5, pady=5)

	win.mainloop()
	

def pdftoword():
	def openFile():
		file = askopenfilename(defaultextension=".pdf", 
                                          filetypes=[("Pdf files","*.pdf")])
		if file == "":
			file = None
		
		else:
			fileEntry.delete(0,END)
			fileEntry.config(fg="blue")
			fileEntry.insert(0,file)
	def convert():
		try:
			pdf = fileEntry.get()
			pdfFile = open(pdf, 'rb')
			# creating a pdf reader object
			pdfReader = PdfFileReader(pdfFile) 

			# creating a page object
			pageObj = pdfReader.getPage(0) 
		
			# extracting text from page 
			extractedText= pageObj.extractText()
			readPdf.delete(1.0,END)
			readPdf.insert(INSERT,extractedText)

			# closing the pdf file object 
			pdfFile.close()
		except FileNotFoundError:
			fileEntry.delete(0,END)
			fileEntry.config(fg="red")
			fileEntry.insert(0,"Please select a pdf file first")
		except:
			pass

		
	def save2word():
		text = str(readPdf.get(1.0,END))
		wordfile = asksaveasfile(mode='w',defaultextension=".doc", 
											filetypes=[("word file","*.doc"),
														("text file","*.txt"),
														("Python file","*.py")])
		
		if wordfile is None:
			return
		wordfile.write(text)
		wordfile.close()
		print("saved")
		fileEntry.delete(0,END)
		fileEntry.insert(0,"pdf Extracted and Saved...")



		
	#=================== Front End Design
	up = Tk()
	up.geometry("600x350")
	up.config(bg="light blue")
	up.title("PDF Converter")
	up.resizable(0,0)
	# try:
	# 	up.wm_iconbitmap("pdf2.ico")
	# except:
	# 	print('icon file is not available')
	# 	pass
	file= ""
	defaultText = "\n\n\n\n\t\t Your extracted text will apear here.\n \t\t     you can modify that text too."
	#==============App Name==============================================================>>
	appName = Label(up,text="PDF to WORD Converter ",font=('arial',20,'bold'),
					bg="light blue",fg='maroon')
	appName.place(x=150,y=5)
	#Select pdf file
	labelFile = Label(up,text="Select Pdf File",font=('arial',12,'bold'))
	labelFile.place(x=30,y=50)
	fileEntry = Entry(up,font=('calibri',12),width=40)
	fileEntry.pack(ipadx=200,pady=50,padx=150)
	#===========button to access openFile method=================================
	# pageNumLbl = Label(up, text='Enter page number')
	# pageNumLbl.pack()
	# pageNum = Entry(up, width=30)
	# pageNum.pack()
	
	openFileButton = Button(up,text=" Open ",font=('arial',12,'bold'),width=30,
						bg="sky blue",fg='green',command=openFile)
	openFileButton.place(x=150,y=80)
	#===========button to access convert method=================================
	convert2Text = Button(up,text="Read",font=('arial',8,'bold'),
					bg="RED",fg='WHITE',width=20,command=convert)
	convert2Text.place(x=250,y=120)
	#======================= Text Box to read pdf file and modify ===================>>
	readPdf = Text(up,font=('calibri',12),fg='light green',bg='black',width=60,height=30,bd=10)
	readPdf.pack(padx=20,ipadx=20,pady=20,ipady=20)
	readPdf.insert(INSERT,defaultText)
	#===============================Button to access save2word method=================
	save2Word = Button(up,text="Save to Word File",font=('arial',10,'bold'),
					bg="RED",fg='WHITE',command=save2word)
	save2Word.place(x=255,y=320)

	#===================halt window=============================>>
	if __name__ == "__main__":
		up.mainloop()

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 382,
    width = 568,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
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
    command=pdftoword,
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
