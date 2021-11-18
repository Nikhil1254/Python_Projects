from tkinter import *
from time import sleep
from math import sin,cos,tan,sqrt,log
screen=Tk()
screen.title("My calculator")
screen.geometry("340x498")
screen.wm_minsize(width=340,height=502)
screen.wm_maxsize(width=450,height=502)
screen.iconbitmap("cal_icon.ico")  # set window icon

################################################################functions

def escape(event):
    screen.destroy()

def rightkey(event):
    screen.geometry("450x500")

def leftkey(event=None):
    screen.geometry("340x498")

def press(event):
    global l,l1,operator
    ch=event.char
    if ch in ['s','i','n','c','o','t','a','q','r','l','g',"(",")",","]:       # sin,cos,tan type pn karta yav mhanun
        operator+=ch
        return

    if ch==".":                         # dot button sathi
        operator+=ch
        btndot.config(bg="#B3B6B7", fg="white")
        entry1.delete(0,END)
        entry1.insert(0,operator)
        return

    if ch in l1:
        operator+=ch
        if ch == '+':
            count = 10
        elif ch == '-':
            count = 11
        elif ch == '*':
            count = 12
        elif ch == "/":
            count = 13
        else:
            count = int(ch)

        l[count].config(bg="#B3B6B7", fg="white")

    else:
        entry1.delete(0,END)                         # delete kela content
        entry1.insert(0,operator)               # ani lagech just adhichach content dakhavla tyamule asa feel ala ki te dusre vale i.e characters vegere press ch nahi hote

def release(event):
    global l, l1
    ch=event.char
    if event.char == ".":
        btndot.config(bg="#EAEDED", fg="#F39C12")
        return
    if ch in l1:
        if ch == '+':
            count = 10
        elif ch == '-':
            count = 11
        elif ch == '*':
            count = 12
        elif ch == "/":
            count = 13
        elif ch == "\r":
            count = 14
        else:
            count = int(ch)

        if count in [10,11,12,13]:
            l[count].config(bg="#EAEDED", fg="#F39C12")
            return
        if count==14:
            l[count].config(bg="#F39C12",fg="white")
            return
        l[count].config(bg="#EAEDED", fg="black")

    if event.char==".":
        btndot.config(bg="#EAEDED", fg="#F39C12")


def backspace(event):
    global operator
    if operator=="":
        return
    operator=operator[:len(operator)-1]
    entry1.delete(0, END)
    entry1.insert(0, operator)


def equal(event=None):                             # 'enter' press kel kivva 'btnequal' dabal tar result calculation sathi
    global operator
    try:
        result = eval(entry1.get())
        entry1.delete(0,END)
        entry1.insert(0,round(result,4))
        operator=str(round(result,2))    # round(value,precision) i.e. decimal nantar kiti digit dakhvaychet tya sathi

        if event!=None:
            btnequal.config(fg="white",bg="#B3B6B7")
    except:
        if event != None:                                  # kahi data nastanna enter martoy tari te disla pahije color change mhanun
            btnequal.config(fg="white", bg="#B3B6B7")
        pass


def click(number):                                              # mouse ne button press kelyavar je click karat jatoy tyala entrybox madhe dakhvayla.
    global operator,entry1
    operator+=str(number)
    entry1.delete(0,END)    # entry box madhla sagla adhicha content delete kel(start index,end index)
    entry1.insert(0,operator) # ani navin string ji operator madhey ahe tyala insert kel entry box mahde  insert(index,string) ( fresh insert)

def clear():                                    # 'btnclear' dablyavar sagla adhicha clear karayla.
    global entry1,operator
    operator = ""
    entry1.delete(0,END)  #entrybox madhla sagla clear hoanr. i.e from 0 to END(purn string)
############################################################################################string
operator = ""

###################################################entrybox
entry1=Entry(screen)
entry1.grid(row=0,column=0,columnspan=4)    # ya entry box 1 column ahe pn tyache apan ajun 4 bhag padtoy tyachya khali buttons set karayla. karan entry box cha ek column asnar ani tyat khali 4 buttons aplyala takaychet
entry1.config(bg="#F9E79F",font=("calibri",20,"italic bold"),bd='30',justify="right")
entry1.focus()   # yavar bydefault click asel.aplyala karaychi garaj nahi

###########################################################################buttons

btn7=Button(screen,text="7",font=("calibri",20,"italic bold"),bd=8,padx=16,pady=16,command=lambda:click(7)   # jar grid() vaprat asu tar padx and pady internal padding aste.
            ,activebackground="#B3B6B7",activeforeground="white")     # bd for border.
btn7.grid(row=1,column=0)

btn8=Button(screen,text="8",font=("calibri",20,"italic bold"),bd=8,padx=16,pady=16,command=lambda:click(8),activebackground="#B3B6B7",activeforeground="white")
btn8.grid(row=1,column=1 )

btn9=Button(screen,text="9",font=("calibri",20,"italic bold"),bd=8,padx=16,pady=16,command=lambda:click(9),activebackground="#B3B6B7",activeforeground="white")
btn9.grid(row=1,column=2)

btnadd=Button(screen,text="+",font=("calibri",20,"italic bold"),bd=8,padx=16,pady=16,command=lambda:click('+'),fg="#F39C12")
btnadd.grid(row=1,column=3)
#
btn4=Button(screen,text="4",font=("calibri",20,"italic bold"),bd=8,padx=16,pady=16,command=lambda:click(4),activebackground="#B3B6B7",activeforeground="white")
btn4.grid(row=2,column=0)

