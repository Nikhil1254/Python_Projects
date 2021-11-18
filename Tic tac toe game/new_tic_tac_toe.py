from tkinter import *;
import tkinter.messagebox;


root = Tk();
root.geometry("1050x640+70+100");																																# 70=x and 100=y from top-left corner
root.wm_minsize(width=1050 , height=640);
root.wm_maxsize(width=1050 , height=640);
root.title("Tic Tac Toe Game");
root.iconbitmap("tic_tac_toe_1.ico")
#root.config(bg='#FA8072');																																	# Window colour


# Players score
PlayerX = IntVar();
PlayerO = IntVar();

PlayerX.set(0);
PlayerO.set(0);


# For True play X     else Y turn
click = True;
        

# Top frame to display title
Tops = Frame(root , borderwidth=10 ,  bg='#29AB87' , pady=2 , width=1030 , height=100 , relief=GROOVE);
Tops.grid(row=0,column=0);


lblPlayerX = Label(Tops , font=("arrial",31,"bold") , text="  " , padx=2,pady=10, bg='#29AB87');
lblPlayerX.grid(row=0,column=0);

lblPlayerX = Label(Tops , font=("arrial",31,"bold") , text="Player X :" , padx=2,pady=10, bg='#29AB87');
lblPlayerX.grid(row=0,column=1);
textPlayerX = Entry(Tops,font=("arrial",31,"bold"),bd=2,fg="black",textvariable=PlayerX,width=10,justify=LEFT, state=DISABLED);
textPlayerX.grid(row=0,column=2 , pady=10);

lblPlayerX = Label(Tops , font=("arrial",31,"bold") , text="    " , padx=2,pady=10, bg='#29AB87');
lblPlayerX.grid(row=0,column=3);

lblPlayerO = Label(Tops , font=("arrial",31,"bold") , text="Player O :" , padx=2,pady=10, bg='#29AB87');
lblPlayerO.grid(row=0,column=4);
textPlayerO = Entry(Tops,font=("arrial",31,"bold"),bd=2,fg="black",textvariable=PlayerO,width=10,justify=LEFT , state=DISABLED);
textPlayerO.grid(row=0,column=5 , pady=10);

lblPlayerX = Label(Tops , font=("arrial",31,"bold") , text="   " , padx=2,pady=10, bg='#29AB87');
lblPlayerX.grid(row=0,column=6);



# Main frame for game and score,reset,new game
MainFrame = Frame(root , bg='#FA8072' , borderwidth=10 , pady=2 , width=1050 , height=620 , relief=RIDGE);
MainFrame.grid(row=1,column=0 , ipadx=7 , ipady=10 , padx=12 , pady=10);


# For playing game
LeftFrame = Frame(MainFrame,borderwidth=6,width=750,height=500,pady=4,padx=4,bg='#FA8072' , relief=GROOVE);
LeftFrame.pack(side=LEFT);


# For score and buttons(reset,new game)
RightFrame = Frame(MainFrame,borderwidth=8,width=410,height=400,pady=2,padx=10,bg='#FA8072' , relief=GROOVE);
RightFrame.pack(side=RIGHT);



# Check after every click
def checker(button):
	global click;

	if button["text"] == " " and click == True:
		button.config(text="X");
		click = False;

	elif button["text"] == " " and click == False:
		button.config(text="O");
		click = True;

	Score();



# Reset
def Reset(ng=False,confirm="no"):

	global butt;
	global click;

	if ng==False:
		confirm = tkinter.messagebox.askquestion("confirm" , "Do You want to reset");

	if confirm=="yes":
		for i in range(9):
			butt[i].config(text=" ");

	elif confirm=="change":
		for i in range(9):
			butt[i].config(bg='gainsboro');
			butt[i].config(text=" ");


	click = True;


def escape(event):
        root.destroy()


# Start New Game
def NewGame():

	global butt;

	confirm = tkinter.messagebox.askquestion("confirm" , "Do You want to start new game");

	if confirm=="yes":
		ng = True
		Reset(ng,confirm);
		for i in range(9):
			butt[i].config(text=" ");

		global PlayerX;
		global PlayerO;
		PlayerX.set(0);
		PlayerO.set(0);



# Display winner msg and change colour of that combination
def Won(player):
	for i in range(3):
		butt[player[i+1]].config(bg="light pink"); 

	tkinter.messagebox.showinfo("Won" , "Congrats player '{}' won this match" .format(player[0]));
	Reset(True,"change");



