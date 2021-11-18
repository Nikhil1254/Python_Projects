from tkinter import *
from tkinter import Toplevel  # chotya valya windows display karayla nantar
import time
import random
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Treeview   # he khoop mast module ahe he nasta tar aplyala tables verege display karayvala seperate code lihayla lagla asta
from tkinter import ttk
import pymysql # database sathi lagnare
import pandas  # export option sathi

root = Tk()
root.title("Student Managment System")
# root.config(bg="lightblue")
root.geometry("1174x700+200+50")
root.iconbitmap("icon.ico")
root.wm_resizable(False,False)  # he jast changlay wm_minsize ani tya peksha (width,height) dogh False kelet apan

############################################# functions
def ConnectDatabase():
    def submitdb():
        global con,mycursor

        host = hostVal.get()
        user = userVal.get()
        password = passwordVal.get()
        try:                                        ######### to establish connection with mysql
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()                    # cursor apla handler ahe tyachya through ch apan saggle database operations perform karto.
            dbroot.destroy()
        except:
            messagebox.showerror("Notification","Incorrect Info Provided,please try again!")
            return

        try:                # connection zalya nantar chi kam
            '''
                he apan new user sathi kartoy.tyasathi sagla tayar hoil jar first time karat asel tar.
            '''
            mycursor.execute("create database studentmanagementsystem")
            mycursor.execute("use studentmanagementsystem")
            mycursor.execute("create table studentdata(Id int primary key,Name varchar(20),Mobile varchar(12),Email varchar(30),Address varchar(100),Gender varchar(50),dob varchar(50),Date varchar(50),Time varchar(50))")
            messagebox.showinfo("Notification","Connected To Database.") # parent var pop hoil box
        except:
            mycursor.execute("use studentmanagementsystem")
            messagebox.showinfo("Notification","Connected To Database.") # parent var pop hoil box

    dbroot = Toplevel()
    dbroot.grab_set()    # yamule hoil asa ki hi screen banel tevha focus madhe rahil continously dusari kade kuthe apan click nahi karu shaknar ya screen shivay
    '''
        mhanje connect database valya crenn cha kam hoil ani apan tila cut karu tevhach
        dusrikade click karta yenar mg.
    '''
    dbroot.geometry("470x250+800+230")
    dbroot.config(bg="#E5E7E9")
    dbroot.iconbitmap("icon.ico")
    dbroot.wm_resizable(False,False) # False,False mhanje width,height dogh change nahi karta yenar

    ######################## Labels
    hostLable = Label(dbroot,text="Host ",font=("Comic Sans Ms",20,"bold"),justify=CENTER,bg="#E5E7E9")
    hostLable.place(x=10,y=10)

    userLable = Label(dbroot, text="Username ", font=("Comic Sans Ms", 20, "bold"),bg="#E5E7E9", justify=CENTER)
    userLable.place(x=10, y=60)

    passwordLable = Label(dbroot, text="Password ", font=("Comic Sans Ms", 20, "bold"),bg="#E5E7E9", justify=CENTER)
    passwordLable.place(x=10, y=110)
    ########################### Entry box
    hostVal = StringVar()
    userVal = StringVar()
    passwordVal = StringVar()

    hostentry = Entry(dbroot,font=("airal",15,"bold"),bd=3,textvariable=hostVal)
    hostentry.place(x=200,y=10)

    userentry = Entry(dbroot, font=("airal", 15, "bold"), bd=3,textvariable=userVal)
    userentry.place(x=200, y=60)

    passwordentry = Entry(dbroot, font=("airal", 15, "bold"), bd=3,textvariable=passwordVal)
    passwordentry.place(x=200, y=110)

    ################################# button
    submitbtn= Button(dbroot,text="Submit",font=("Comic Sans Ms",14,"bold"),width=15,bg="#CACFD2",bd=3,activebackground="#F8C471",activeforeground="white",command=submitdb)
    submitbtn.place(x=130,y=190)

    dbroot.mainloop()

