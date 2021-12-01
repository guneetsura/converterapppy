from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo
from docx2pdf import convert
from tkinter.filedialog import askopenfilename,asksaveasfile
from PyPDF2 import PdfFileReader
import PyPDF2

root = Tk()

root.title("Converter App")

label = Label(root, text = "Welcome to the converter app!")
label.grid(row=0,column=0)
label2 = Label(root,text = "Please select the file conversion method from below.")
label2.grid(row=1, column=0)

def imgtopdf():
	root.destroy()
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

button1 = Button(root, text = "Word to PDF", command = wordtopdf)
button1.grid(row=2, column=0)

button2= Button(root, text="PDF to Word", command = pdftoword)
button2.grid(row=3, column=0)

button3= Button(root, text="Image to PDF", command=imgtopdf)
button3.grid(row=4, column=0)

button4= Button(root, text="Quit", command=root.destroy)
button4.grid(row=5, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()