from tkinter import ttk, Tk, Frame, Button, BOTTOM, CENTER, filedialog, Toplevel, Label


class MergePDF(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("500x500+500+150")
        self.iconbitmap('IFLogo.ico')
        self.resizable(False, False)
        self.configure(bg='#CFF5E7')
        Toplevel.grab_set(self)
        
        # 
        self.textLabel1 = Label(self, text="COMING SOON...", height=20, fg="red", font='Helvetica 18 bold', bg='#CFF5E7')
        self.textLabel1.place(relx=0.2, rely=0.1)