from tkinter import*
from random import*
from os import *
import unicodedata

#system("clear")
window = Tk()
window.title("Coin Flipper")
window.geometry("500x500")
window.config(bg="#8CFF9E")

coin = 0
money = 10000
coinluck = 5
insurance = 1

moneyLabel = Label(window, text="$"+str(money), bg="#8CFF9E")
moneyLabel.pack()#, pady=1)

coinbetBox = Entry(window, font=("Impact", 20))
coinbetBox.pack()

def insurance1():
  global insurance, money
  if money > 200 and insurance > 0.8:
    money -= 200
    moneyLabel.config(text="$"+str(money))
    insurance = 0.8
    coinInsuranceButton1.pack_forget()
    

def insurance2():
  global insurance, money
  if money > 400 and insurance > 0.7:
    money -= 400
    moneyLabel.config(text="$"+str(money))
    insurance = 0.7
    coinInsuranceButton1.pack_forget()
    coinInsuranceButton2.pack_forget()
    
def insurance3():
  global insurance, money
  if money > 800 and insurance > 0.65:
    money -= 800
    moneyLabel.config(text="$"+str(money))
    insurance = 0.65
    coinInsuranceButton1.pack_forget()
    coinInsuranceButton2.pack_forget()
    coinInsuranceButton3.pack_forget()

def coinluck1():
  global coinluck, money
  if money >= 300 and coinluck < 6:
    money-=300
    moneyLabel.config(text="$"+str(money))
    coinluck = 6
    coinluckbutton1.pack_forget()

def coinluck2():
  global coinluck, money
  if money >= 900 and coinluck< 7:
    money-=900
    moneyLabel.config(text="$"+str(money))
    coinluck = 7
    coinluckbutton1.pack_forget()
    coinluckbutton2.pack_forget()

def coinluck3():
  global coinluck, money
  if money >= 2700 and coinluck< 8:
    money-=2700
    moneyLabel.config(text="$"+str(money))
    coinluck = 8
    coinluckbutton1.pack_forget()
    coinluckbutton2.pack_forget()
    coinluckbutton3.pack_forget()

def show1():
  global coin, money, luck, insurance
  if coinbetBox.get() != "" and money >= int(coinbetBox.get()):
    x = randint(0,9)
    if x < coinluck:
      coin = 1
    if x > coinluck:
      coin = 0
    if coin == 1:
      coinshowArea.config(text=chr(9675), font=("Impact", 50, "bold"))
      coinresult.config(text="You win!", font=("Impact", 40))
      money += int(coinbetBox.get())
    if coin == 0: 
      coinshowArea.config(text=chr(9676), font=("Impact", 50, "normal"))
      coinresult.configure(text="You lose!", font=("Impact", 40))
      money -= int(int(coinbetBox.get()) * insurance)
    moneyLabel.config(text="$"+str(money))
    coinbetBox.delete(0, END)

coinbutton1 = Button(window, text="Roll", command=show1)
coinbutton1.pack()
coinbutton1.config(bg="#8CFF9E", fg="#FEFEFA")

coinshowArea = Label(window)
coinshowArea.config(bg="#8CFF9E", fg="#FEFEFA", width=50)
coinshowArea.pack()

coinresult = Label(window)
coinresult.pack()
coinresult.config(bg="#8CFF9E", fg="#FEFEFA")

coinluckbutton1 = Button(window, text="Purchase Luck 1 for $300", command = coinluck1)
coinluckbutton1.pack()
coinluckbutton1.config(bg="#8CFF9E", fg="#FEFEFA")

coinluckbutton2 = Button(window, text="Purchase Luck 2 for $900", command = coinluck2)
coinluckbutton2.pack()
coinluckbutton2.config(bg="#8CFF9E", fg="#FEFEFA")

coinluckbutton3 = Button(window, text="Purchase Luck 3 for $2700", command = coinluck3)
coinluckbutton3.pack()
coinluckbutton3.config(bg="#8CFF9E", fg="#FEFEFA")

coinInsuranceButton1 = Button(window, text="Purchase Insurance 1 for $200", command = insurance1)
coinInsuranceButton1.pack()
coinInsuranceButton1.config(bg="#8CFF9E", fg="#FEFEFA")

coinInsuranceButton2 = Button(window, text="Purchase Insurance 2 for $400", command = insurance2)
coinInsuranceButton2.pack()
coinInsuranceButton2.config(bg="#8CFF9E", fg="#FEFEFA")

coinInsuranceButton3 = Button(window, text="Purchase Insurance 3 for $800", command = insurance3)
coinInsuranceButton3.pack()
coinInsuranceButton3.config(bg="#8CFF9E", fg="#FEFEFA")

def prestige():
  global money
  if money >= 10000:
    window.destroy()
    import football

prestigeButton = Button(window, text="Prestige to the Football game for $10,000", command=prestige)
prestigeButton.pack()
prestigeButton.config(bg="#89CFF0", fg="#FEFEFA")
