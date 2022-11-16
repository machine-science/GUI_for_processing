from tkinter import ttk, Tk, Frame, Button, BOTTOM, CENTER, filedialog
import os
from PyPDF2 import PdfFileReader, PdfFileWriter


class Main(object):
    def __init__(self,master):
        self.master = master
        
        self.mainFrame = Frame(self.master, relief="sunken", borderwidth=4)
        self.mainFrame.place()
        
        # Center frame
        self.centerFrame = Frame(self.master, width=400, height=200, bg='#435EA9', relief='sunken')
        self.centerFrame.place(relx=.5, rely=.5,anchor= CENTER)
        
        #Add buttons
        self.split_button = Button(self.centerFrame, width=50, height=2, bg='#63CD41', relief='sunken', text="Split PDF", command=self.splitPdf)
        self.split_button.place(relx=.5, rely=.2,anchor= CENTER)
        
        self.merge_button = Button(self.centerFrame, width=50, height=2, bg='#63CD41', relief='sunken', text="Merger PDF", command=None)
        self.merge_button.place(relx=.5, rely=.7,anchor= CENTER)
        
    def splitPdf(self):
        pdf_path = filedialog.askopenfilename()
        fname = os.path.splitext(os.path.basename(pdf_path))[0]
        pdf = PdfFileReader(pdf_path)
        outPath = filedialog.askdirectory(title = "Select a folder where the files should be saved")
        for page in range(pdf.getNumPages()):
            print(page)
            pdfwrite = PdfFileWriter()
            pdfwrite.addPage(pdf.getPage(page))
            outputfilename = '{}_page_{}.pdf'.format(
                fname, page+1)
            outputfile = os.path.join(outPath, outputfilename)
            with open(outputfile, 'wb') as out:
                pdfwrite.write(out)
            print('Created: {}'.format(outputfilename))
        
        
def main():
    root = Tk()
    app = Main(root)
    root.title("Main Page")
    root.geometry("500x500+500+150")
    root.iconbitmap('IFLogo.ico')
    root.mainloop()

if __name__ == "__main__":
    main()
    