def addstudent():
    def submitadd():
        id = idval.get()
        name = nameVal.get()
        mobile = mobileVal.get()
        email = emailVal.get()
        gender = genderVal.get()
        address = addressVal.get()
        dob = dobVal.get()
        addedtime = time.strftime("%H : %M : %S")   # currecnt time system cha deil apan lihilelya format madhe
        addeddate = time.strftime("%d/%m/%Y")      # apan dilelya format madhe date denar

        try:
            mycursor.execute("insert into studentdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(id,name,mobile,email,address,gender,dob,addeddate,addedtime))
            con.commit()   # jar database madhe kahi modification karat asu tar commit karav lagel mhanje changes permanent honar database madhe.
            res = messagebox.askyesnocancel("Notification","id {} name {} added successfully....Do you want to clear form".format(id,name),parent = addroot)
            if res:
                idval.set("")
                nameVal.set("")
                mobileVal.set("")
                emailVal.set("")
                genderVal.set("")
                addressVal.set("")
                dobVal.set("")
        except:
            messagebox.showerror("Notification","Id already exits,or either you are not connected to database!",parent=addroot) # jo parent deto na apan jo paryant messagebox jat nahi parent pn tasach rahnar screen var
            return

        mycursor.execute("select * from studentdata")
        datas = mycursor.fetchall()  # table madhla sagla data return karel he function

        studentTable.delete(*studentTable.get_children()) # studenTable madhla adhi je asel te delete kel sagla
        for i in datas:
            w = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studentTable.insert("",END,values=w)

    addroot = Toplevel(master=DataEntryFrame) # master jo deil tyavar he tayar hoil
    addroot.grab_set()  # bakich stop karayla yavarach focus thevayla
    addroot.geometry("480x475+220+200")
    addroot.title("Student Management System")
    addroot.iconbitmap("icon.ico")
    addroot.config(bg="#E5E7E9")
    addroot.wm_resizable(False,False)  # window resize nko vhayla mhanun

    ############################### Labels
    idLabel = Label(addroot,text="Id",font=("times",20,"bold"),bg="#E5E7E9")
    idLabel.place(x=10,y=10)

    nameLabel = Label(addroot, text="Name", font=("times", 20, "bold"),bg="#E5E7E9")
    nameLabel.place(x=10, y=70)

    mobiemailLabel = Label(addroot, text="Mobile No", font=("times", 20, "bold"),bg="#E5E7E9")
    mobiemailLabel.place(x=10, y=130)

    emailLabel = Label(addroot, text="Email", font=("times", 20, "bold"),bg="#E5E7E9")
    emailLabel.place(x=10, y=190)

    addressLabel = Label(addroot, text="Address", font=("times", 20, "bold"),bg="#E5E7E9")
    addressLabel.place(x=10, y=250)

    genderLabel = Label(addroot, text="Gender", font=("times", 20, "bold"),bg="#E5E7E9")
    genderLabel.place(x=10, y=310)

    dobLabel = Label(addroot, text="DOB", font=("times", 20, "bold"),bg="#E5E7E9")
    dobLabel.place(x=10, y=370)

    ######################################## Entry
    idval = StringVar()
    nameVal = StringVar()
    mobileVal = StringVar()
    emailVal = StringVar()
    genderVal = StringVar()
    addressVal = StringVar()
    dobVal = StringVar()

    idEntry = Entry(addroot,font=("calibri",15),bd=5,textvariable=idval)
    idEntry.place(x=250,y=10)

    nameEntry = Entry(addroot, font=("calibri", 15), bd=5, textvariable=nameVal)
    nameEntry.place(x=250, y=70)

    mobileEntry = Entry(addroot, font=("calibri", 15), bd=5, textvariable=mobileVal)
    mobileEntry.place(x=250, y=130)

    emailEntry = Entry(addroot, font=("calibri", 15), bd=5, textvariable=emailVal)
    emailEntry.place(x=250, y=190)

    addressEntry = Entry(addroot, font=("calibri", 15), bd=5, textvariable=addressVal)
    addressEntry.place(x=250, y=250)

    genderEntry = Entry(addroot, font=("calibri", 15), bd=5, textvariable=genderVal)
    genderEntry.place(x=250, y=310)

    dobEntry = Entry(addroot, font=("calibri", 15), bd=5, textvariable=dobVal)
    dobEntry.place(x=250, y=370)

    ######################################### Button
    submitbtn = Button(addroot,text="Submit",font=("Comic Sans Ms",13,"bold"),width=15,bd=5,activebackground="#F8C471",activeforeground="white",command=submitadd)
    submitbtn.place(x=150,y=420)

    addroot.mainloop()

def searchstudent():
    def search():
        try:
            id = idval.get()
            name = nameVal.get()
            mobile = mobileVal.get()
            email = emailVal.get()
            gender = genderVal.get()
            address = addressVal.get()
            dob = dobVal.get()
            addeddate = time.strftime("%d/%m/%Y")  # apan dilelya format madhe date denar

            if id!="":
                mycursor.execute("select * from studentdata where id=%s",(id))
                datas = mycursor.fetchall()
            elif name != "":
                mycursor.execute("select * from studentdata where name=%s",(name))
                datas = mycursor.fetchall()
            elif mobile != "":
                mycursor.execute("select * from studentdata where mobile=%s",(mobile))
                datas = mycursor.fetchall()
            elif email != "":
                mycursor.execute("select * from studentdata where email=%s",(email))
                datas = mycursor.fetchall()
            elif address != "":
                mycursor.execute("select * from studentdata where address=%s",(address))
                datas = mycursor.fetchall()
            elif gender != "":
                mycursor.execute("select * from studentdata where gender=%s",(gender))
                datas = mycursor.fetchall()
            elif dob != "":
                mycursor.execute("select * from studentdata where dob=%s",(dob))
                datas = mycursor.fetchall()
            elif addeddate != "":
                mycursor.execute("select * from studentdata where date=%s",(addeddate))
                datas = mycursor.fetchall()

            studentTable.delete(*studentTable.get_children())  # studenTable madhla adhi je asel te delete kel sagla
            for i in datas:
                w = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studentTable.insert("", END, values=w)  # "" manje start ani END mhanje shevat paryant i.e. sagle columns
        except:
            messagebox.showerror("Notification","First Connect To Database!")


    searchroot = Toplevel(master=DataEntryFrame)  # master jo deil tyavar he tayar hoil
    searchroot.grab_set()  # bakich stop karayla yavarach focus thevayla
    searchroot.geometry("480x540+220+200")
    searchroot.title("Student Management System")
    searchroot.config(bg="#E5E7E9")
    searchroot.iconbitmap("icon.ico")
    searchroot.wm_resizable(False, False)  # window resize nko vhayla mhanun

    ############################### Labels
    idLabel = Label(searchroot, text="Id", font=("times", 20, "bold"),bg="#E5E7E9")
    idLabel.place(x=10, y=10)

    nameLabel = Label(searchroot, text="Name", font=("times", 20, "bold"),bg="#E5E7E9")
    nameLabel.place(x=10, y=70)

    mobiemailLabel = Label(searchroot, text="Mobile No", font=("times", 20, "bold"),bg="#E5E7E9")
    mobiemailLabel.place(x=10, y=130)

    emailLabel = Label(searchroot, text="Email", font=("times", 20, "bold"),bg="#E5E7E9")
    emailLabel.place(x=10, y=190)

    addressLabel = Label(searchroot, text="Address", font=("times", 20, "bold"),bg="#E5E7E9")
    addressLabel.place(x=10, y=250)

    genderLabel = Label(searchroot, text="Gender", font=("times", 20, "bold"),bg="#E5E7E9")
    genderLabel.place(x=10, y=310)

    dobLabel = Label(searchroot, text="DOB", font=("times", 20, "bold"),bg="#E5E7E9")
    dobLabel.place(x=10, y=370)

    dateLabel = Label(searchroot, text="Enter Date", font=("times", 20, "bold"),bg="#E5E7E9")
    dateLabel.place(x=10, y=430)

    ######################################## Entry
    idval = StringVar()
    nameVal = StringVar()
    mobileVal = StringVar()
    emailVal = StringVar()
    genderVal = StringVar()
    addressVal = StringVar()
    dobVal = StringVar()
    dateVal = StringVar()

    idEntry = Entry(searchroot, font=("calibri", 15), bd=5, textvariable=idval)
    idEntry.place(x=250, y=10)

    nameEntry = Entry(searchroot, font=("calibri", 15), bd=5, textvariable=nameVal)
    nameEntry.place(x=250, y=70)

    mobileEntry = Entry(searchroot, font=("calibri", 15), bd=5, textvariable=mobileVal)
    mobileEntry.place(x=250, y=130)

    emailEntry = Entry(searchroot, font=("calibri", 15), bd=5, textvariable=emailVal)
    emailEntry.place(x=250, y=190)

    addressEntry = Entry(searchroot, font=("calibri", 15), bd=5, textvariable=addressVal)
    addressEntry.place(x=250, y=250)

    genderEntry = Entry(searchroot, font=("calibri", 15), bd=5, textvariable=genderVal)
    genderEntry.place(x=250, y=310)

    dobEntry = Entry(searchroot, font=("calibri", 15), bd=5, textvariable=dobVal)
    dobEntry.place(x=250, y=370)

    dateEntry = Entry(searchroot, font=("calibri", 15), bd=5, textvariable=dateVal)
    dateEntry.place(x=250, y=430)

    ######################################### Button
    searchbtn = Button(searchroot, text="Search", font=("Comic Sans Ms", 13, "bold"), width=15, bd=5,
                       activebackground="#F8C471", activeforeground="white", command=search)
    searchbtn.place(x=150, y=480)

    searchroot.mainloop()

def deletestudent():
    click = studentTable.focus()  # kashavar click kelay te kalta easily.
    content = studentTable.item(click)   # jya row var click kelay tyache sagle items return karel,dictionary det tyat 'values' key madhe aplya row cha data asto
    id = content['values'][0]  # values key madhe list ahe aplya saglya fields chi apan fakt id kadla tyatun 0th index la hota to
    mycursor.execute("delete from studentdata where id=%s",(id))
    con.commit()
    messagebox.showinfo("Notification","id:{} deleted successfully.".format(id))
    showstudent()           # Treeview update kela mhanje delete zalyach fell pn yeil lagech

def updatestudent():
    def update():
        id = idval.get()
        name = nameVal.get()
        mobile = mobileVal.get()
        email = emailVal.get()
        address = addressVal.get()
        gender = genderVal.get()
        dob = dobVal.get()
        date = dateVal.get()
        time = timeVal.get()

        query = "update studentdata set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s"
        mycursor.execute(query,(name,mobile,email,address,gender,dob,date,time,id))
        con.commit()  # jevha apan modification karto kahihi database madhe commit kele tarach tyat changes honar.
        messagebox.showinfo("Notification","Id:{} modified successfully.".format(id),parent=updateroot)
        showstudent()

    updateroot = Toplevel(master=DataEntryFrame)  # master jo deil tyavar he tayar hoil
    updateroot.grab_set()  # bakich stop karayla yavarach focus thevayla
    updateroot.geometry("480x600+220+140")
    updateroot.title("Student Management System")
    updateroot.config(bg="#E5E7E9")
    updateroot.iconbitmap("icon.ico")
    updateroot.wm_resizable(False, False)  # window resize nko vhayla mhanun

    ############################### Labels
    idLabel = Label(updateroot, text="Id", font=("times", 20, "bold"),bg="#E5E7E9")
    idLabel.place(x=10, y=10)

    nameLabel = Label(updateroot, text="Name", font=("times", 20, "bold"),bg="#E5E7E9")
    nameLabel.place(x=10, y=70)

    mobiemailLabel = Label(updateroot, text="Mobile No", font=("times", 20, "bold"),bg="#E5E7E9")
    mobiemailLabel.place(x=10, y=130)

    emailLabel = Label(updateroot, text="Email", font=("times", 20, "bold"),bg="#E5E7E9")
    emailLabel.place(x=10, y=190)

    addressLabel = Label(updateroot, text="Address", font=("times", 20, "bold"), bg="#E5E7E9")
    addressLabel.place(x=10, y=250)

    genderLabel = Label(updateroot, text="Gender", font=("times", 20, "bold"), bg="#E5E7E9")
    genderLabel.place(x=10, y=310)

    dobLabel = Label(updateroot, text="DOB", font=("times", 20, "bold"),bg="#E5E7E9")
    dobLabel.place(x=10, y=370)

    dateLabel = Label(updateroot, text="Enter Date", font=("times", 20, "bold"),bg="#E5E7E9")
    dateLabel.place(x=10, y=430)

    timeLabel = Label(updateroot, text="Enter Time", font=("times", 20, "bold"),bg="#E5E7E9")
    timeLabel.place(x=10, y=490)

    ######################################## Entry
    idval = StringVar()
    nameVal = StringVar()
    mobileVal = StringVar()
    emailVal = StringVar()
    genderVal = StringVar()
    addressVal = StringVar()
    dobVal = StringVar()
    dateVal = StringVar()
    timeVal = StringVar()

    idEntry = Entry(updateroot, font=("calibri", 15), bd=5, textvariable=idval)
    idEntry.place(x=250, y=10)

    nameEntry = Entry(updateroot, font=("calibri", 15), bd=5, textvariable=nameVal)
    nameEntry.place(x=250, y=70)

    mobileEntry = Entry(updateroot, font=("calibri", 15), bd=5, textvariable=mobileVal)
    mobileEntry.place(x=250, y=130)

    emailEntry = Entry(updateroot, font=("calibri", 15), bd=5, textvariable=emailVal)
    emailEntry.place(x=250, y=190)

    addressEntry = Entry(updateroot, font=("calibri", 15),bd=5, textvariable=addressVal)
    addressEntry.place(x=250, y=250)

    genderEntry = Entry(updateroot, font=("calibri", 15), bd=5, textvariable=genderVal)
    genderEntry.place(x=250, y=310)

    dobEntry = Entry(updateroot, font=("calibri", 15), bd=5, textvariable=dobVal)
    dobEntry.place(x=250, y=370)

    dateEntry = Entry(updateroot, font=("calibri", 15), bd=5, textvariable=dateVal)
    dateEntry.place(x=250, y=430)

    timeEntry = Entry(updateroot, font=("calibri", 15), bd=5, textvariable=timeVal)
    timeEntry.place(x=250, y=490)

    ######################################### Button
    updatebtn = Button(updateroot, text="Update", font=("Comic Sans Ms", 13, "bold"), width=15, bd=5,
                       activebackground="#F8C471", activeforeground="white", command=update,bg="#E5E7E9")
    updatebtn.place(x=150, y=540)
    click = studentTable.focus()  # kashavar click kelay te samjnya sathi.
    content = studentTable.item(click)    # dictionary return karat khoop sarya values chi tyat 'values' key aste tyat apala row madhla data asto
    list1 = content['values']  # aplya saglya values chi list values key la ahe dictionary madhe

    if len(list1)!=0:
        idval.set(list1[0])
        nameVal.set(list1[1])
        mobileVal.set(list1[2])
        emailVal.set(list1[3])
        addressVal.set(list1[4])
        genderVal.set(list1[5])
        dobVal.set(list1[6])
        dateVal.set(list1[7])
        timeVal.set(list1[8])


    updateroot.mainloop()

def showstudent():
    try:
        mycursor.execute("select * from studentdata")
        datas = mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())  # studenTable Treeview madhla adhi je asel te delete kel sagla
        for i in datas:
            w = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studentTable.insert("", END, values=w)  # "" manje start ani END mhanje shevat paryant i.e. sagle columns
    except:
        messagebox.showerror("Notification","First Connect To Database!")

