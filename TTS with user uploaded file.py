# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 18:46:11 2023

@author: param
"""
import pyttsx3 as tts
from tkinter import*
from tkinter import filedialog
from tkinter import font
import os
def upload():
    filename=filedialog.askopenfilename(filetypes=[('TEXT Documents','*.txt')])
    file=open(filename,'r')
    txt=file.read()
    global text
    text=txt
    global fname
    fname=filename
    msgfrupld.set('UPLOADED!')
    #print(text)
    
import os  
def convert():
    voice=tts.init()
    #text1=text.read()
    voice.say('text')
    voice.save_to_file(text,'dem.mp3')
    path=os.path.abspath('dem.mp3')
    print(path)
    voice.runAndWait()
    msgfrgnrt.set("SUCCESS^^ AUDIO FILE HAS BEEN GENERATED")
    
    #voice.runAndWait()
wid=Tk() 
wid.geometry('500x250')
wid.title('TEXT to SPEECH')
global msgfrupld
global msgfrgnrt
msgfrgnrt=StringVar()
msgfrupld=StringVar()
Label(wid,textvar=msgfrupld,font=('Arial 20 bold'),fg='white',bg='green').place(x=20,y=220)
Label(wid,textvar=msgfrgnrt,font=('Arial 20 bold'),fg='red',bg='white').place(x=120,y=220)

Button(wid,text="UPLOAD",command=upload,font=('Helvetica 10 bold'),fg='white',bg='orange').place(x=20,y=40)
Button(wid,text="CONVERT",command=convert,font=('Helvetica 10 bold'),fg='blue',bg='pink').place(x=120,y=40)
wid.mainloop()
#import os
#os.system('start'+fname+'.mp3')




