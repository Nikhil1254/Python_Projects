from tkinter import *
from random import shuffle
from tkinter import filedialog
import cv2
from tkinter import messagebox
import pyautogui
import numpy as np
import threading

root = Tk()
root.geometry('500x350+500+200')
root.title('Screen Recorder')
root.config(bg='#73C6B6')
root.wm_resizable(width=False,height=False)
root.iconbitmap('record.ico')

colors = ['#CD6155','#AF7AC5','#F7DC6F','#E59866']
global flag,exit,pause
flag = 0
exit = False
pause = False

def color_change():
    global colors
    shuffle(colors)
    welcome_label.config(fg=colors[0])
    welcome_label.after(1000,color_change)

def get_file_path(event):
    file_path_var.set(filedialog.askdirectory())
    print(file_path_var.get())

def record_thread():
    global flag
    if flag==0 and rec_btn['text']=='► START':
        thread = threading.Thread(target=record)
        thread.start()

    if flag==1 and rec_btn['text']=='■ STOP':
        flag = 0
        rec_btn.config(text='► START',bg='#A9CCE3',fg='black')
        rec_label.config(text='')


def record():
    global flag,exit,pause,check
    flag=1
    pause = False
    if file_name_var.get() == '' or file_path_var.get() == '':
        messagebox.showinfo('Info','Enter file name and its path first.')
        flag=0
        return

    rec_btn.config(text='■ STOP',bg='#F5B041',fg='white')
    rec_label.config(text='Recording...')
    width,height = pyautogui.size()
    file = file_path_var.get() + '/' + file_name_var.get()+'.avi'

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(file,fourcc,10,(width,height))
    record = cv2.VideoCapture(0)
    record.set(cv2.CAP_PROP_FRAME_WIDTH,426)
    record.set(cv2.CAP_PROP_FRAME_HEIGHT,240)

    while flag:
        if not pause:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

            if check.get() == 1:
                ret,video = record.read()
                if ret:
                    video = cv2.resize(video,(426,240))
                    frame[0:240,width-426:] = video


            cv2.circle(frame,pyautogui.position(),8,(182, 89, 155 ),-1,lineType=cv2.LINE_AA)
            out.write(frame)

    messagebox.showinfo('Info','Video is saved at {}'.format(file))
    if check.get() == 1 or check.get() == 0:
        check.set(2)
        onbtn.config(bg='#A9CCE3',fg='black')
        offbtn.config(bg='#A9CCE3',fg='black')

    out.release()
    record.release()
    if exit==True:
        root.destroy()

def on_closing():
    global flag,exit

    flag = 0
    exit = True

    if exit==True and rec_btn['text']=='► START':
        root.destroy()

def pause_rec(event):
    global pause
    if rec_label['text']=='Recording...':
        rec_label.config(text='Paused...')
        pause = True

def resume_rec(event):
    global pause
    if rec_label['text']=='Paused...':
        pause = False
        rec_label.config(text='Recording...')

def radio_color():
    if check.get() == 1:
        onbtn.config(fg='white')
        offbtn.config(fg='black')
    elif check.get() == 0:
        onbtn.config(fg='black')
        offbtn.config(fg='white')

def camera_thread(event):
    if threading.active_count() != 2 :
        thread = threading.Thread(target=adjust_camera)
        thread.start()
    else:
        messagebox.showinfo('Info',"Already video is capturing can't show adjustment screen!")

def adjust_camera():
    camera = cv2.VideoCapture(0)

    while camera.isOpened():
        ret,frame = camera.read()

        cv2.imshow('Adjust Camera',frame)
        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows()
            break

    camera.release()


#################### Lales
welcome_label = Label(root,text='Screen Recorder',bg='#73C6B6',font=('Comic Sans MS',15,'bold','underline'))
welcome_label.place(x=170,y=10)

file_name_label = Label(root,text='File name -',font=('calibri',13),bg='#73C6B6')
file_name_label.place(x=10,y=80)

file_path_label = Label(root,text='File path -',font=('calibri',13),bg='#73C6B6')
file_path_label.place(x=10,y=130)

rec_label =Label(root,text='',bg='#73C6B6',anchor=CENTER,font=('airal',9,'bold'))
rec_label.place(x=200,y=305,width=150)


game_mode_label = Label(root,text='Gaming Mode -',bg='#73C6B6',anchor=CENTER,font=('calibri',13))
game_mode_label.place(x=10,y=190)

###################### Entrybox
file_name_var = StringVar()
file_path_var = StringVar()

file_name_entry = Entry(root,font=('calibri',10,'bold'),highlightthickness=2,highlightcolor = "#F5B041",highlightbackground='#2980B9',textvariable=file_name_var)
file_name_entry.place(x=140,y=82,width=280,height=25)

file_path_entry = Entry(root,font=('calibri',10,'bold'),highlightthickness=2,highlightcolor = "#F5B041",highlightbackground='#2980B9',textvariable=file_path_var)
file_path_entry.place(x=140,y=133,width=280,height=25)

###################### Button
rec_btn = Button(root,text='► START',font=('Comic Sans MS',12,'bold'),bd=3,bg='#A9CCE3',command=record_thread,cursor='hand2')
rec_btn.place(x=200,y=250,width=150)
################### Checkbox

check = IntVar()
check.set(2)

onbtn = Radiobutton(root,text='ON',font=('Comic Sans MS',12,'bold'),variable=check,value=1,bg='#A9CCE3',indicator=0,bd=3,cursor='hand2',command=radio_color,selectcolor='#F5B041')
offbtn = Radiobutton(root,text='OFF',font=('Comic Sans MS',12,'bold'),variable=check,value=0,bg='#A9CCE3',indicator=0,bd=3,cursor='hand2',command=radio_color,selectcolor='#F5B041')
onbtn.place(x=180,y=190,width=100)
offbtn.place(x=282,y=190,width=100)



color_change()
file_path_entry.bind('<Button-1>',get_file_path)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.bind('<Control-Key-p>',pause_rec)
root.bind('<Control-Key-r>',resume_rec)
root.bind('<Control-Key-c>',camera_thread)
root.mainloop()