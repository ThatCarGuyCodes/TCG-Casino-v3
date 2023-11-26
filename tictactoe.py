from tkinter import *
from random import *
from time import *
import colorama
from colorama import Fore

window = Tk()
background = window.cget("background")
window.title("Tic Tac Toe")
window.configure(bg="#CA9BF7")
buttonMatrix=[]
winner =""
money = 10000
turn = False
powerUp1 = False
insurance = 1

def insurance1():
  global insurance, money
  if money > 300 and insurance > 0.8:
    money -= 300
    moneyLabel.config(text="$" + str(money))
    insurance = 0.8
    insuranceButton1.destroy()


def insurance2():
  global insurance, money
  if money > 900 and insurance > 0.7:
    money -= 900
    moneyLabel.config(text="$" + str(money))
    insurance = 0.7
    insuranceButton1.destroy()
    insuranceButton2.destroy()

def insurance3():
  global insurance, money
  if money > 2700 and insurance > 0.65:
    money -= 2700
    insurance = 0.6
    insuranceButton1.destroy()
    insuranceButton2.destroy()
    insuranceButton3.destroy()

def endGame(who):
  global money, buttonMatrix, background, turn, powerUp1, insurance
  if who == "p":
    if powerUp1 == True:
      powerUp1 = False
      money = int(round(2.5 * money, 0))
    else:    
      money = money + int(bet.get())
    turn = True
    result.config(text="You win!", highlightthickness=3, highlightbackground="#00FF00")
    
  elif who == "b":
    if powerUp1 == True:
      powerUp1 = False
      money = 10000
      window.destroy()
      import diceroller
      
    else:
      result.config(text="You lost!", highlightthickness=3, highlightbackground="#FF0000")
      money = money - int(insurance*(int(bet.get())))
      
    turn = False
    
  else:
    result.config(text="It's a draw! ", highlightthickness=3, highlightbackground="#FFFFFF")
    turn = True
    
  moneyLabel.config(text="$" + str(money))
  for i in range(3):
    for j in range(3):
      buttonMatrix[i][j]["text"] = ""
      buttonMatrix[i][j]["bg"] = background

    
def botMove():
  row = randint(0,2)
  col = randint(0,2)
  if buttonMatrix[row][col]["text"] == "": #checking if square is valid spot
    buttonMatrix[row][col]['text']="O" 
    buttonMatrix[row][col].config(bg="#CA9BF7")
    checkWinnerBot()
  else:
    count = 0
    for i in range(3):
      for j in range(3):
        if buttonMatrix[i][j]["text"] != "":
          count += 1

    if count == 9:
      endGame("tie")

    else:
      botMove()
    
def checkWinnerBot():
  global buttonMatrix, win
  for i in range(3):
    if buttonMatrix[i][0]['text'] == "O" and buttonMatrix[i][1]['text'] == "O" and buttonMatrix[i][0]['text'] == "O" and buttonMatrix[i][2]['text'] == "O" and buttonMatrix[i][0]['text'] !="":#check horizontal
      winner = buttonMatrix[i][0]['text']
      endGame("b")
      return
      
    elif buttonMatrix[0][i]["text"] == "O" and buttonMatrix[1][i]["text"] == "O" and buttonMatrix[0][i]["text"] == "O" and buttonMatrix[2][i]["text"] == "O" and buttonMatrix[0][i]["text"] != "": #check vertical
      winner = buttonMatrix[i][0]["text"]
      endGame("b")
      return

    elif buttonMatrix[0][2]["text"] == "O" and buttonMatrix[1][1]["text"] == "O" and buttonMatrix[0][2]["text"] == "O" and buttonMatrix[2][0]["text"] == "O" and buttonMatrix[0][2]["text"] != "":# check diag right to left corner
      winner = buttonMatrix[0][2]["text"]
      endGame("b")
      return

    elif buttonMatrix[0][0]["text"] == "O" and buttonMatrix[1][1]["text"] == "O" and buttonMatrix[0][0]["text"] == "O" and buttonMatrix[2][2]["text"] == "O" and buttonMatrix[0][0]["text"] != "":#check diag left to right corner
      winner = buttonMatrix[0][0]["text"]
      print(winner + " diag l to r corner")
      endGame("b")
      return
      
    else:
      count = 0
      for i in range(3):
        for j in range(3):
          if buttonMatrix[i][j]["text"] != "":
            count += 1

      if count == 9:
        endGame("tie")
    
