import requests   # html cha data ananyasathi i.e. html page cha code
from bs4 import BeautifulSoup  # data scrapping sathi kamat yeto
import plyer #for notification
from tkinter import *
from tkinter import messagebox,filedialog  #filedialoge path store karnyasathi sathi
import pandas # file save karayla
import threading


root = Tk()
root.title("COVID-19 Updates")
root.geometry("530x300+200+80")
root.configure(bg="#F6DDCC")
root.iconbitmap("icon.ico")
##################################################functions

def downloadThread():
    thread = threading.Thread(target=download)
    thread.start()

def scrap():
    def notifyme(title,message):
        plyer.notification.notify(
            title=title,
            message=message,
            app_icon="icon.ico",
            app_name="COVID-19 Updates",
            timeout=20 #kiti time rahel notification

        )
    url = "https://www.worldometers.info/coronavirus/"
    r = requests.get(url)  # r.text madhe code asel tya page cha
    soup = BeautifulSoup(r.content,'html.parser')
    #print(soup.prettify())   #code ekdam proper format madhe yeil, html format nit indentation vegere
    tablebody = soup.find("tbody")  # tbody tag madhe apla table data,ekach table ahe purn page var mhanun find ne kam houn janar
    #print(tablebody)
    ttt = tablebody.find_all("tr") # find all ne sagle tr tag bhetnar tya tablebody madhle

    notifycountry = countrydata.get()

    if notifycountry == "":
        notifycountry="india"


    countries,total_cases,new_cases,total_deaths,new_deaths,total_recover,active_cases = [],[],[],[],[],[],[]
    serious,totalcases_permillion,totaldeaths_permillion,totaltests,totaltests_permillion = [],[],[],[],[]

    headers = ['countries','total_cases','new_cases','total_deaths','new_deaths','total_recover','active_cases',
               'serious','totalcases_permillion','totaldeaths_permillion','totaltests','totaltests_permillion'
               ]


    for i in ttt:
        id = i.find_all("td")
        #print(id[].text.strip().replace(",",""))   # karan id madhe sagle td ale ahet tyatlya first td cha text city name ahe
        if id[1].text.strip().lower() == notifycountry:
            totalcases = int(id[2].text.strip().replace(",",""))
            totaldeaths = id[4].text.strip()
            newcases = id[3].text.strip()
            newdeaths = id[5].text.strip()
            notifyme("Corona Virus Details In {}".format(notifycountry),
                   'Total Cases : {}\nTotal Deaths : {}\nNew Cases : {}\nNew Deaths : {}'.format(totalcases,totaldeaths,newcases,newdeaths))



        countries.append(id[1].text.strip()),
        total_cases.append(int(id[2].text.strip().replace(',',''))) #strip mule spaces remove hotat baki kahi nahi.ani numbers madhe comma kadayla replace vaparlay eg 12,230,321 cha honar 12230321 karan aplyala tyala int madhe convert karaychay sorting sathi
        new_cases.append(id[3].text.strip()),total_deaths.append(id[4].text.strip())
        new_deaths.append(id[5].text.strip()),total_recover.append(id[6].text.strip())
        active_cases.append(id[7].text.strip()),serious.append(id[8].text.strip())
        totalcases_permillion.append(id[9].text.strip()),totaldeaths_permillion.append(id[10].text.strip())
        totaltests.append(id[11].text.strip()),totaltests_permillion.append(id[12].text.strip())
    df = pandas.DataFrame(list(zip(countries,total_cases,new_cases,total_deaths
                              ,new_deaths,total_recover,active_cases,serious,
                              totalcases_permillion,totaldeaths_permillion,
                              totaltests,totaltests_permillion )),columns=headers)
    sor = df.sort_values('total_cases',ascending=False)

    global HTMLval,CSVval

    if HTMLval.get()==True:
        path2 = '{}/alldata.html'.format(path)
        sor.to_html(r'{}'.format(path2))

    if CSVval.get()==True:
        path2 = '{}/alldata.csv'.format(path)
        sor.to_csv(r'{}'.format(path2))

    if HTMLval.get()==True or CSVval.get()==True:
        messagebox.showinfo("Notification","Corona record is stored at {}".format(path),parent=root)

def download():
    submitbtn.config(state=DISABLED)
    global path,HTMLval,CSVval
    if (HTMLval.get()==True or CSVval.get()==True):
        path = filedialog.askdirectory() # pop up window yenar kuthe store karaychay tyasathi,ani return karel jithe store karnar ahe to path

    scrap()
    HTMLval.set(False) # sagla zalyavar parat uncheck honya sathi
    CSVval.set(False)
    submitbtn.config(state=NORMAL)


########################################## labels
IntroLabel = Label(root,text="Corona Virus Info",font=("Comic Sans Ms",20,"bold"),width=22,justify=CENTER,bg="#F6DDCC",fg="#3498DB")
IntroLabel.place(x=70,y=0)

EntryLabel = Label(root,text="Country Name :",font=("Comic Sans Ms",15,"bold"),bg="#F6DDCC")
EntryLabel.place(x=10,y=70)

FormatLabel = Label(root,text="Download as :",font=("Comic Sans Ms",15,"bold"),bg="#F6DDCC")
FormatLabel.place(x=10,y=150)
############################################# Entry
countrydata = StringVar()

ent1 = Entry(root,textvariable=countrydata,font=("calibri",15,"bold"),bd=4,relief="groove",width=25)
ent1.place(x=220,y=75)
############################################## buttons

HTMLval = BooleanVar()
CSVval = BooleanVar()


checkboxHTML = Checkbutton(root,text="HTML",font=("calibri",15,"bold"),bd=4,activeforeground="white",activebackground="#EB984E",width=7,bg="#F6DDCC",variable=HTMLval)
checkboxHTML.place(x=210,y=150)

checkboxCSV = Checkbutton(root,text="CSV",font=("calibri",15,"bold"),bd=4,activeforeground="white",activebackground="#EB984E",width=7,bg="#F6DDCC",variable=CSVval)
checkboxCSV.place(x=370,y=150)

submitbtn = Button(root,text="SUBMIT",font=("calibri",13,"bold"),bg="#3498DB",bd=4,activeforeground="white",activebackground="#EB984E",width=10,command=downloadThread)
submitbtn.place(x=220,y=240)




root.mainloop()
