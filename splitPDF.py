from tkinter import *
import os
from tkinter import filedialog, messagebox
from PyPDF2 import PdfFileReader, PdfFileWriter
from tktooltip import ToolTip


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
        
        self.v = StringVar(self, "1")
 
        # Dictionary to create multiple buttons
        values = {"Single page split" : "1",
                "Combination split" : "2"}
        rely = 0
        self.btnList = []
        print("Initial value of v:", self.v.get() )
        
        for i, (text, value) in enumerate(values.items()):
            self.btnList.append(Radiobutton(self, text = text, variable = self.v,
                        value = value))
            if i == 0:
                self.btnList[i].place(relx = 0.1, rely=rely+0.2)
                ToolTip(self.btnList[i], msg="This option will split PDF into single pages")
                rely = 0.2
            else:
                self.btnList[i].place(relx = 0.1, rely=rely)
                ToolTip(self.btnList[i], msg="This option will split PDF according to the user specification")
            rely=rely+0.05
            
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            exit()
            

        
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