btn5=Button(screen,text="5",font=("calibri",20,"italic bold"),bd=8,padx=16,pady=16,command=lambda:click(5),activebackground="#B3B6B7",activeforeground="white")
btn5.grid(row=2,column=1 )

btn6=Button(screen,text="6",font=("calibri",20,"italic bold"),bd=8,padx=16,pady=16,command=lambda:click(6),activebackground="#B3B6B7",activeforeground="white")
btn6.grid(row=2,column=2)

btnsub=Button(screen,text="-",font=("calibri",20,"italic bold"),bd=8,padx=19,pady=16,command=lambda:click('-'),fg="#F39C12")
btnsub.grid(row=2,column=3)
#
btn1=Button(screen,text="1",font=("calibri",20,"italic bold"),bd=8,padx=16,pady=16,command=lambda:click(1),activebackground="#B3B6B7",activeforeground="white")
btn1.grid(row=3,column=0)

btn2=Button(screen,text="2",font=("calibri",20,"italic bold"),bd=8,padx=16,pady=16,command=lambda:click(2),activebackground="#B3B6B7",activeforeground="white")
btn2.grid(row=3,column=1 )

btn3=Button(screen,text="3",font=("calibri",20,"italic bold"),bd=8,padx=16,pady=16,command=lambda:click(3),activebackground="#B3B6B7",activeforeground="white")
btn3.grid(row=3,column=2)

btnmult=Button(screen,text="*",font=("calibri",20,"italic bold"),bd=8,padx=17,pady=16,command=lambda:click('*'),fg="#F39C12")
btnmult.grid(row=3,column=3)
#
btn0=Button(screen,text="0",font=("calibri",20,"italic bold"),bd=8,padx=16,pady=16,command=lambda:click(0),activebackground="#B3B6B7",activeforeground="white")
btn0.grid(row=4,column=0)

btnclear=Button(screen,text="C",font=("calibri",20,"italic bold"),bd=8,padx=16,pady=16,command=clear,fg="#F39C12")
btnclear.grid(row=4,column=1)

btnequal=Button(screen,text="=",font=("calibri",20,"italic bold"),bd=8,padx=16,pady=16,command=equal,fg="white",bg="#F39C12")  #ethe equal la btnequal asach send kelay fakt error yeu nye mhanun karan bind(<return>) mule tyala ek argument dyavach lagel
btnequal.grid(row=4,column=2)

btndiv=Button(screen,text="/",font=("calibri",20,"italic bold"),bd=8,padx=17,pady=16,command=lambda:click("/"),fg="#F39C12")
btndiv.grid(row=4,column=3)

#########extra

btnsin=Button(screen,text="Sin",font=("calibri",20,"italic bold"),bd=8,padx=19,pady=16,command=lambda:click("sin"),activebackground="#B3B6B7",activeforeground="white",fg="white",bg="#F39C12")
btnsin.grid(row=0,column=5)

btncos=Button(screen,text="Cos",font=("calibri",20,"italic bold"),bd=8,padx=16,pady=16,command=lambda:click("cos"),fg="white",bg="#F39C12")
btncos.grid(row=1,column=5)

btntan=Button(screen,text="Tan",font=("calibri",20,"italic bold"),bd=8,padx=16,pady=16,command=lambda:click("tan"),fg="white",bg="#F39C12")  #ethe equal la btnequal asach send kelay fakt error yeu nye mhanun karan bind(<return>) mule tyala ek argument dyavach lagel
btntan.grid(row=2,column=5)

btnsqrt=Button(screen,text="Sqrt",font=("calibri",20,"italic bold"),bd=8,padx=13,pady=16,command=lambda:click("sqrt"),
               fg="#F39C12",activebackground="#B3B6B7",activeforeground="white")
btnsqrt.grid(row=3,column=5)

btnlog=Button(screen,text="Log",font=("calibri",20,"italic bold"),bd=8,padx=16,pady=16,command=lambda:click("log"),
              fg="#F39C12",activebackground="#B3B6B7",activeforeground="white")
btnlog.grid(row=4,column=5)
#######################################################################lists

l=[btn0,btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btnadd,btnsub,btnmult,btndiv,btnequal]  #konta button press kel te samjnya sathi,color change karta yeil mg tyacha using press()
l1=['1','2','3','4','5','6','7','8','9','0','+','-','/','*',"\r"]

#########################################################bind()
screen.bind("<Return>",equal)    # for Enter key event
screen.bind("<KeyPress>",press)  # for KeyPress event,Enter sathi nahi chlnar ata karan tyasathi <Return> banavlay mhanun,nahitar te pn zal asta
screen.bind("<KeyRelease>",release)  #for KeyRelease ani Enter sathi pn honar karan ti pn key ahe ani ti pn release honar press kelyavar
screen.bind("<BackSpace>",backspace) #for backspace key event
screen.bind("<Shift-Right>",rightkey)  # for right arrow event →
screen.bind("<Shift-Left>",leftkey)    # for left arrow event ←
screen.bind("<Escape>",escape)

screen.mainloop()


# shift + right_arrow extend honar calculator
# shift + left_arrow contract honar calc
# Esc ne close honar.