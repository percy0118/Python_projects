import moviepy.editor as mp
from tkinter import*
from tkinter import filedialog

def upload():
    fname=filedialog.askopenfilename(filetypes=[('Mp4 files','*.mp4'),('WMV files','*.wmv'),('ogg files','*.ogg')])
    msgfrupld.set("UPLOADED!"+fname)
    global file
    file=fname
def convert():
    vclip=mp.VideoFileClip(file)
    vclip.audio.write_audiofile('filename.mp3')
    msgfrcnvrt.set("converted^^")
global msgfrupld
global msgfrcnvrt
win=Tk()
win.geometry("800x500")
win.title('Video to Audio')
msgfrcnvrt=StringVar()
msgfrupld=StringVar()
Label(master=win,text='DONE',textvar=msgfrupld,font='Arial 12 bold',bg='red',fg='white').place(x=200,y=100)
Button(text="UPLOAD",fg='black',bg='green',command=upload).place(x=10,y=20)
Label(win,text='DONE',textvar=msgfrcnvrt,font='Arial 12 bold',bg='red',fg='white').place(x=250,y=120)
Button(text="CONVERT",fg='white',bg='black',command=convert).place(x=180,y=20)

win.mainloop()  
   
    
