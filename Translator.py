# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 21:43:07 2023

@author: param
"""
import googletrans as ts
#rom translate import Translator
#mport translate as ts
from tkinter import*
#window
wid=Tk()
wid.title("TRANSLATOR")
wid.geometry('800x500')
wid.resizable(0,0)
wid.config(background='aqua')
#options
inlang=StringVar()
inlang.set('choose here')
inlangchoices=OptionMenu(wid, inlang,'English', 'Hindi','Kannada','French','Spanish','Tamil','German')
inlangchoices.config(bg='blue',fg='white')
inlangchoices['menu'].config(bg='white',fg='green')
inlangchoices.grid(row=2,column=1,ipadx=15,pady=10)


outlang=StringVar()
outlang.set('Choose here')
outlangchoices=OptionMenu(wid, outlang, 'Hindi','Kannada','French','Spanish','Tamil','German')
outlangchoices.config(bg='red',fg='white')
outlangchoices.grid(row=2,column=3,ipadx=15)
#ip and op 
inp=StringVar()
Label(wid,text='Enter the text',fg='black').grid(row=3,column=1)
box1=Entry(wid,textvariable=inp).grid(row=3,column=2,ipadx=15,pady=20)

out=StringVar()
Label(wid,text='The translation is',fg='black').grid(row=3,column=3)
box1=Entry(wid,textvariable=out,font='Arial 20').grid(row=3,column=4)

#Label(wid,)

#translate function
"""def translae():
    trans=Translator(from_lang=inlang.get(),to_lang=outlang.get())
    translation=trans.translate(inp.get())
    out.set(translation)"""
def translate():
    client=ts.Translator()
    response=client.translate(inp,dest='kn')
    global out
    out.set(response)
#button
Button(wid,text='Translate',command=translate,fg='orange',bg='green',font='Arial 15').grid(row=5,column=3)


wid.mainloop()
