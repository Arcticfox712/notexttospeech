import tkinter as tk
import gtts
from tkinter import messagebox
import os

screen=tk.Tk()
screen.title("tts convertr")
screen.configure(bg= "#C2A1D1")
screen.geometry("400x400")

a= ("Arial", 20)
b= ("Arial", 15)

def ntts():
    text1= e1.get()
    audiofile=gtts.gTTS(text1, lang= "fr", slow= False)
    audiofile.save("Def_NOT_tts.mp3")
    messagebox.showinfo("yipe", "file saved succesfully!!!")



l1=tk.Label(text= "texttospeech convertr", width= 20, height= 2, bg="#C2A1D1", fg= "white", font= a)
l1.place(x=2, y= 30)


l2=tk.Label(text= "entr text belou::", width= 15, height= 1, bg="#C2A1D1", fg= "white", font= b)
l2.place(x=10, y= 100)

e1= tk.Entry(width= 50)
e1.place(x= 10, y=150)

b1=tk.Button(text= "convrt", width= 15, height= 1, bg="#F2F494", fg= "white", font= b, command= ntts)
b1.place(x=10, y= 200)





screen.mainloop()