# Calculate Score
def Score():

	global butt;
	p_won =["no"];


	# Check for diagonal (top-left to bottom-right)

	if butt[0]["text"] == butt[4]["text"] == butt[8]["text"] == "X":
			n = float(PlayerX.get());
			n_score = n+1;
			PlayerX.set(n_score);
			p_won = [ butt[0]["text"] , 0,4,8 ];

	elif butt[0]["text"] == butt[4]["text"] == butt[8]["text"] == "O":
			n = float(PlayerO.get());
			n_score = n+1;
			PlayerO.set(n_score);
			p_won = [ butt[0]["text"] , 0,4,8 ];


	# Check for diagonal (top-right to bottom-left)
	if(p_won[0] == "no"):

		if butt[2]["text"] == butt[4]["text"] == butt[6]["text"] == "X":
				n = float(PlayerX.get());
				n_score = n+1;
				PlayerX.set(n_score);
				p_won = [ butt[2]["text"] , 2,4,6 ];


		elif butt[2]["text"] == butt[4]["text"] == butt[6]["text"] == "O":
				n = float(PlayerO.get());
				n_score = n+1;
				PlayerO.set(n_score);
				p_won = [ butt[2]["text"] , 2,4,6 ];


	# Check for horizontal
	if(p_won[0] == "no"):

		for i in range(0,9,3):

			if butt[i]["text"] == butt[i+1]["text"] == butt[i+2]["text"] == "X":
				n = float(PlayerX.get());
				n_score = n+1;
				PlayerX.set(n_score);
				p_won = [ butt[i]["text"] , i , (i+1) , (i+2) ];

			elif butt[i]["text"] == butt[i+1]["text"] == butt[i+2]["text"] == "O":
				n = float(PlayerO.get());
				n_score = n+1;
				PlayerO.set(n_score);
				p_won = [ butt[i]["text"] , i , (i+1) , (i+2) ];


	# Check for verical
	if(p_won[0] == "no"):

		for i in range(0,3,1):

			if butt[i]["text"] == butt[i+3]["text"] == butt[i+6]["text"] == "X":
				n = float(PlayerX.get());
				n_score = n+1;
				PlayerX.set(n_score);
				p_won = [ butt[i]["text"] , i , (i+3) , (i+6) ];


			elif butt[i]["text"] == butt[i+3]["text"] == butt[i+6]["text"] == "O":
				n = float(PlayerO.get());
				n_score = n+1;
				PlayerO.set(n_score);
				p_won = [ butt[i]["text"] , i , (i+3) , (i+6) ];


	# Call Won function is any player won
	if (not(p_won[0]=="no")):
		Won(p_won);




btnReset = Button(RightFrame,text="Reset",font=('Times 29 bold'),height=1,width=16 , command=Reset);
btnReset.grid(row=0,column=0 , padx=6,pady=20);

btnNewGame = Button(RightFrame,text="New Game",font=('Times 29 bold'),height=1,width=16 , command=NewGame);
btnNewGame.grid(row=1,column=0 , padx=6,pady=20);


butt = [];

button1 = Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro' , command=lambda:checker(button1));
button1.grid(row=0,column=0 , sticky=S+N+E+W);
butt.append(button1);

button2 = Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro' , command=lambda:checker(button2));
button2.grid(row=0,column=1 , sticky=S+N+E+W);
butt.append(button2);

button3 = Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro' , command=lambda:checker(button3));
button3.grid(row=0,column=2 , sticky=S+N+E+W);
butt.append(button3);

button4 = Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro' , command=lambda:checker(button4));
button4.grid(row=1,column=0 , sticky=S+N+E+W);
butt.append(button4);

button5 = Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro' , command=lambda:checker(button5));
button5.grid(row=1,column=1 , sticky=S+N+E+W);
butt.append(button5);

button6 = Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro' , command=lambda:checker(button6));
button6.grid(row=1,column=2 , sticky=S+N+E+W);
butt.append(button6);

button7 = Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro' , command=lambda:checker(button7));
button7.grid(row=2,column=0 , sticky=S+N+E+W);
butt.append(button7);

button8 = Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro' , command=lambda:checker(button8));
button8.grid(row=2,column=1 , sticky=S+N+E+W);
butt.append(button8);

button9 = Button(LeftFrame,text=" ",font=('Times 26 bold'),height=3,width=8,bg='gainsboro' , command=lambda:checker(button9));
button9.grid(row=2,column=2 , sticky=S+N+E+W);
butt.append(button9);


root.bind("<Escape>",escape)

root.mainloop()
