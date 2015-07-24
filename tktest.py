from Tkinter import *

class App(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.pack()
        self.initWidgets()
    def initWidgets(self):
        self.info = Label(self)
        self.info["text"] = "You have received a virus."
        self.info["fg"] = "purple"
        self.info.pack({"side":"left"})

        self.dismiss = Button(self)
        self.dismiss["text"] = "Dismiss"
        self.dismiss["command"] = self.dismiss
        self.dismiss.pack({"side":"right"})
    def dismiss(self):
        root.quit()
root = Tk()
window = App(master=root)
window.mainloop()
