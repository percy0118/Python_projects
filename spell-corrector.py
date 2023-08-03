# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 20:20:27 2023

@author: param
"""
from tkinter import*
import textblob as tb

wid=Tk()
wid.geometry('750x500')
wid.resizable(0,0)
wid.title('SPELLING CORRECTOR')
wid.config(bg='#A2FFFB')

def corrector():
    #inword=str(inp.get())
    cor=tb.TextBlob(str(inword.get()))
    global outw
    outword=str(cor.correct())
    outw.set(outword)
    #print(outword)
    #out.insert(END,outword)

"""def clearall():
    inp.delete(0,END)
    outw.delete(0,END)
"""

inword=StringVar() 
outw=StringVar()   
Label(wid,text='Enter the word',font='Times 15 italic',fg='blue').place(x=0,y=10)
inp=Entry(wid,textvariable=inword,width=25).place(x=180,y=10)
Button(wid,command=corrector,text='CORRECT',font='Arial 12 bold').place(x=200,y=70)
Label(wid,text='Corrected word',font='Times 15 italic',fg='green').place(x=0,y=100)
#out=Entry(wid,width=25).place(x=180,y=100)
Label(wid,textvariable=outw,font='Times 15 italic',fg='blue').place(x=210,y=100)
#Button(wid,command=clearall,text='CLEAR',font='Arial 12 bold').place(x=200,y=170)

wid.mainloop()