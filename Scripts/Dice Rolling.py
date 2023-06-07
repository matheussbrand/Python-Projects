import tkinter
from PIL import Image, ImageTk
import random

# Top-level widget which represents the main window of an aplication
root = tkinter.Tk()
root.geometry('400x400')
root.title('Matheus Roll the Dice')

# Designing the buttons

# Add label into the frame
BlankLine = tkinter.Label(root, text="")    
BlankLine.pack()

# Add label with different font and formatting
HeadingLabel = tkinter.Label(root,text="Hi!",   
    fg = "light green",
        bg = "dark green",
        font="Helvetica 16 bold italic")
HeadingLabel.pack()

# Images
dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']

# Simulating the dice with random numbers and generating image
DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# Construct a label widget
ImageLabel = tkinter.Label(root, image=DiceImage)
ImageLabel.image = DiceImage

# Packing a widget
ImageLabel.pack(expand=True)

# Function activated by button
def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    ImageLabel.configure(image=DiceImage)   # Update Image
    ImageLabel.image = DiceImage    # Keep a reference
    
# Add button and command
button = tkinter.Button(root, text='Roll the dice', fg='blue', command=rolling_dice)

#Pack a widget
button.pack(expand=True)

root.mainloop()
