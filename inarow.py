#Tao cua so game
from tkinter import *
from tkinter import messagebox
ctn=0
window=Tk()
window.title("Tic Tac Toe")
window.geometry("500x550")

#Cho nguoi dung nhapp thong tin
pA=StringVar()
pB=StringVar()

p1=StringVar()
label=Label(window,text="Player 1",font='Times 15 bold',bg="white", fg="black")
label.grid(row=12, column=0)

p2=StringVar()
label=Label(window,text="Player 2",font='Times 15 bold',bg="white", fg="black")
label.grid(row=12, column=3)


player1_name=Entry(window,textvariable=p1, bd=5)
player1_name.grid(row=13, column=0, columnspan=2)

player2_name=Entry(window,textvariable=p2, bd=5)
player2_name.grid(row=13, column=3, columnspan=6)

#Gan 25 box= gia tri X hoac O
box1="1"
box2="2"
box3="3"
box4="4"
box5="5"
box6="6"
box7="7"
box8="8"
box9="9"
box10="10"
box11="11"
box12="12"
box13="13"
box14="14"
box15="15"
box16="16"
box17="17"
box18="18"
box19="19"
box20="20"
box21="21"
box22="22"
box23="23"
box24="24"
box25="25"

#tao 25 button
btn1=Button(window,text=" ",bg="yellow",fg="green",font="Times 10 bold",command=lambda:activate(1))
btn1.grid(row=0,column=0, ipadx=40,ipady=30)

btn2=Button(window,text=" ",bg="yellow",fg="green",font="Times 10 bold",command=lambda:activate(2))
btn2.grid(row=0,column=1, ipadx=40,ipady=30)

btn3=Button(window,text=" ",bg="yellow",fg="green",font="Times 10 bold",command=lambda:activate(3))
btn3.grid(row=0,column=2, ipadx=40,ipady=30)

btn4=Button(window,text=" ",bg="yellow",fg="green",font="Times 10 bold",command=lambda:activate(4))
btn4.grid(row=0,column=3, ipadx=40,ipady=30)

btn5=Button(window,text=" ",bg="yellow",fg="green",font="Times 10 bold",command=lambda:activate(5))
btn5.grid(row=0,column=4, ipadx=40,ipady=30)

btn6=Button(window,text=" ",bg="yellow",fg="green",font="Times 10 bold",command=lambda:activate(6))
btn6.grid(row=1,column=0, ipadx=40,ipady=30)

btn7=Button(window,text=" ",bg="yellow",fg="green",font="Times 10 bold",command=lambda: activate(7))
btn7.grid(row=1,column=1, ipadx=40,ipady=30)

btn8=Button(window,text=" ",bg="yellow",fg="green",font="Times 10 bold",command=lambda: activate(8))
btn8.grid(row=1,column=2, ipadx=40,ipady=30)

btn9=Button(window,text=" ",bg="yellow",fg="green",font="Times 10 bold",command=lambda: activate(9))
btn9.grid(row=1,column=3, ipadx=40,ipady=30)

btn10=Button(window, text=" ",bg="yellow",fg="green",font="Times 10 bold",command=lambda: activate(10))
btn10.grid(row=1,column=4, ipadx=40,ipady=30)

btn11=Button(window, text=" ",bg="yellow",fg="green",font="Times 10 bold",command=lambda: activate(11))
btn11.grid(row=2,column=0, ipadx=40,ipady=30)

btn12=Button(window, text=" ",bg="yellow",fg="green",font="Times 10 bold",command=lambda: activate(12))
btn12.grid(row=2,column=1, ipadx=40,ipady=30)

btn13=Button(window, text=" ",bg="yellow",fg="green",font="Times 10 bold",command=lambda: activate(13))
btn13.grid(row=2,column=2, ipadx=40,ipady=30)

btn14=Button(window, text=" ",bg="yellow",fg="green",font="Times 10 bold",command=lambda: activate(14))
btn14.grid(row=2,column=3, ipadx=40,ipady=30)

btn15=Button(window, text=" ",bg="yellow",fg="green",font="Times 10 bold",command=lambda: activate(15))
btn15.grid(row=2,column=4, ipadx=40,ipady=30)

btn16=Button(window, text=" ",bg="yellow",fg="green",font="Times 10 bold",command=lambda: activate(16))
btn16.grid(row=3,column=0, ipadx=40,ipady=30)

btn17=Button(window, text=" ",bg="yellow",fg="green",font="Times 10 bold",command=lambda: activate(17))
btn17.grid(row=3,column=1, ipadx=40,ipady=30)

