from Tkinter import *
root=Tk()
def add():
    res = float(e1.get())+float(e2.get())
    Label(root,text="Result :" + str(res),fg="white",bg="black").grid(row=4,column=0)
def subtract():
    res = float(e1.get())-float(e2.get())
    Label(root,text="Result :" + str(res),fg="white",bg="black").grid(row=4,column=0)
def multiply():
    res = float(e1.get())*float(e2.get())
    Label(root,text="Result :" + str(res),fg="white",bg="black").grid(row=4,column=0)
def divide():
    res = float(e1.get())/float(e2.get())
    Label(root,text="Result :" + str(res),fg="white",bg="black").grid(row=4,column=0)

Label(root,text="First number").grid(row=0,column=0)
Label(root,text="Second number").grid(row=1,column=0)
e1=Entry(root)
e2=Entry(root)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
Button(root,text="Add",command=add).grid(row=2,column=0)
Button(root,text="Subtract",command=subtract).grid(row=2,column=1)
Button(root,text="Multiply",command=multiply).grid(row=3,column=0)
Button(root,text="Divide",command=divide).grid(row=3,column=1)
Button(root,text="Quit",command=root.destroy).grid(row=5,column=0)
mainloop()
