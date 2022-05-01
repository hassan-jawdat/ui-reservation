from tkinter import *
from tkinter import  ttk
from tkinter import  messagebox
from  DbConnect import DBConnect
from  ListRequest import  ListTicket
dbConnect=DBConnect()
root=Tk()
root.title("Ticket reservation")
root.configure(background="#e1d8b2")
#style=
style=ttk.Style()
style.theme_use('classic')
style.configure('TLabel',background="#e1d8b2")
style.configure('TButton',background="#e1d8b2")
style.configure('TRadiobutton',background="#e1d8b2")
#full name
ttk.Label(root, text="full Name:").grid(row=0,column=0,padx=10,pady=10)
EntryFullName=ttk.Entry(root, width=30, font=('Arial',16))
EntryFullName.grid(row=0,column=1, columnspan=2, pady=10)
#Email
ttk.Label(root, text="Email:").grid(row=1,column=0,padx=10,pady=10)
EntryEmail=ttk.Entry(root, width=30, font=('Arial',16))
EntryEmail.grid(row=1,column=1, columnspan=2, pady=10)
#telefon
ttk.Label(root, text="telefon:").grid(row=2,column=0,padx=10,pady=10)
Entrytelefon=ttk.Entry(root, width=30, font=('Arial',16))
Entrytelefon.grid(row=2,column=1, columnspan=2, pady=10)

#gender
ttk.Label(root, text="Gender:").grid(row=3,column=0)
SpanGender=StringVar()
ttk.Radiobutton(root,text="Male",variable=SpanGender, value="male").grid(row=3,column=1)
ttk.Radiobutton(root,text="Female",variable=SpanGender, value="Female").grid(row=3,column=2)

#comment
ttk.Label(root, text="Comments:").grid(row=4,column=0)
txtComments=Text(root, width=30, height=15, font=('Arial',16))
txtComments.grid(row=4,column=1, columnspan=2)

#buttons
buSubmit=ttk.Button(root,text="Submit")
buSubmit.grid(row=5,column=3)
buList=ttk.Button(root,text="List Res.")
buList.grid(row=5,column=2)


def BuSaveData():
    #print("Full Name:{}".format(EntryFullName.get()))
    #print("Gender:{}".format(SpanGender.get()))
    #print("Comments:{}".format(txtComments.get(1.0,'end')))
    msg=dbConnect.Add(EntryFullName.get(),EntryEmail.get(),Entrytelefon.get(),SpanGender.get(),txtComments.get(1.0,'end'))
    messagebox.showinfo(title="Add info",message=msg)
    EntryFullName.delete(0,'end')
    txtComments.delete(1.0,'end') 

def BulistData():
    #TODO: show orders
    #print(' not implemented yet')
    listrequset=ListTicket()

buSubmit.config(command=BuSaveData)
buList.config(command=BulistData)
root.mainloop()