btn18=Button(window, text=" ",bg="yellow",fg="green",font="Times 10 bold",command=lambda: activate(18))
btn18.grid(row=3,column=2, ipadx=40,ipady=30)

btn19=Button(window, text=" ",bg="yellow",fg="green",font="Times 10 bold",command=lambda: activate(19))
btn19.grid(row=3,column=3, ipadx=40,ipady=30)

btn20=Button(window, text=" ",bg="yellow",fg="green",font="Times 10 bold",command=lambda: activate(20))
btn20.grid(row=3,column=4, ipadx=40,ipady=30)

btn21=Button(window, text=" ",bg="yellow",fg="green",font="Times 10 bold",command=lambda: activate(21))
btn21.grid(row=4,column=0, ipadx=40,ipady=30)

btn22=Button(window, text=" ",bg="yellow",fg="green",font="Times 10 bold",command=lambda: activate(22))
btn22.grid(row=4,column=1, ipadx=40,ipady=30)

btn23=Button(window, text=" ",bg="yellow",fg="green",font="Times 10 bold",command=lambda: activate(23))
btn23.grid(row=4,column=2, ipadx=40,ipady=30)

btn24=Button(window, text=" ",bg="yellow",fg="green",font="Times 10 bold",command=lambda: activate(24))
btn24.grid(row=4,column=3, ipadx=40,ipady=30)

btn25=Button(window, text=" ",bg="yellow",fg="green",font="Times 10 bold",command=lambda: activate(25))
btn25.grid(row=4,column=4, ipadx=40,ipady=30)


#Khai bao bien cho toan bo truong trinh
player=1
def activate(box):
    global player
    global pA
    global pB
    global player1_name
    global player2_name
    global ctn
    global box1
    global box2
    global box3
    global box4
    global box5
    global box6
    global box7
    global box8
    global box9
    global box10
    global box11
    global box12
    global box13
    global box14
    global box15
    global box16
    global box17
    global box18
    global box19
    global box20
    global box21
    global box22
    global box23
    global box24
    global box25

    ctn =ctn + 1

    #Nhap X hoac O
    if box==1 and player ==1:
        btn1.config(text="O",fg="black")
        player =2
        box1="O"
    elif box==1 and player ==2:
        btn1.config(text="X")
        player= 1
        box1="X"
    elif box==2 and player ==1:
        btn2.config(text="O",fg="black")
        player= 2
        box2="O"
    elif box==2 and player ==2:
        btn2.config(text="X")
        player= 1
        box2="X"

    elif box==3 and player ==1:
        btn3.config(text="O",fg="black")
        player= 2
        box3="O"
    elif box==3 and player ==2:
        btn3.config(text="X")
        player= 1
        box3="X"

    elif box==4 and player ==1:
        btn4.config(text="O",fg="black")
        player= 2
        box1="O"
    elif box==4 and player ==2:
        btn4.config(text="X")
        player= 1
        box1="X"

    elif box==5 and player ==1:
        btn5.config(text="O",fg="black")
        player= 2
        box5="O"
    elif box==5 and player ==2:
        btn5.config(text="X")
        player= 1
        box5="X"

    elif box==6 and player ==1:
        btn6.config(text="O",fg="black")
        player= 2
        box6="O"
    elif box==6 and player ==2:
        btn6.config(text="X")
        player= 1
        box6="X"

    elif box==7 and player ==1:
        btn7.config(text="O",fg="black")
        player= 2
        box7="O"
    elif box==7 and player ==2:
        btn7.config(text="X")
        player= 1
        box7="X"

    elif box==8 and player ==1:
        btn8.config(text="O",fg="black")
        player= 2
        box8="O"
    elif box==8 and player ==2:
        btn8.config(text="X")
        player= 1
        box8="X"

    elif box==9 and player ==1:
        btn9.config(text="O",fg="black")
        player= 2
        box9="O"
    elif box==9 and player ==2:
        btn9.config(text="X")
        player= 1
        box9="X"

    elif box==10 and player ==1:
        btn10.config(text="O",fg="black")
        player= 2
        box10="O"
    elif box==10 and player ==2:
        btn10.config(text="X")
        player= 1
        box10="X"

    elif box==11 and player ==1:
        btn11.config(text="O",fg="black")
        player= 2
        box11="O"
    elif box==11 and player ==2:
        btn11.config(text="X")
        player= 1
        box11="X"

    elif box==12 and player ==1:
        btn12.config(text="O",fg="black")
        player= 2
        box12="O"
    elif box==12 and player ==2:
        btn12.config(text="X")
        player= 1
        box12="X"

    elif box==13 and player ==1:
        btn13.config(text="O",fg="black")
        player= 2
        box13="O"
    elif box==13 and player ==2:
        btn13.config(text="X")
        player= 1
        box13="X"

    elif box==14 and player ==1:
        btn14.config(text="O",fg="black")
        player= 2
        box14="O"
    elif box==14 and player ==2:
        btn14.config(text="X")
        player= 1
        box14="X"

    elif box==15 and player ==1:
        btn15.config(text="O",fg="black")
        player= 2
        box15="O"
    elif box==15 and player ==2:
        btn15.config(text="X")
        player= 1
        box15="X"

    elif box==16 and player ==1:
        btn16.config(text="O",fg="black")
        player= 2
        box16="O"
    elif box==16 and player ==2:
        btn16.config(text="X")
        player= 1
        box16="X"

    elif box==17 and player ==1:
        btn17.config(text="O",fg="black")
        player= 2
        box17="O"
    elif box==17 and player ==2:
        btn17.config(text="X")
        player= 1
        box17="X"

    elif box==18 and player ==1:
        btn18.config(text="O",fg="black")
        player= 2
        box18="O"
    elif box==18 and player ==2:
        btn18.config(text="X")
        player= 1
        box18="X"

    elif box==19 and player ==1:
        btn19.config(text="O",fg="black")
        player= 2
        box19="O"
    elif box==19 and player ==2:
        btn19.config(text="X")
        player= 1
        box19="X"

    elif box==20 and player ==2:
        btn20.config(text="O",fg="black")
        player= 2
        box20="O"
    elif box==10 and player ==1:
        btn20.config(text="X")
        player= 1
        box20="X"

    elif box==21 and player ==1:
        btn21.config(text="O",fg="black")
        player= 2
        box21="O"
    elif box==21 and player ==2:
        btn21.config(text="X")
        player= 1
        box21="X"

    elif box==22 and player ==1:
        btn22.config(text="O",fg="black")
        player= 2
        box22="O"
    elif box==22 and player ==2:
        btn22.config(text="X")
        player= 1
        box22="X"

    elif box==23 and player ==1:
        btn23.config(text="O",fg="black")
        player= 2
        box23="O"
    elif box==23 and player ==2:
        btn23.config(text="X")
        player= 1
        box23="X"

    elif box==24 and player ==1:
        btn24.config(text="O",fg="black")
        player= 2
        box24="O"
    elif box==24 and player ==2:
        btn24.config(text="X")
        player= 1
        box24="X"

    elif box==25 and player ==1:
        btn25.config(text="O",fg="black")
        player= 2
        box25="O"
    elif box==25 and player ==2:
        btn25.config(text="X")
        player= 1
        box25="X"