def checkWinnerPlayer():
  global buttonMatrix, winner
  for i in range(3):
    if buttonMatrix[i][0]['text'] == "X" and buttonMatrix[i][1]['text'] == "X" and buttonMatrix[i][0]['text'] == "X" and buttonMatrix[i][2]['text'] == "X" and buttonMatrix[i][0]['text'] !="":#check horizontal
      winner = buttonMatrix[i][0]['text']
      endGame("p")
      return
      
    elif buttonMatrix[0][i]["text"] == "X" and buttonMatrix[1][i]["text"] == "X" and buttonMatrix[0][i]["text"] == "X" and buttonMatrix[2][i]["text"] == "X" and buttonMatrix[0][i]["text"] != "": #check vertical
      winner = buttonMatrix[i][0]["text"]
      endGame("p")
      return

    elif buttonMatrix[0][2]["text"] == "X" and buttonMatrix[1][1]["text"] == "X" and buttonMatrix[0][2]["text"] == "X" and buttonMatrix[2][0]["text"] == "X" and buttonMatrix[0][2]["text"] != "":# check diag right to left corner
      winner = buttonMatrix[0][2]["text"]
      endGame("p")
      return

    elif buttonMatrix[0][0]["text"] == "X" and buttonMatrix[1][1]["text"] == "X" and buttonMatrix[0][0]["text"] == "X" and buttonMatrix[2][2]["text"] == "X" and buttonMatrix[0][0]["text"] != "":#check diag left to right corner
      winner = buttonMatrix[0][0]["text"]
      endGame("p")
      return

    else:
      count = 0
      for i in range(3):
        for j in range(3):
          if buttonMatrix[i][j]["text"] != "":
            count += 1

      if count == 9:
        endGame("tie")
    

def click(row, col):
  global buttonMatrix, turn
  if int(bet.get()) <= money:
    if buttonMatrix[row][col]['text'] == "":
      buttonMatrix[row][col]['text'] = "X"
      buttonMatrix[row][col].config(bg='#F3C2C2')
      checkWinnerPlayer()
      if turn == True:
        turn = False
      else:
          botMove()  
  else:
    print(Fore.RED + "You are betting too much!!! Try a lower value")

for i in range(3):
  buttonRow=[]
  for j in range(3):
      button = Button(window, height=4, width=8, font="Times 20 bold", command=lambda row =i, col=j: click(row, col))
      buttonRow.append(button)
      button.grid(row=i, column=j)
  buttonMatrix.append(buttonRow)

bet = Entry(window)
bet.grid(row=3, column = 1)
text = Label(window, text="How much will you bet?", font=("Arial", 8, "normal"), bg="#CA9BF7", fg="#FEFEFA")
text.grid(row=3, column=0)

moneyLabel = Label(window, text="$" + str(money), font=("Arial", 8, "normal"), bg="#CA9BF7")
moneyLabel.grid(row=3, column=2)

result = Label(window)
result.grid(row=4, column=0)
result.config(bg="#CA9BF7", fg="#FEFEFA")

def prestige():
  global money
  if money >= 10000:
    window.destroy()
    import coinflipper
    
def double():
  global powerUp1, money
  powerUp1 = True
  money -= 5000
  moneyLabel.config(text="$" + str(money))
  powerUp.destroy()

def strikeThrough(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result
powerUp = Button(window, text="$5000: 2.5x or Restart", command=double, font=("Arial", 9, "normal"), bg="#CA9BF7", fg="#FFFFFF")
powerUp.grid(row=4, column=1, columnspan=2)

insuranceButton1 = Button(window, text="Purchase Insurance 1 for $300", command=insurance1)
insuranceButton1.grid(row=5, column=1, columnspan=2)
insuranceButton1.config(bg="#89CFF0", fg="#FEFEFA")

insuranceButton2 = Button(window,text="Purchase Insurance 2 for $900",command=insurance2)
insuranceButton2.grid(row=6, column=1, columnspan=2)
insuranceButton2.config(bg="#89CFF0", fg="#FEFEFA")

insuranceButton3 = Button(window,text="Purchase Insurance 3 for $2700", command=insurance3)
insuranceButton3.grid(row=7, column=1, columnspan=2)
insuranceButton3.config(bg="#89CFF0", fg="#FEFEFA")

prestigeButton = Button(window, text="$10,000: Prestige to the Coin Flipper game", command=prestige)
prestigeButton.grid(row=8, column=1, columnspan=2)
prestigeButton.config(bg="#52faec", fg="#FEFEFA")
