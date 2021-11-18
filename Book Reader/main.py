from tkinter import *
import threading
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Progressbar
from gtts import gTTS
import time
from langdetect import detect

root = Tk()
root.geometry('500x310+500+200')
root.title('Text2audio converter')
root.config(bg='#D0D3D4')
root.wm_resizable(width=False,height=False)
root.iconbitmap('icon.ico')

def translate():
    file = open(inputfile_var.get(),encoding='UTF-8')  # by default reading mode madhe open hote
    content = file.read()


    progress = Progressbar(root, orient=HORIZONTAL, length=150, mode='indeterminate')
    progress.place(x=180, y=200)
    bar_progress(progress)
    convert_btn.config(state=DISABLED)
    ################### getting output file name
    output_file = [i for i in inputfile_var.get().split('/')]
    output_file = output_file[-1]
    output_file = output_file.split('.')
    output_file = output_file[0] + ".mp3"
    output_file = destfolder_var.get() + "/" + output_file
    #########################################
    try:
        language = detect(content)
        process_Label.config(text='Creating audio...')
        time.sleep(1)
        audio = gTTS(text=content, lang=language,slow=False)
        process_Label.config(text='Audio created.')
        time.sleep(1)
        process_Label.config(text='Saving audio file...')
        audio.save(output_file)
        process_Label.config(text='audio file saved.')
        messagebox.showinfo('Info','Audio file saved successfully')
    except:
        messagebox.showerror('ERROR','Please check your internet connection!')

    progress.destroy()
    process_Label.config(text='')
    convert_btn.config(state=NORMAL)

def bar_progress(progress):
    try:
        progress['value'] = progress['value'] + 15
        root.after(500,bar_progress,progress)
    except:
        return

def translate_thread():
    if destfolder_var.get() != '' and inputfile_var.get() != '':
        thread = threading.Thread(target=translate)
        thread.start()
    else:
        messagebox.showinfo('Info','Enter Input file and Destination folder first!')


def input_dialouge(event):
    filename = filedialog.askopenfilename(filetypes =(('text files','*.txt'),) )
    inputfile_var.set(filename)

def destination_dialouge(event):
    folder_path = filedialog.askdirectory()
    destfolder_var.set(folder_path)

#################################### labels

input_Lable = Label(root,text='Input File :',font=('system',12,'bold'),bg='#D0D3D4')
input_Lable.place(x=10,y=20)

dest_label =  Label(root,text='Dst Folder :',font=('system',12,'bold'),bg='#D0D3D4')
dest_label.place(x=10,y=70)

process_Label = Label(root,text='',justify=CENTER,font=('calibri',10),bg='#D0D3D4')
process_Label.place(x=160,y=175,width=200)

################## about developer
developer_label = Label(root,text='Developer : ',font=('Comic Sans MS',8,'bold'),bg='#D0D3D4')
developer_label.place(x=170,y=255)

developer_name = Label(root,text='NIKHIL PATIL.',font=('airal',9),bg='#D0D3D4')
developer_name.place(x=240,y=257)

contact_Label = Label(root,text='Contact : ',font=('Comic Sans MS',8,'bold'),bg='#D0D3D4')
contact_Label.place(x=155,y=276)

email_Label = Label(root,text='np52622@gmail.com',font=('airal',9),bg='#D0D3D4')
email_Label.place(x=215,y=278)

######################## Entrybox
inputfile_var = StringVar()
inputfile_var.set('')

destfolder_var = StringVar()
destfolder_var.set('')

input_Entry = Entry(root,font=('airal',12),highlightthickness=2,highlightcolor='#F5B041',relief='sunken',textvariable=inputfile_var)
input_Entry.place(x=140,y=23,width=300)

dest_Entry = Entry(root,font=('airal',12),highlightthickness=2,highlightcolor='#F5B041',relief='sunken',textvariable=destfolder_var)
dest_Entry.place(x=140,y=70,width=300)
####################### buttons
convert_btn = Button(root,text='Convert',font=('Comic Sans MS',12,'bold'),relief='raised',bd=3,command=translate_thread)
convert_btn.place(x=220,y=130)

input_Entry.bind('<Button-1>',input_dialouge)
dest_Entry.bind('<Button-1>',destination_dialouge)

root.mainloop()