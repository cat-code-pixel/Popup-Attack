from tkinter import *
from tkinter.ttk import *
import random

delete = False

master = Tk()

master.title("Buy now!")
master.geometry("200x200")
master.resizable(False, False)

# Keep count of how many windows are opened
count = 0

# A bunch of stupid messages that appear on the windows
TMessages = ["Get free health insurance!",
         "More down payments!",
         "I have crippling depression! uwu",
         "Buy now before it's gone!",
         "Never gonna give you up!",
         "BUY MORE BUY MORE!!",
         "Error_$(Trace_Callback)",
         "Get the 2 for 1 deal at Taco Bell",
         "Free diarrhea pills!",
         "How to stop crying, click now!",
         "Our website isn't illegal, we swear!",
         "Who? Asked.",
         "Buy now! Or else.",
         "Extra money for free!",
         "Make money in 3 days!",
         "Why I still live in moms basement",
         "Free NFTS",
         "Free Bitcoin, click now!"]

BMessages = ["CLICK HERE NOW",
            "GET FOR FREE",
            "THATS SUSSY",
            "ok.",
            "BUY NOW",
            "BUY BEFORE IT RUNS OUT"]

# Make each new window spawn in a new location on the screen
def randomWindowPos(window):
    X = random.randint(0, 1300)
    Y = random.randint(0, 700)
    window.geometry(f'+{X}+{Y}') 
    Tk.update(window)

# First window goes to a random location
randomWindowPos(master)

# When a key is pressed check if it is "Q" and quit if it is
def key_pressed(event):
    global delete
    if str(event.char) == "Q" or "q":
        delete = True
        master.destroy()

master.bind("<Key>",key_pressed)

# Make a new window and wreck havoc >:)
# Each window makes 5 new windows in a chain reaction)
def openNewWindow():

    global count

    for i in range(5):
        try:
            count += 1
            print(count)

            newWindow = Toplevel(master)
            newWindow.geometry("200x200")
            newWindow.title(BMessages[random.randint(0, len(BMessages)-1)])
            randomWindowPos(newWindow)
            newWindow.bind("<Key>",key_pressed)

            label = Label(newWindow, text=TMessages[random.randint(0, len(TMessages)-1)])

            label.pack(pady = 10)

            btn = Button(newWindow, text =BMessages[random.randint(0, len(BMessages)-1)], command = openNewWindow)
            btn.pack(pady = 10)

            newWindow.protocol("WM_DELETE_WINDOW", openNewWindow)
        except:
            print("Program Disabled...")
        else:
            if delete == False:
                openNewWindow()
            else:
                newWindow.destroy()

# The first window
label = Label(master, text ="Get free health insurance!")

label.pack(pady = 10)

btn = Button(master, text ="CLICK HERE NOW", command = openNewWindow)
btn.pack(pady = 10)

master.protocol("WM_DELETE_WINDOW", openNewWindow)

mainloop()
