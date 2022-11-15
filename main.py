from tkinter import ttk, Tk, Frame, Button


class Main(object):
    def __init__(self,master):
        self.master = master
        
        mainFrame = Frame(self.master, relief="sunken", borderwidth=4)
        mainFrame.pack()
        
        middelFrame = Frame(mainFrame, width=1350, bg='red', relief='sunken')
        
        
def main():
    root = Tk()
    app = Main(root)
    root.title("Main Page")
    root.geometry("1350x750+350+200")
    root.iconbitmap('IFLogo.ico')
    root.mainloop()

if __name__ == "__main__":
    main()
    