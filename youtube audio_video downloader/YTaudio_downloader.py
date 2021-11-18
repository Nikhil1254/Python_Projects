from tkinter import *
import random
import pafy
from tkinter import messagebox
from tkinter import filedialog
import threading

root = Tk()
root.title('Youtube Audio Downloader')
root.geometry('500x460+500+200')
root.iconbitmap('youtube.ico')

def audioInfo():
   try:
      linkbtn.config(state=DISABLED)
      url = urlVariable.get()
      if url == ' ':
         linkbtn.config(state=NORMAL)
         return
      obj = pafy.new(url)
      audioStream = obj.getbestaudio()
      filesize = round(audioStream.get_filesize()/(1024*1024),2)

      audioTitle.config(text='Title : '+str(obj.title))
      audioSize.config(text='File size : '+str(filesize)+' Mb')
      audioBitrate.config(text='Bitrate : '+str(audioStream.bitrate))
      audioDuration.config(text='Duration : '+str(obj.duration))
   except:
     messagebox.showerror('Network error','Please check URL and Internet connection!')

   linkbtn.config(state=NORMAL)

def progress(total,recvd,ratio,rate,eta):
   downloadbtn.config(text=' {}%'.format(round(ratio*100)))
   internetSpeed.config(text='{} KB/s'.format(round(rate,2)))
   #print("downloaded : {}".format(round(ratio*100)),'speed : {}'.format(round(rate,2)),'ETA : {} min'.format(eta/60))


def downloadThread():
    downloadThread = threading.Thread(target=download)
    downloadThread.start()

def download():
   downloadbtn.config(state=DISABLED)
   url = urlVariable.get()
   if url == '':
      messagebox.showinfo('Information','Enter URL first!')
      return

   try:
      obj = pafy.new(url=url)
      audiostream = obj.getbestaudio()

      path = filedialog.askdirectory()
      audiostream.download(filepath=path+'/',callback=progress)
      messagebox.showinfo('Info','Download Completed.')


   except:
      messagebox.showerror('Something Went Wrong','Check URL and Internet Connection!!!')

   downloadbtn.config(state=NORMAL, text='Download')


def colorchange():
   colors = ['#CD6155','#9B59B6','#2980B9','#1ABC9C','#52BE80','#F1C40F','#E59866']
   random.shuffle(colors)
   welcomeLabel.config(fg=colors[0])
   welcomeLabel.after(1000,colorchange)

################################# labels

welcomeLabel = Label(root,text='Welcome To Youtube Audio Downloader',font=('Comic Sans MS',16,'bold'),bd=4,relief='solid',justify=CENTER)
welcomeLabel.place(x=35,y=20,width=430)

############################### Entry label

urlVariable = StringVar()
urlVariable.set(' ')

url = Entry(root,font=('calibri',14),bd=4,relief='groove',border=3,textvariable=urlVariable)
url.focus()
url.place(x=20,y=100,width=330)

audioTitle = Label(root,text='Title :',font=('Comic Sans MS',13,'bold'))
audioTitle.place(x=10,y=250)

audioDuration = Label(root,text='Duration :',font=('Comic Sans MS',13,'bold'))
audioDuration.place(x=10,y=290)

audioSize = Label(root,text='File size :',font=('Comic Sans MS',13,'bold'))
audioSize.place(x=10,y=330)

audioBitrate = Label(root,text='Bitrate :',font=('Comic Sans MS',13,'bold'))
audioBitrate.place(x=10,y=370)

internetSpeed = Label(root,text='',font=('airal',10,'bold'))
internetSpeed.place(x=235,y=220)

publisher = Label(root,text='Publisher : Nikhil Patil',font=('calibri',11))
publisher.place(x=195,y=410)

support =  Label(root,text='Contact : np52622@gmail.com',font=('calibri',11))
support.place(x=170,y=430)

############################# buttons

linkbtn = Button(root,text="← Enter Link",font=('airal',13),bd=5,relief="raised",bg="#85C1E9",activebackground="#F5B041",activeforeground="white",command=audioInfo)
linkbtn.place(x=370,y=96)

downloadbtn = Button(root,text="Download",justify=CENTER,font=('Comic Sans MS',14),bd=5,relief='raised',bg="#D2B4DE",activebackground="#F5B041",activeforeground="white",command=downloadThread)
downloadbtn.place(x=200,y=160,width=120)



colorchange()

root.mainloop()