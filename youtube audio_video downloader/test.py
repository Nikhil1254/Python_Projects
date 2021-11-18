from tkinter import *
import random
import pytube
from tkinter import messagebox
from tkinter import filedialog
import threading





root = Tk()
root.title("Youtube Downloader")
root.geometry("780x500+300+100")
root.iconbitmap('download.ico')
root.config(bg="#D7DBDD")
root.resizable(False,False) #width,height


def downloadThread():
    downloadbtn.config(state=DISABLED)
    downloadThread = threading.Thread(target=download)
    downloadThread.start() # download() la call janar pn te seperate thread madhe chalnar kam

def showinfo():
    if youtube_url.get() == '':
        messagebox.showinfo('Information','Enter URL first!')
        return

    try:
        yt = pytube.YouTube(youtube_url.get())
        list1 =  yt.streams.filter(file_extension='mp4',type='audio')
        i=0
        for videos in list1:
            listbox.insert(i,videos)
            i+=1
    except:
        messagebox.showinfo('Info','Check Internet Connection and URL!')






    #messagebox.showinfo('Info','Something went wrong,check URL or internet connetion!')

def download():
    ff = filedialog.askdirectory()
    try:
        index = listbox.curselection()[0]
        if len(str(index))==0:
            messagebox.showinfo('Info','Select file to download!')
            return

        yt = pytube.YouTube(youtube_url.get())
        list1 = yt.streams.filter(file_extension='mp4',type='audio')
        list1[index].download(ff+'/')
        messagebox.showinfo('Info','DOWNLOAD Completed.')

    except:
        messagebox.showinfo('Info','Check Internet Connection!')
    downloadbtn.config(state=NORMAL, text='DOWNLOAD')

def colorchange():
    colors = ['#CD6155','#9B59B6','#2980B9','#1ABC9C','#52BE80','#F1C40F','#E59866']
    random.shuffle(colors)
    introLabel.config(fg=colors[0])
    introLabel.after(1000,colorchange)

##################################################### Entry Label
youtube_url = StringVar()
youtube_url.set('')

url = Entry(root,width=43,font=('calibri',15),bd=3,relief='groove',textvariable=youtube_url)
url.place(x=20,y=140,height=40)

###################################### scrollbar

################################### Listbox

listbox = Listbox(root,width=50,height=10,font=('calibri',12,'bold'),relief='solid'
                  ,bd=2,highlightcolor='#ABEBC6',highlightbackground='#AED6F1',
                  highlightthickness=2) # highlightcolor mhanje list item var click kelyavar tyacha color kay hoil
'''
    highlightcolor mhanje listbox var click kelyavar border chya ajubajula color yeto
    highlightbackground mhanje click karaychya adhi kay color asel border chya ajubajula
'''
listbox.place(x=20,y=230,width=420,height=180)

#--------------------------------------------------- scroll bat to listbox
x_scroll = Scrollbar(listbox,orient=HORIZONTAL)
y_scroll = Scrollbar(listbox,orient=VERTICAL)


listbox.config(yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)
x_scroll.config(command=listbox.xview)
y_scroll.config(command=listbox.yview)
x_scroll.pack(side=BOTTOM,fill=X)
y_scroll.pack(side=RIGHT,fill=Y)

####################################### Labels

introLabel = Label(root,text="Welcome To Youtube Audio Video Downloader",width=50,relief='groove'
                   ,bd=4,font=('Comic Sans MS',19,'bold'))
introLabel.place(x=12,y=20)

DownloadingSize = Label(root,text="Total Size : ",font=('airal',14,'bold'),
                        bg="#D7DBDD")
DownloadingSize.place(x=450,y=240)

DownloadingLabel = Label(root,text="Received Size : ",font=('airal',14,'bold'),
                        bg="#D7DBDD")
DownloadingLabel.place(x=450,y=290)

DownloadingTime = Label(root,text="Time Left : ",font=('airal',14,'bold'),
                        bg="#D7DBDD")
DownloadingTime.place(x=450,y=340)

DownloadingSizeLabelResult = Label(root,text="",font=('airal',14,'bold'),
                        bg="#D7DBDD")
DownloadingSizeLabelResult.place(x=600,y=240)
#################################################### ProgressBar

################################# Buttons
enterLink = Button(root,text='← Enter link',font=('Comic Sans MS',12,'bold'),activebackground="#F5CBA7",bd=4,command=showinfo)
enterLink.place(x=540,y=138,width=120)


downloadbtn = Button(root,text="DOWNLOAD",font=('calibri',14,'italic bold'),bd=4,activebackground="#F5CBA7",command=downloadThread)
downloadbtn.place(x=540,y=390,width=150)


colorchange()

root.mainloop()