def export():
    ff = filedialog.asksaveasfilename()  # ti window dakvel file save karayvali.
    data = studentTable.get_children()   # aplya Treeview madhe je show kartoy apan te sagla ghetla   i.e. Treeview madhlya saglya rows
    id,name,mobile,email,address,gender,dob,addeddate,addedtime = [],[],[],[],[],[],[],[],[]

    for i in data:
        content = studentTable.item(i)  # row by row content madhe tya row cha sagla data jo values key madhey karan hi ek dictionary ahe.
        pp = content['values']
        id.append(pp[0])
        name.append(pp[1])
        mobile.append(pp[2])
        email.append(pp[3])
        address.append(pp[4])
        gender.append(pp[5])
        dob.append(pp[6])
        addeddate.append(pp[7])
        addedtime.append(pp[8])

        headings = ['Id','Name','Mobile','Email','Address','Gender','DOB','Added Date','Added Time']
        df = pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=headings)  # insert kartoy file madhe ek by ek value
        paths = r'{}.csv'.format(ff)  #csv comma seperated values
        df.to_csv(paths,index=False)
        messagebox.showinfo("Notification","Student data is Saved at {}".format(paths))

def exit():
    res = messagebox.askyesnocancel("Notification","Do you want to exit ?")  # yes-True ,no-False , cancle- None return karat
    if res:
        root.destroy()

