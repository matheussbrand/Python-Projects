from tkinter import *
import random

# Creating a window frame
root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Matheus Game - Rock Paper Scissors')
root.config(bg='ghost white')

Label(root, text='Rock, Papper, Scissors', font='arial 20 bold', bg='ghost white').pack()

# User Choice
user_take = StringVar()
Label(root, text='choose any one: rock, paper, scissors', font='arial 15 bold', bg='ghost white').place(x=20, y=70)
Entry(root, font='arial 15', textvariable=user_take, bg='ghost white').place(x=90, y=130)

# Computer Choice
comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick == 2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'
    
# Start Game
Result = StringVar()

def play():
    user_pick = user_take.get()
    if user_take == comp_pick:
        Result.set('Tie!')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('You loose!')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('You Win!')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('You loose!')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('You Win!')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('You loose!')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('You Win!')
    else:
        Result.set('invalid: choose any one')
        
# Reset Game
def Reset():
    Result.set("")
    user_take.set("")
    
# Exit Game
def Exit():
    root.destroy()
    

# Buttons
Entry(root, font='arial 10 bold', textvariable=Result, bg='ghost white', width= 50).place(x=25, y=250)

Button(root, font='arial 13 bold', text='PLAY', padx=5, bg='ghost white', command=play).place(x=150, y=190)
Button(root, font='arial 13 bold', text='Reset', padx=5, bg='ghost white', command=Reset).place(x=70, y=310)
Button(root, font='arial 13 bold', text='Exit', padx=5, bg='ghost white', command=Exit).place(x=230, y=310)

root.mainloop()