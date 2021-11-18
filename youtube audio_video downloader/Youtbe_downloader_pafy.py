import pafy
from tkinter import filedialog
from tkinter import *

url = input('Enter Video URL : ')

try:
    obj = pafy.new(url=url)
except:
    print('Enter valid URL and check Internet connection!!!')
    exit(0)

streams = []
streams.append(obj.getbest())
streams.append(obj.getbestaudio())

print('Title : {}'.format(obj.title))
print('Duration : {}'.format(obj.duration))
i=0
while i<len(streams):
    filesize = streams[i].get_filesize()/(1024*1024)
    if i!=len(streams)-1:
        print(str(i+1),streams[i].mediatype,streams[i].resolution,'  - {}'.format(round(filesize,2))+' Mb')
    else:
        print(str(i+1) ,streams[i].mediatype,streams[i].bitrate , '  - {}'.format(round(filesize, 2)) + ' Mb')
    i+=1

index = int(input("\nEnter File number to download  "))
##################### filedialogue
downloadStream = streams[index-1]
root = Tk()
root.geometry('100x100+100+100')
root.title('Select path')
path = filedialog.askdirectory()
root.destroy()

print('DOWNLOADING....')
downloadStream.download(quiet=False,filepath=path+'/')
input('Download Complete.')