colors = ["#CD6155","#EC7063","#9B59B6","#2980B9","#1ABC9C","#27AE60","#F39C12","#E67E22"]  # to change colors of welcome message

def tick():   # date and time sathi continously update karnya sathi.
    time_string = time.strftime("%H : %M : %S")  # %H hours,%M minutes , %S seconds ani tyanchya aat hava te seperator vaparu shakto eg , / :
    date_string = time.strftime("%d/%m/%Y") # %d day , %m month , %Y year ani seperator hava to use karu shakto
    TimeLabel.config(text="Time - "+ time_string)
    DateLabel.config(text="Date - "+ date_string)
    random.shuffle(colors)
    WelcomeLabel.config(fg=colors[0])
    root.after(1000,tick)   #repeatadely call karnya sathi 1sec ne tick call honar parat parat





#################################################### Frames
############################################################################# DataEntryFrame
DataEntryFrame = Frame(root,borderwidth=5,relief="groove")
DataEntryFrame.place(x=10,y=80,width=500,height=600)

frontLabel = Label(DataEntryFrame,text="---------- Tools ----------",font=("Comic Sans Ms",22,"bold"))
frontLabel.pack(side=TOP,expand=True)
'''
    Top mule kay hota var var jat jata ek ek item ala ki.
    expand=True mule kay hotay height vise properly bastat sagle nit distance ne.
'''

