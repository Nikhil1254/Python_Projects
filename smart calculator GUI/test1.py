import sys
sys.path.append("/module/")
from module.Mathy import *
from tkinter import *
import speech_recognition as sr

# create object of recognizer


root=Tk()
root.title("Smart calculator")
root.geometry("500x400+500+150")
#root.wm_minsize(width=500,height=500)
root.wm_maxsize(width=500,height=500)
root.config(bg="#F0F3F4")
root.iconbitmap("Smart calculator icon.ico")

####speech

def speech_to_text():
    r = sr.Recognizer()
    query = ''
    with sr.Microphone() as m:
        print("Listening...")
        audio = r.listen(m)
    try:
        query = r.recognize_google(audio, language="eng-in")
        print("You said : " + query)
        e1.configure(text="You said : " + query)
    except:
        e1.configure(text="Cant recognize what you said")

    return query


def fun(event=None):
    text = speech_to_text()
    list1 = text.split()
    if len(list1)==1:
        l4.configure(text=str(eval(text)))
        return
    for word in text.split():
        if word.upper() in operations.keys():
            try:
                l=extract_numbers_from_text(text)
                r=operations[word.upper()](l[0],l[1])
                l4.config(text=str(r))
            except:
                l4.config(text="Something went wrong,Retry!!!")
            finally:
                break
        elif word.upper() in commands.keys():
            l4.config(text=commands[word.upper()]())
            break
    else:
        l4.config(text=sorry())

def exit(event):
    root.destroy()


l5=Label(root,text=responses[0],fg="#A93226")
l5.config(font=("calibri",16,"italic bold"),bg="#F0F3F4")
l5.place(x=160,y=20)

l2=Label(root,text="Ask your question -")
l2.config(font=("calibri",14,"bold"),bg="#F0F3F4")
l2.place(x=10,y=80)

e1=Label(root,text="I'm your mathematical assistant...")
e1.config(font=("calibri",20,"italic bold"),bd=20,bg="#A9DFBF")
e1.place(x=10,y=150,width=480)

l3=Label(root,text="Answer → ")
l3.config(font=("calibri",16,"bold"),bg="#F0F3F4")
l3.place(x=10,y=350)

b1= Button(root,text="Speak",font=("Comic Sans Ms",12,'bold'),command=fun,bd=10,bg="#85C1E9",activeforeground="white",activebackground="#F5B041")
b1.place(x=200,y=250,width=90)

l4=Label(root)
l4.config(font=("airal",18,"italic bold"),fg="#A93226",bg="#F0F3F4")
l4.place(x=140,y=350)

#root.bind("<Return>",fun)


root.bind("<Escape>",exit)

root.bind("<Return>",fun)

root.mainloop()