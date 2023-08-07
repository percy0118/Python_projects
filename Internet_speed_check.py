# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 22:36:34 2023

@author: param
"""
from tkinter import *
import pyspeedtest
win=Tk()
win.title('Internet Speed Checker')
win.configure(bg='yellow')
win.geometry('750x500')
win.resizable(0,0)
def check():
    internet=pyspeedtest.SpeedTest(link.get())
    ping_speed.set(internet.ping())
    down_speed.set(internet.download())

ping_speed=StringVar()
down_speed=StringVar() 

link=StringVar()    

Label(win,text="Enter the WEB URL",bg='yellow',fg='red',font='Times 18 bold').place(x=10,y=10)
Entry(win,textvariable=link,fg='blue',font='arial 15').place(x=300,y=10)
Button(win,text='CHECK the SPEED',command=check,bg='black',fg='orange',font='arial 10 bold').place(x=310,y=50)
Label(win,text='ping',fg='red',bg='yellow',font='arial 15 bold').place(x=130,y=120)
Label(win,text='download',fg='green',bg='yellow',font='arial 15 bold').place(x=130,y=180)
Label(win,textvariable=ping_speed,fg='red',bg='aqua',font='arial 15 italic').place(x=330,y=120)
Label(win,textvariable=down_speed,fg='green',bg='aqua',font='arial 15 italic').place(x=330,y=180)
win.mainloop()



