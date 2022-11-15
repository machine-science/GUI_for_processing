from tkinter import ttk, Tk, Frame, Button, BOTTOM, CENTER


class Main(object):
    def __init__(self,master):
        self.master = master
        
        mainFrame = Frame(self.master, relief="sunken", borderwidth=4)
        mainFrame.place()
        
          
        # middelFrame1 = Frame(mainFrame, width=400, bg='red', relief='sunken')
        # middelFrame1.pack(side=BOTTOM)
        
        # Center frame
        centerFrame = Frame(self.master, width=400, height=200, bg='#435EA9', relief='sunken')
        centerFrame.place(relx=.5, rely=.5,anchor= CENTER)
        
        #Add buttons
        addButton = Button(centerFrame, width=50, height=2, bg='#63CD41', relief='sunken')
        addButton.place(relx=.5, rely=.2,anchor= CENTER)
        
        addButton = Button(centerFrame, width=50, height=2, bg='#63CD41', relief='sunken')
        addButton.place(relx=.5, rely=.7,anchor= CENTER)
        
        
def main():
    root = Tk()
    app = Main(root)
    root.title("Main Page")
    root.geometry("500x500+500+150")
    root.iconbitmap('IFLogo.ico')
    root.mainloop()

if __name__ == "__main__":
    main()
    