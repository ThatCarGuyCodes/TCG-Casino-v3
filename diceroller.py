from tkinter import *
from random import *
from os import *

#system("clear")
window = Tk()
window.title("Dice Roller")
window.geometry("500x500")
window.config(bg="#89CFF0")

faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
dicen1 = 0
dicen2 = 0

money = 10000
diceluck = 0

insurance = 1

moneyLabel = Label(window, text="$" + str(money), bg="#89CFF0")
moneyLabel.pack()  #, pady=1)

dicebetBox = Entry(window, font=("Impact", 20))
dicebetBox.pack()


def insurance1():
  global insurance, money
  if money > 300 and insurance > 0.8:
    money -= 300
    moneyLabel.config(text="$" + str(money))
    insurance = 0.8
    insuranceButton1.pack_forget()


def insurance2():
  global insurance, money
  if money > 900 and insurance > 0.7:
    money -= 900
    moneyLabel.config(text="$" + str(money))
    insurance = 0.7
    insuranceButton1.pack_forget()
    insuranceButton2.pack_forget()


def insurance3():
  global insurance, money
  if money > 2700 and insurance > 0.65:
    money -= 2700
    moneyLabel.config(text="$" + str(money))
    insurance = 0.65
    insuranceButton1.pack_forget()
    insuranceButton2.pack_forget()
    insuranceButton3.pack_forget()


def diceluck1():
  global diceluck, money
  if money >= 400 and diceluck < 1:
    money -= 1600
    moneyLabel.config(text="$" + str(money))
    diceluck = 1
    diceluckbutton1.pack_forget()


def diceluck2():
  global diceluck, money
  if money >= 1600 and diceluck < 2:
    money -= 1600
    moneyLabel.config(text="$" + str(money))
    diceluck = 2
    diceluckbutton1.pack_forget()
    diceluckbutton2.pack_forget()


def diceluck3():
  global diceluck, money
  if money >= 6400 and diceluck < 3:
    money -= 6400
    moneyLabel.config(text="$" + str(money))
    diceluck = 3
    diceluckbutton1.pack_forget()
    diceluckbutton2.pack_forget()
    diceluckbutton3.pack_forget()


def show1():
  global dicen1, dicen2, luck, diceluck
  x = randint(0, 11)
  if dicebetBox.get() != "" and money >= int(dicebetBox.get()): #lets test
    dicen1 = randint(diceluck, 5)
    dicen2 = randint(diceluck, 5)
    diceshowArea1.config(text=faces[dicen1] + " " + faces[dicen2], font=("Impact", 50, "bold"))
    show2()


def show2():
  global dicen1, dicen2, money, bet, insurance
  dicen3 = randint(0, 5)
  dicen4 = randint(0, 5)
  diceshowArea2.config(text=faces[dicen3] + " " + faces[dicen4], font=("Impact", 50, "bold"))
  if dicen1 + dicen2 > dicen3 + dicen4:
    diceresult.config(text="You win!", font=("Impact", 40))
    money += int(dicebetBox.get())
    moneyLabel.configure(text="$" + str(money))
  if dicen3 + dicen4 > dicen1 + dicen2:
    diceresult.configure(text="You lose!", font=("Impact", 40))
    money -= int(int(dicebetBox.get()) * insurance)
    moneyLabel.config(text="$" + str(money))
  if dicen1 + dicen2 == dicen3 + dicen4:
    diceresult.config(text="Draw!")
  dicebetBox.delete(0, END)
  testmoney.pack()


def freemoney():
  global money
  money += 10000
  moneyLabel.config(text="$" + str(money))
  testmoney.pack_forget()

def prestige():
  global money
  if money >= 10000:
    window.destroy()
    import tictactoe

dicebutton1 = Button(window, text="Roll", command=show1, bg="#56f573")
dicebutton1.pack()
diceshowArea1 = Label(window)
diceshowArea1.config(bg="#89CFF0", fg="#FEFEFA", width=50)
diceshowArea1.pack()

diceshowArea2 = Label(window)
diceshowArea2.config(bg="#89CFF0", fg="#FEFEFA", width=50)
diceshowArea2.pack()

diceresult = Label(window)
diceresult.config(bg="#89CFF0", fg="#FEFEFA")
diceresult.pack()

diceluckbutton1 = Button(window, text="Purchase Luck 1 for $400",command=diceluck1)
diceluckbutton1.pack()
diceluckbutton1.config(bg="#89CFF0", fg="#FEFEFA")

diceluckbutton2 = Button(window,text="Purchase Luck 2 for $1600",command=diceluck2)
diceluckbutton2.pack()
diceluckbutton2.config(bg="#89CFF0", fg="#FEFEFA")

diceluckbutton3 = Button(window, text="Purchase Luck 3 for $6400",command=diceluck3)
diceluckbutton3.pack()
diceluckbutton3.config(bg="#89CFF0", fg="#FEFEFA")

insuranceButton1 = Button(window, text="Purchase Insurance 1 for $300", command=insurance1)
insuranceButton1.pack()
insuranceButton1.config(bg="#89CFF0", fg="#FEFEFA")

insuranceButton2 = Button(window,text="Purchase Insurance 2 for $900",command=insurance2)
insuranceButton2.pack()
insuranceButton2.config(bg="#89CFF0", fg="#FEFEFA")

insuranceButton3 = Button(window,text="Purchase Insurance 3 for $2700",command=insurance3)
insuranceButton3.pack()
insuranceButton3.config(bg="#89CFF0", fg="#FEFEFA")

testmoney = Button(window, text="fReE mOnEy No ScAm", command=freemoney)

diceprestigeButton = Button(window, text="Prestige to the TicTacToe game for $10,000", command=prestige)
diceprestigeButton.pack()
diceprestigeButton.config(bg="#ffd278", fg="#FEFEFA")