addbtn = Button(DataEntryFrame,text="Add Student",width=20,font=("calibri",20,"bold"),bd=5,bg="#BFC9CA",activebackground="#F8C471",activeforeground="white",borderwidth=3,relief="groove",command=addstudent)
addbtn.pack(side=TOP,expand=True)

searchbtn = Button(DataEntryFrame,text="Search Student",width=20,font=("calibri",20,"bold"),bd=5,bg="#BFC9CA",activebackground="#F8C471",activeforeground="white",borderwidth=3,relief="groove",command=searchstudent)
searchbtn.pack(side=TOP,expand=True)

deletebtn = Button(DataEntryFrame,text="Delete student",width=20,font=("calibri",20,"bold"),bd=5,bg="#BFC9CA",activebackground="#F8C471",activeforeground="white",borderwidth=3,relief="groove",command=deletestudent)
deletebtn.pack(side=TOP,expand=True)

updatebtn = Button(DataEntryFrame,text="Update student",width=20,font=("calibri",20,"bold"),bd=5,bg="#BFC9CA",activebackground="#F8C471",activeforeground="white",borderwidth=3,relief="groove",command=updatestudent)
updatebtn.pack(side=TOP,expand=True)

showallbtn = Button(DataEntryFrame,text="Show All",width=20,font=("calibri",20,"bold"),bd=5,bg="#BFC9CA",activebackground="#F8C471",activeforeground="white",borderwidth=3,relief="groove",command=showstudent)
showallbtn.pack(side=TOP,expand=True)

