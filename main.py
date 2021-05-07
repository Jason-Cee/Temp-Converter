# Temperature Converter

from tkinter import *

# Root Window
root = Tk()
root.geometry("680x450")
root.title("Temperature Converter")
convert = "none"


# Defining Functions
# Defining Activation
def enable_ctf():
    en_Cel_Far.config(state="normal")
    en_Cel_Far.delete(0, END)

    en_Answer.config(state="normal")
    en_Answer.delete(0, END)
    en_Answer.config(state="readonly")

    en_Far_Cel.config(state="normal")
    en_Far_Cel.delete(0, END)
    en_Far_Cel.config(state="readonly")

    global convert
    convert = "ctf"

# Defining Activation
def enable_ftc():
    en_Far_Cel.config(state="normal")
    en_Far_Cel.delete(0, END)

    en_Answer.config(state="normal")
    en_Answer.delete(0, END)
    en_Answer.config(state="readonly")

    en_Cel_Far.config(state="normal")
    en_Cel_Far.delete(0, END)
    en_Cel_Far.config(state="readonly")

    global convert
    convert = "ftc"

# Defining Calculations
def cal():
    global convert
    if convert == "ctf":
        temp = float(en_Cel_Far.get())
        Answer = str(temp * 9 / 5 + 32)
        en_Answer.config(state="normal")
        en_Answer.delete(0, END)
        en_Answer.insert(0, Answer)
        en_Answer.config(state="readonly")
    elif convert == "ftc":
        temp = float(en_Far_Cel.get())
        Answer = str((temp - 32) * 5 / 9)
        en_Answer.config(state="normal")
        en_Answer.delete(0, END)
        en_Answer.insert(0, Answer)
        en_Answer.config(state="readonly")
    else:
        Answer = "Please convert correctly"
        en_Answer.config(state="normal")
        en_Answer.delete(0, END)
        en_Answer.insert(0, Answer)
        en_Answer.config(state="readonly")

# Defining the Clear Button
def clear():
    en_Cel_Far.config(state="normal")
    en_Cel_Far.delete(0, END)
    en_Cel_Far.config(state="readonly")

    en_Far_Cel.config(state="normal")
    en_Far_Cel.delete(0, END)
    en_Far_Cel.config(state="readonly")

    en_Answer.config(state="normal")
    en_Answer.delete(0, END)
    en_Answer.config(state="readonly")


# Code
# Celcius To Fahrenheit
Cel_Far = LabelFrame(root, text="Celcius to Fahrenheit")
Cel_Far.place(x=50, y=50, width=250, height=100)

# Fahrenheit to Celcius
Far_Cel = LabelFrame(root, text="Fahrenheit to Celcius")
Far_Cel.place(x=350, y=50, width=250, height=100)

# Entry
en_Cel_Far = Entry(Cel_Far)
en_Cel_Far.place(x=20, y=25, width=200)
en_Cel_Far.config(state="readonly")

en_Far_Cel = Entry(Far_Cel)
en_Far_Cel.place(x=20, y=25, width=200)
en_Far_Cel.config(state="readonly")

# Buttons
btn_Cel_Far = Button(root, text="Activate - Celcius to Fahrenheit", command=enable_ctf)
btn_Cel_Far.place(x=50, y=200, width=230)

btn_Far_Cel = Button(root, text="Activate - Fahrenheit to Celcius", command=enable_ftc)
btn_Far_Cel.place(x=350, y=200)

btn_cal = Button(root, text="Calculate Conversion", command=cal)
btn_cal.place(x=50, y=350)

# Answers
en_Answer = Entry(root, text="", bg="red")
en_Answer.place(x=250, y=350, height=50)
en_Answer.config(state="readonly")

btn_Clear = Button(root, text="Clear", command=clear)
btn_Clear.place(x=450, y=350)

btn_Exit = Button(root, text="Exit Program", command=exit)
btn_Exit.place(x=450, y=400)

# Mainloop to run code
root.mainloop()

