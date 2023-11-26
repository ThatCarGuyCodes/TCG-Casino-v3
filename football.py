from tkinter import*
from random import*
from os import *

#system("clear")
window = Tk()
window.title("Football Game")
window.geometry("500x500")
window.config(bg="#F4C2C2")

footballcolors=["royalblue", "teal", "navy", "green", "purple", "orangered", "orangered", "silver", "navy", "royalblue", "gold", "navy", "orangered", "firebrick", "silver", "gold", "navy", "royalblue", "silver", "maroon", "orangered", "powderblue", "forestgreen", "gold", "maroon", "powderblue", "gold", "firebrick", "maroon", "navy", "firebrick", "navy"]

money = 10000
insurance = 1
T2 = False
p1 = 0 
p2 = 0
wlist= []
llist = []
tlist = []
wltlist = []
footballteams = [
"Buffalo Bills",
"Miami Dolphins",
"New England Patriots",
"New York Jets",
"Baltimore Ravens",
"Cincinnati Bengals",
"Cleveland Browns",
"Pittsburgh Steelers",
"Houston Texans",
"Indianapolis Colts",
"Jacksonville Jaguars",
"Tennessee Titans",
"Denver Broncos",
"Kansas City Chiefs",
"Las Vegas Raiders",
"Los Angeles Chargers",

"Dallas Cowboys",
"New York Giants",
"Philadelphia Eagles",
"Washington Commanders",
"Chicago Bears",
"Detroit Lions",
"Green Bay Packers",
"Minnesota Vikings",
"Atlanta Falcons",
"Carolina Panthers",
"New Orleans Saints",
"Tampa Bay Buccaneers",
"Arizona Cardinals",
"Los Angeles Rams",
"San Francisco 49ers",
"Seattle Seahawks"]

moneyLabel = Label(window, text="$"+str(money), bg="#F4C2C2")
moneyLabel.pack()#, pady=1)

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

for i in range(32):
  w = randint(0,15)
  l = randint(0, (15-w))
  t = 15-w-l
  wlist.append(w)
  llist.append(l)
  tlist.append(t)
  wlt = str(w)+"-"+str(l)+"-"+str(t)
  wltlist.append(wlt)

#print(wltlist)

def T1():
  global t2
  t2 = False

def T2():
  global t2
  t2 = True

def gen():
  global p1, p2
  #if p1 = True or p2 = True
  winner.pack_forget()
  play.pack_forget()
  #footballbetBox.pack_forget()
  p1 = randint(0,31)
  p2 = randint(0,31)
  if p1 == p2:
    p2 = randint(0,31)
  players.config(text=footballteams[p1] + " vs " + footballteams[p2])
  b1.config(text="Bet: " + footballteams[p1], command=T1, bg=footballcolors[p1])
  b1.pack()
  b2.config(text="Bet: " + footballteams[p2], command=T2, bg=footballcolors[p2])
  b2.pack()
  players.pack()
  footballbetBox.pack()
  play.pack()

def best():
  global p1, p2, t2, money
  bet = (footballbetBox.get())
  if bet.isnumeric():
    bet = int(footballbetBox.get())
    if bet < money: 
      warn.config(text="")
      c1 = wlist[p1]-llist[p1]
      c2 = wlist[p2]-llist[p2]
      c = abs(c1-c2)
      x = randint(0,c)
      if x == 0:
        if c1 > c2:
          winner.config(text="The " + footballteams[p2] + " have won")
          winner.pack()
          win = p2
        if c2 > c1:
          winner.config(text="The " + footballteams[p1] + " have won")
          winner.pack()
          win = p1
      if x > 0:
        if c1 > c2:
          winner.config(text="The " + footballteams[p1] + " have won")
          winner.pack()
          win = p1
        if c2 > c1:
          winner.config(text="The " + footballteams[p2] + " have won")
          winner.pack()
          win = p2
      if t2 == False:
        if win == p1:
          money += bet
        if win == p2:
          money -= bet
      if t2 == True:
        if win == p1:
          money -= bet
        if win == p2:
          money += bet
      moneyLabel.config(text="$"+str(money))
    else:
      warn.config(text="You don't have enough money")
      warn.pack()
  else:
    warn.config(text="Enter a bet")
    warn.pack()

insuranceButton1 = Button(window, text="Purchase Insurance 1 for $300", command=insurance1)
insuranceButton1.pack()
insuranceButton1.config(bg="#89CFF0", fg="#FEFEFA")

insuranceButton2 = Button(window,text="Purchase Insurance 2 for $900",command=insurance2)
insuranceButton2.pack()
insuranceButton2.config(bg="#89CFF0", fg="#FEFEFA")

insuranceButton3 = Button(window,text="Purchase Insurance 3 for $2700",command=insurance3)
insuranceButton3.pack()
insuranceButton3.config(bg="#89CFF0", fg="#FEFEFA")

footballbetBox = Entry(window, font=("Impact", 20))
footballbetBox.pack()
generate = Button(window, text="Generate teams", command= gen)
generate.pack()
players = Label(window)
players.pack()
b1 = Button(window)
b2 = Button(window)
winner = Label(window)
play = Button(window, text="Play match", command=best, bg="#90ee90")
warn = Label(window)