exportbtn = Button(DataEntryFrame,text="Export",width=20,font=("calibri",20,"bold"),bd=5,bg="#BFC9CA",activebackground="#F8C471",activeforeground="white",borderwidth=3,relief="groove",command=export)
exportbtn.pack(side=TOP,expand=True)

exitbtn = Button(DataEntryFrame,text="Exit",width=20,font=("calibri",20,"bold"),bd=5,bg="#BFC9CA",activebackground="#F8C471",activeforeground="white",borderwidth=3,relief="groove",command=exit)
exitbtn.pack(side=TOP,expand=True)



################################################################# ShowDataFrame

ShowDataFrame = Frame(root,borderwidth=5,relief="groove")
ShowDataFrame.place(x=550,y=80,width=620,heigh=600)

############# ShowDataFrame Madhla bakicha stuff i.e. table scroll bar vegere sagla
style =ttk.Style()
style.theme_use('alt')
style.configure("Treeview.Heading",font=("Comic Sans Ms",15,"bold"),foreground="#52BE80",background="#FAE5D3")
style.configure("Treeview",font=("calibri",13,"bold"),background="cyan",foreground="#52BE80")

scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)

studentTable = Treeview(ShowDataFrame,column=('Id','Name','Mobile No','Email','Address','Gender','D.O.B','Added Date','Added Time')
                        ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set) # Treeview(master,columns)
