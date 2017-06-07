#!/usr/bin/env python3

import tkinter

window = tkinter.Tk()
# Code to add widgets will go here...

# set the window title
window.title("Calculator")

# set the window size
window.geometry("500x500")

#color background
#window.configure(background="red")

#PYTHAGOREAN THEOREM FORMULA OPEN
def power():
    import tkinter
    import tkinter.messagebox

    window = tkinter.Tk()
    # Code to add widgets will go here...

    # set the window title
    window.title("Calculator")

    # set the window size
    window.geometry("300x300")

    #color background
    #window.configure(background="red")

    def helloCallBack():

       x1 = tkinter.Entry.get(x)

       y1 = tkinter.Entry.get(y)

       xy = str(((float(x1) * float(x1)) + (float(y1) * float(y1)))**(0.5))

       tkinter.messagebox.showinfo( "Answer", "Your Hypotenuse is " + xy)

    def close_window(): 

       window.destroy()

    #power
    power = tkinter.Label(window, text="PYTHAGOREAN THEOREM", font=("Helvetica", 18))

    voltage1 = tkinter.Label(window, text="Base:")

    x = tkinter.Entry(window)

    current1 = tkinter.Label(window, text="Height:")

    y = tkinter.Entry(window)

    button = tkinter.Button(window, text ="Calculate", command = helloCallBack)

    buttonExit = tkinter.Button(window, text ="Exit", command = close_window)

    power.pack()

    voltage1.pack()

    x.pack()

    current1.pack()

    y.pack()

    button.pack()

    buttonExit.pack()

    window.mainloop()
##FORMULA CLOSE

#EXIT
def close_window(): 

    window.destroy()
#EXIT CLOSE

#MAIN WINDOW
mainLabel = tkinter.Label(window, text="Calculator", font=("Helvetica", 18))

powerLabel = tkinter.Label(window, text="Pythagorean Theorem:")

buttonPower = tkinter.Button(window, text ="Pythagorean Theorem", command = power)

exitLabel = tkinter.Label(window, text="Exit:")

buttonExit = tkinter.Button(window, text ="Exit", command = close_window)

mainLabel.pack()

powerLabel.pack()

buttonPower.pack()

exitLabel.pack()

buttonExit.pack()

window.mainloop()
#MAIN WINDOW CLOSE
