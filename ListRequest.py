from tkinter import *
from tkinter import  ttk
from DbConnect import DBConnect
dbconnect=DBConnect()

class ListTicket:

    def __init__(self):
         self._root=Tk()
         self._dbconnect=DBConnect()
         tv=ttk.Treeview(self._root)
         tv.pack()
         tv.heading('#0',text='ID')
         tv.configure(column=('#Name', '#Email','#Gender', '#Comment'))
         tv.heading('#Name', text='Name')
         tv.heading('#Email', text='Email')
         tv.heading('#Gender', text='Gender')
         tv.heading('#Comment', text='Comment')
         cursor=self._dbconnect.ListRequest()
         for row in cursor:
             tv.insert('','end','#{}'.format(row['ID']),text=row['ID'])
             tv.set('#{}'.format(row['ID']),'#Name', row['Name'])
             tv.set('#{}'.format(row['ID']),'#Email', row['Email'])
             tv.set('#{}'.format(row['ID']),'#Gender', row['Gender'])
             tv.set('#{}'.format(row['ID']),'#Comment', row['Comment'])






