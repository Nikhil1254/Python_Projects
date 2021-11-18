words=['breathe', 'bridge', 'bright', 'bring', 'brother', 'brown','central', 'century', 'certain','dance', 'dangerous', 'dark', 'daughter',
       'example','except', 'excited', 'exercise', 'expect', 'expensive', 'freedom', 'freeze', 'fresh','friend','friendly','model', 'modern', 'moment', 'money','monkey',
       'neck', 'need', 'needle', 'neighbour','prison', 'private', 'prize', 'probably', 'problem','produce', 'promise',
       'ugly', 'uncle', 'under', 'understand','vegetable', 'very', 'village', 'voice', 'visit','street', 'strong', 'structure', 'student', 'study', 'stupid', 'subject', 'substance', 'successful']


def labelslider():   #te varti nav firat rahta tya sathi
    global count,sliderwords
    text="Welcome to Typing Speed Game"
    if (count>=len(text)):
        count=0
        sliderwords=""
    sliderwords+= text[count]
    count+=1
    fontLabel.config(text=sliderwords)
    fontLabel.after(150,labelslider)
    '''
        150milisec ne labelslider() call honar parat parat,ani 
        tyala kontyahi component sathi call karu shakto apan eg. root.after(150,labelslider)
        asa pn karu shakto apan.
    '''

def time():
    global timeleft
    global score,miss
    if timeleft>11:
        pass
    else:
        timeLabelCount.config(fg="red")
    if timeleft >0:
        timeleft-=1
        timeLabelCount.config(text=timeleft)
        timeLabelCount.after(1000,time) #dar 1 sec ne hech function call honar ani value ek ek ne kami honar.
    else:
        gamePlayDetailLabel.config(text="hit={} miss={} Total Score={}".format(score,miss,score-miss))
        rr = messagebox.askretrycancel("Notification","For play again hit Retry button")
        if rr==True:         # mhanje retry hit kelay
            score=0
            timeleft=60
            miss=0
            timeLabelCount.config(text=timeleft)
            wordLabel.config(text=words[0])
            scoreLabelCount.config(text=score)
            timeLabelCount.config(fg="blue")

def startGame(event):         # to accept event object 'event' getlay
    global score,miss,timeleft
    if timeleft==60:      # karan ethun aplyala ekdach call dyychay nahitar time fast kami honar, karan Enter mule time() pn parat parat call honarc
        time()
    gamePlayDetailLabel.config(text="")  # first time enter press kelyavar te saglyat khali lihlel gayab honar.
    if(wordEntry.get()== wordLabel['text']):
        score+=1
        scoreLabelCount.config(text=score)
    else:
        miss+=1
    random.shuffle(words)  # apali list ji ahe words chya rearange karto jitkya veles call karu tevdya veles.
    wordLabel.config(text=words[0])
    wordEntry.delete(0,END)        # Entry box madhe je adhi type kel hot te delete houn janar purn i.e.0 to END

from tkinter import *
import random
from tkinter import messagebox
############################################root methods
root=Tk()
root.title("Typing Speed Game")
root.geometry("800x600+400+100")
root.config(bg="#29AB87")
#root.iconbitmap("filename.ico")  # to set icon only ico format allowed

###########################################variables

score = 0
timeleft = 60
count = 0            # varti nav firat tya sathi lagtoy.
sliderwords = ""     # varti nav firtay tya sathi lagtoy.
miss=0               # kiti chukiche words enter kele tyacha count thevnya sathi.
####################################################################################Label methods

fontLabel=Label(root,text="")
fontLabel.config(font=("airal",25,"italic bold"),bg="#29AB87",fg="#FF7F50",width=40)
fontLabel.place(x=20,y=10)

labelslider()   # ethe first time call kel nantar te automatically call hot rahnar.

random.shuffle(words)  #first time game chalu hoil tevha pn pratyek veles different word milava mhanun.
wordLabel=Label(root,text=words[0])
wordLabel.config(font=("airal",40,"italic bold"),bg="#29AB87")
wordLabel.place(x=330,y=200)

scoreLabel=Label(root,text="Your Score :",font=("airal",25,"italic bold"),bg="#29AB87")
scoreLabel.place(x=10,y=100)

scoreLabelCount=Label(root,text=score,font=("airal",25,"italic bold"),bg="#29AB87",fg="blue")
scoreLabelCount.place(x=80,y=180)

timerLabel=Label(root,text="Time Left :",font=("airal",25,"italic bold"),bg="#29AB87")
timerLabel.place(x=600,y=100)

timeLabelCount=Label(root,text=timeleft,font=("airal",25,"italic bold"),bg="#29AB87",fg="blue")
timeLabelCount.place(x=680,y=180)


gamePlayDetailLabel=Label(root,text="Type word and Hit Enter button",font=("airal",30,"italic bold"),bg="#29AB87")
gamePlayDetailLabel.place(x=120,y=450)
#######################################################################################################Entry method

wordEntry=Entry(root)
wordEntry.config(font=("airal",25,"italic bold"),bd=10,justify="center")   #justify='center' mule typing center pasna honar entrybox madhe
wordEntry.place(x=250,y=300)
wordEntry.focus_set()   # aplyala tyavar(textbox var) click karaychi garaj nahi,alredy click asnar.

####################################################
root.bind("<Return>",startGame)   # Return represent karta 'Enter' la i.e.Enter key press event ahe ha,Enter press kel ki startgame() call honar
root.mainloop()