'''
    xscrollcommand ani yscrollcommand vaprun basically apan aplya slider la dusrya widget sobat
    connect karu shakto using Scrollbar.set() method
'''
scroll_x.pack(side=BOTTOM,fill=X)  # horizontally purn occupy karel jaga ani bottom la placed asnar.
scroll_x.config(command=studentTable.xview)  # scroll_x mule student table cha xview move honar i.e. horizontally
scroll_y.pack(side=RIGHT,fill=Y)    # vertically purn jaga ghenar ani right side la placed asnar.
scroll_y.config(command=studentTable.yview) #scroll_y karu tevha studentTable cha yview move honar i.e. khali var vertically

studentTable.heading('Id',text="Id")        # heading('column name',text='text of that column')
studentTable.heading('Name',text="Name")
studentTable.heading('Mobile No',text="Mobile No")
studentTable.heading('Email',text="Email")
studentTable.heading('Address',text="Address")
studentTable.heading('Gender',text="Gender")
studentTable.heading('D.O.B',text="D.O.B")
studentTable.heading('Added Date',text="Added Date")
studentTable.heading('Added Time',text="Added Time")
'''
    ani swatah ek column add karto Treeview Id sathi asto to tyanchy.
    Tyala aplyala kadayla lagel.
'''
studentTable['show'] = "headings"  #fakt aplya headings ch show hotil

studentTable.column('Id',width=100,anchor=CENTER)
studentTable.column('Name',width=200,anchor=CENTER)
studentTable.column('Mobile No',width=200,anchor=CENTER)
studentTable.column('Email',width=300,anchor=CENTER)
studentTable.column('Address',width=300,anchor=CENTER)
studentTable.column('Gender',width=100,anchor=CENTER)
studentTable.column('D.O.B',width=150,anchor=CENTER)
studentTable.column('Added Date',width=150,anchor=CENTER)
studentTable.column('Added Time',width=150,anchor=CENTER)

studentTable.pack(fill=BOTH,expand=True)  #fill=BOTH manje height weight purn space vapraychay aplyala,ani expand ne te actually expand hoil.ya dogh goshti sobatach vapravya lagtat.


###################################################### Labels

WelcomeLabel = Label(root,text = " Welcome to Student Management System ",font=("Comic Sans Ms",20,"bold"),borderwidth=4,relief="solid")
WelcomeLabel.place(x=300,y=15)

##################################################### clock

TimeLabel = Label(root,font=("times",14,"bold"),text="Time - ")
TimeLabel.place(x=3,y=10)
DateLabel = Label(root,font=("times",14,"bold"),text="Date - ")
DateLabel.place(x=3,y=40)
tick()
####################################################### button

DatabaseBtn = Button(root,text="Connect To Database",padx=5,pady=5,bd=3,command=ConnectDatabase)
DatabaseBtn.place(x=1000,y=22)

root.mainloop()