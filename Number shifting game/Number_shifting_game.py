from tkinter import *
from tkinter import messagebox
import random
import pygame

pygame.init() # to initialize pygame module
import pygame.mixer

pygame.mixer.music.load("background.mp3")
pygame.mixer.music.play(-1) # -1 means infinitly it will run

def close(event):
    screen.destroy()

def reset():
    global count,numbers,labels
    count=0
    random.shuffle(numbers)
    index=0
    try:
        for obj in labels:
            obj.config(text=numbers[index])
            index+=1
    except:
        pass
    l16.config(text="")
    Labelinfo.config(text="Moves : {}".format(count))



def check(event):

    global labels,numbers,count
    num=1
    for obj in [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15]:
        if obj['text']!= ""+str(num):
            return
        num+=1

    else:
        if messagebox.askyesno("Play again","Do you want to Play Again?"):
            reset()



def moveR(event):
    global labels,count
    for obj in labels:
        if obj['text']=="":
            break
    index=labels.index(obj)
    if index in [3,7,11,15]:
        return
    count+=1
    Labelinfo.config(text="Moves : {}".format(count))
    labels[index].config(text=labels[index+1]['text'])
    labels[index+1].config(text="")

def moveL(event):
    global labels,count
    for obj in labels:
        if obj['text'] == "":
            break
    index = labels.index(obj)
    if index in [0,4,8,12]:
        return
    count+=1
    Labelinfo.config(text="Moves : {}".format(count))
    labels[index].config(text=labels[index - 1]['text'])
    labels[index - 1].config(text="")

def moveU(event):
    global labels,count
    for obj in labels:
        if obj['text'] == "":
            break
    index = labels.index(obj)
    if index in [0,1,2,3]:
        return
    count+=1
    Labelinfo.config(text="Moves : {}".format(count))
    labels[index].config(text=labels[index - 4]['text'])
    labels[index - 4].config(text="")

def moveD(event):
    global labels,count
    for obj in labels:
        if obj['text'] == "":
            break
    index = labels.index(obj)
    if index in [12,13,14,15]:
        return
    count+=1
    Labelinfo.config(text="Moves : {}".format(count))
    labels[index].config(text=labels[index + 4]['text'])
    labels[index + 4].config(text="")


screen=Tk()
screen.title("Number Shifting Game")
screen.geometry("363x453+450+150")
screen.wm_minsize(width=363,height=453)
screen.wm_maxsize(width=363,height=453)
screen.config(bg="#ABEBC6")
screen.iconbitmap("icon.ico")

######################################################################Labels
numbers=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
count=0
random.shuffle(numbers)

##row 0
l1=Label(text=numbers[0],borderwidth=7,relief="groove",font=("airal",20,"italic bold"),padx=30,pady=30,bg="#FA8072",width=1,height=1)
l1.grid(row=0,column=0)

l2=Label(text=numbers[1],borderwidth=7,relief="groove",font=("airal",20,"italic bold"),padx=30,pady=30,bg="#FA8072",width=1,height=1)
l2.grid(row=0,column=1)

l3=Label(text=numbers[2],borderwidth=7,relief="groove",font=("airal",20,"italic bold"),padx=30,pady=30,bg="#FA8072",width=1,height=1)
l3.grid(row=0,column=2)

l4=Label(text=numbers[3],borderwidth=7,relief="groove",font=("airal",20,"italic bold"),padx=30,pady=30,bg="#FA8072",width=1,height=1)
l4.grid(row=0,column=3)

##row 1
l5=Label(text=numbers[4],borderwidth=7,relief="groove",font=("airal",20,"italic bold"),padx=30,pady=30,bg="#FA8072",width=1,height=1)
l5.grid(row=1,column=0)

l6=Label(text=numbers[5],borderwidth=7,relief="groove",font=("airal",20,"italic bold"),padx=30,pady=30,bg="#FA8072",width=1,height=1)
l6.grid(row=1,column=1)

l7=Label(text=numbers[6],borderwidth=7,relief="groove",font=("airal",20,"italic bold"),padx=30,pady=30,bg="#FA8072",width=1,height=1)
l7.grid(row=1,column=2)

l8=Label(text=numbers[7],borderwidth=7,relief="groove",font=("airal",20,"italic bold"),padx=30,pady=30,bg="#FA8072",width=1,height=1)
l8.grid(row=1,column=3)

##row 2
l9=Label(text=numbers[8],borderwidth=7,relief="groove",font=("airal",20,"italic bold"),padx=30,pady=30,bg="#FA8072",width=1,height=1)
l9.grid(row=2,column=0)

l10=Label(text=numbers[9],borderwidth=7,relief="groove",font=("airal",20,"italic bold"),padx=30,pady=30,bg="#FA8072",width=1,height=1)
l10.grid(row=2,column=1)

l11=Label(text=numbers[10],borderwidth=7,relief="groove",font=("airal",20,"italic bold"),padx=30,pady=30,bg="#FA8072",width=1,height=1)
l11.grid(row=2,column=2)

l12=Label(text=numbers[11],borderwidth=7,relief="groove",font=("airal",20,"italic bold"),padx=30,pady=30,bg="#FA8072",width=1,height=1)
l12.grid(row=2,column=3)

##row 3
l13=Label(text=numbers[12],borderwidth=7,relief="groove",font=("airal",20,"italic bold"),padx=30,pady=30,bg="#FA8072",width=1,height=1)
l13.grid(row=3,column=0)

l14=Label(text=numbers[13],borderwidth=7,relief="groove",font=("airal",20,"italic bold"),padx=30,pady=30,bg="#FA8072",width=1,height=1)
l14.grid(row=3,column=1)

l15=Label(text=numbers[14],borderwidth=7,relief="groove",font=("airal",20,"italic bold"),padx=30,pady=30,bg="#FA8072",width=1,height=1)
l15.grid(row=3,column=2)

l16=Label(text="",borderwidth=7,relief="groove",font=("airal",20,"italic bold"),padx=30,pady=30,bg="#FA8072",width=1,height=1)
l16.grid(row=3,column=3)

Labelinfo=Label(text="Moves : {}".format(count),font=("airal",15,"italic bold"),bg="#ABEBC6")
Labelinfo.grid(row=4,column=0,columnspan=4)

#######################################################variables

labels=[l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16]

############################################################bind
screen.bind("<Escape>",close)
screen.bind("<Left>",moveR)
screen.bind("<Right>",moveL)
screen.bind("<Up>",moveD)
screen.bind("<Down>",moveU)

screen.bind("<KeyRelease>",check)

screen.mainloop()