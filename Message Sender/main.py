import requests
import json
from tkinter import *
from tkinter import messagebox

def send_sms(number,message):
    url = 'https://www.fast2sms.com/dev/bulk'
    params = {
        'authorization':'PoBeUF6uGCypawdZ1q8Di2lAr3EtfYgm7hNSMkO4XzQb05jWJ9Ym2DRp9zVS3sCag1n8LGKe64O5QAIZ',
        'sender_id':'FSTSMS','message':message,'language':'english','route':'p',
        'numbers':number
    }
    response = requests.get(url,params=params)
    dic = response.json()
    return dic.get('return')

# send_sms('7972490147','Hello Nikhil')


def btn_click():
    num = textNumber.get()
    msg = textMsg.get('1.0',END) # start to end purn text havay
    r = send_sms(num,msg)
    if r:
        messagebox.showinfo('Send Success','Successfully Sent')
    else:
        messagebox.showerror('Error','Something Went Wrong!')


########### Create GUI
root = Tk()
root.title('Message Sender')
root.geometry('400x550')

textNumber = Entry(root,font=('Comic Sans MS',22,'bold'))
textNumber.pack(fill=X,pady=20,padx=10)

textMsg = Text(root)
textMsg.pack(fill=X,padx=10)

sendBtn = Button(root,text='SEND SMS',command=btn_click)
sendBtn.pack(pady=15)


root.mainloop()