# Dieu kien thang
    if box1==box7==box13==box19==box25=="O" or box21==box17==box13==box9==box5=="O":
        pA = p1.get()
        messagebox._show("Game end","player:" +pA + " " + " win")
        exit(0)

    elif box1==box2==box3==box4==box5=="O" or box6==box7==box8==box9==box10=="O" or box11==box12==box13==box14==box15=="O" or box16==box17==box18==box19==box20=="O" or box21==box22==box23==box24==box25=="O":
        pA = p1.get()
        messagebox._show("Game end", "player:" + pA + " " + " win")
        exit(0)

    elif box1==box6==box11==box16==box21=="O" or box2==box7==box12==box17==box22=="O" or box3==box8==box13==box18==box23=="O" or box4==box9==box14==box19==box24=="O" or box5==box10==box15==box20==box25=="O":
        pA = p1.get()
        messagebox._show("Game end", "player:" + pA + " " + " win")
        exit(0)


    elif box1==box7==box13==box19==box25=="X" or box21==box17==box13==box9==box5=="X" or box1==box2==box3==box4==box5=="X" or box6==box7==box8==box9==box10=="X" or box11==box12==box13==box14==box15=="X" or box16==box17==box18==box19==box20=="X" or box21==box22==box23==box24==box25=="X" or box1==box6==box11==box16==box21=="X" or box2==box7==box12==box17==box22=="X" or box3==box8==box13==box18==box23=="X" or box4==box9==box14==box19==box24=="X" or box5==box10==box15==box20==box25=="X" :
        pB=p2.get()
        messagebox._show("Game end","player:" + pB + " " + " win")
        exit(0)
    elif ctn==25:
        messagebox._show("Draw","End game")

#Exit button
def quit():
    exit()
label=Label(window,text="END THE GAME",bg="black",fg="white",font='none 8 bold').grid(row=17,column=2)
Button(window,text="EXIT",width=10,bg="red",fg="white",font='none 10 bold',command=quit).grid(row=18,column=2)

window.mainloop()