from tkinter import *
from tkinter.ttk import Combobox   #tkinter madhe ttk module madhe asto Combobox i.e.dropdown list
from tkinter import messagebox
from  textblob import TextBlob     # Text processing sathi vaparto hi library apan

lan_dict = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az',
            'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb',
            'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da',
            'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka',
            'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'iw', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is',
            'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku',
            'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi',
            'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru',
            'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw',
            'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo',
            'zulu': 'zu', 'Filipino': 'fil', 'Hebrew': 'he'}


####################################window
root  = Tk()
root.geometry("510x400")
root.title("Traslator")
root.wm_minsize(width=510,height=400)
root.wm_maxsize(width=510,height=400)
root.iconbitmap("icon.ico")
################################################### combo box of languages

languages = StringVar()    # yala apan Tk() chya adhi nahi vapru shakat karan tyacha interpeter use karat te mhanun Tk() nantar lihtoy aan
combo_box = Combobox(root,width=30,textvariable = languages, state="readonly")  #readonly mhanje tyala modify nhi karu shaknar apan
combo_box['values'] = [e for e in lan_dict.keys()]  # values taklya apan
combo_box.current(37)   # kahitari current value dyaychi ahe,apan hindi detoy jo 37 position la ahe list madhe

combo_box.place(x=150,y=130)

########################################functions

def translate(event=None):
    try:
        word3 = TextBlob(varname1.get())  # object banla ethe ani text dilay apla tyat
        lan = word3.detect_language()    # en asel english karan english madhe type kartoy na apan
        lan_todict = languages.get()   # konti language select keliye list madhun to convert
        lan_to = lan_dict[lan_todict] # value kadli i.e. hi for hindi, en for english etc..
        word3 = word3.translate(from_lang=lan,to=lan_to)
        label3.config(text=word3,fg="black",justify=CENTER)

    except:
        label3.config(text="Something went wrong!",fg='red')
        label3.place(x=150, y=320)


def close():
    rr = messagebox.askyesnocancel("Notification","Do you want to EXIT.",parent=root)
    if rr==True:
        root.destroy()





####################################### Entry box
varname1 =StringVar()

entry1 = Entry(root,width=30,textvariable=varname1,font=("comicsansms",15,"italic bold"),relief="groove",borderwidth = 3)
entry1.place(x=150,y=40)
entry1.focus()

###################################### Labels
label1 = Label(root,fg="#48C9B0",text = "Enter words",font=("comicsansms",15,"italic bold"))
label1.place(x=5,y=40)

label3 = Label(root,text = "",font=("comicsansms",15,"italic bold"),justify=CENTER)
label3.place(x=220,y=320)

################################ buttons

btn1 = Button(root,text="Translate",bd=8,bg="#AAB7B8",activebackground="#F0B27A",font=("comicsansms",10,"italic bold"),padx=3,pady=4,command=translate)
btn1.place(x=50,y=200,width=120)

btn2 = Button(root,text="Exit",bd=8,bg="#AAB7B8",activebackground="#F0B27A",font=("comicsansms",10,"italic bold"),padx=3 , pady = 4,command=close)
btn2.place(x=350,y=200,width=120)


root.bind("<Return>",translate)

root.mainloop()
