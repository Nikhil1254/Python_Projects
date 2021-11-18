from tkinter import *
import random
from pytube import YouTube



root = Tk()
root.title("Youtube Downloader")
root.geometry("780x500+300+100")
root.iconbitmap('download.ico')
root.config(bg="#D7DBDD")
root.resizable(False,False) #width,height

def colorchange():
    colors = ['#CD6155','#9B59B6','#2980B9','#1ABC9C','#52BE80','#F1C40F','#E59866']
    random.shuffle(colors)
    introLabel.config(fg=colors[0])
    introLabel.after(1000,colorchange)

##################################################### Entry Label
url = Entry(root,width=43,font=('calibri',15),bd=3,relief='groove')
url.place(x=20,y=140,height=40)

###################################### scrollbar
scrollbar = Scrollbar(root)
scrollbar.place(x=430,y=232,height=202)

################################### Listbox

listbox = Listbox(root,yscrollcommand=scrollbar.set,width=50,height=10,font=('calibri',12,'bold'),relief='solid'
                  ,bd=2,highlightcolor='#ABEBC6',highlightbackground='#AED6F1',
                  highlightthickness=2) # highlightcolor mhanje list item var click kelyavar tyacha color kay hoil
'''
    highlightcolor mhanje listbox var click kelyavar border chya ajubajula color yeto
    highlightbackground mhanje click karaychya adhi kay color asel border chya ajubajula
'''
listbox.place(x=20,y=230)

listbox.insert(1,'Nikhil')
print(listbox.curselection())

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
enterLink = Button(root,text='← Enter link',font=('Comic Sans MS',12,'bold'),activebackground="#F5CBA7",bd=4)
enterLink.place(x=540,y=138,width=120)

downloadbtn = Button(root,text="DOWNLOAD",font=('calibri',14,'italic bold'),bd=4,activebackground="#F5CBA7")
downloadbtn.place(x=540,y=390,width=150)

colorchange()

root.mainloop()