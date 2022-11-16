from tkinter import *
import os
from tkinter import filedialog
from PyPDF2 import PdfFileReader, PdfFileWriter


class SplitPDF(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("500x500+500+150")
        self.iconbitmap('IFLogo.ico')
        self.resizable(False, False)
        Toplevel.grab_set(self)
        
        # 
        self.textLabel1 = Label(self, text="Select your option")
        self.textLabel1.place(relx=0.25, rely=0.1)
        
        # pdf_path = filedialog.askopenfilename(title = "Select a PDF file")
        # fname = os.path.splitext(os.path.basename(pdf_path))[0]
        # pdf = PdfFileReader(pdf_path)
        # outPath = filedialog.askdirectory(title = "Select a folder where the files should be saved")
        # for page in range(pdf.getNumPages()):
        #     pdfwrite = PdfFileWriter()
        #     pdfwrite.addPage(pdf.getPage(page))
        #     outputfilename = '{}_page_{}.pdf'.format(
        #         fname, page+1)
        #     outputfile = os.path.join(outPath, outputfilename)
        #     with open(outputfile, 'wb') as out:
        #         pdfwrite.write(out)
        #     print('Created: {}'.format(outputfilename))
        
        # Toplevel.deiconify(self)