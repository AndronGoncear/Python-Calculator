import math
from tkinter import *


def press_button(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def sqrt():
    global equation_text
    total = str(eval(equation_text))
    total = str(math.sqrt(float(total)))
    equation_label.set(total)
    equation_text = total


def percent():
    global equation_text
    try:
        if (equation_text[-2] == "*"):
            result = (float(eval(equation_text[:-2])) * float(equation_text[-1])) / 100
            equation_label.set(result)
            equation_text = str(result)
        if (equation_text[-2] == "/"):
            result = (float(eval(equation_text[:-2])) / (float(equation_text[-1]) / 100))
            equation_label.set(result)
            equation_text = str(result)
        if (equation_text[-2] == "+"):
            result = (float(eval(equation_text[:-2])) * float(equation_text[-1])) / 100
            result2 = float(eval(equation_text[:-2])) + result
            equation_label.set(result2)
            equation_text = str(result2)
        if (equation_text[-2] == "-"):
            result = (float(eval(equation_text[:-2])) * float(equation_text[-1])) / 100
            result2 = float(eval(equation_text[:-2])) - result
            equation_label.set(result2)
            equation_text = str(result2)

    except ZeroDivisionError:
        equation_label.set("We can't divide by Zero!!!")
        equation_text = ""
    except SyntaxError:
        equation_label.set("We can't do this operations!!!")
        equation_text = ""


def changeplusminus():
    global equation_text
    total = str(-float(equation_text))
    equation_label.set(total)
    equation_text = total


def backspace():
    global equation_text
    total = equation_text[:-1]
    equation_label.set(total)
    equation_text = total


def result():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:

        equation_label.set("We can't divide by Zero!!!")
        equation_text = ""
    except SyntaxError:
        equation_label.set("We can't do this operations!!!")
        equation_text = ""


def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""


def key_press(event):
    key = event.char
    if key.isdigit() or key in "+-*/.":
        press_button(key)
    elif key == "\r" or key == "\n":
        result()
    elif key == "\x08":
        backspace()
    elif key == "*":
        press_button("*")
    elif key == "/":
        press_button("/")


window = Tk()
window.title("Calculator Program")
window_width = 800
window_height = 650

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))
window.configure(bg="#f0f0f0")
file = "./ImageFolder/calc.png"
icon = PhotoImage(file=file)
window.iconphoto(True, icon)
equation_text = ""
equation_label = StringVar()
label = Label(window, textvariable=equation_label, font=("Consolas", 30), width=32, height=2, bg="#e4ddd4", anchor="e",
              borderwidth=2, relief="solid", highlightthickness=0)
label.grid(row=0, column=0, columnspan=6, pady=25, padx=(46, 0))
frame = Frame(window)
frame.grid(row=1, column=0, padx=(60, 0), pady=20)
button1 = Button(frame, text="C", height=3, width=8, font=("Helvetica", 15),  command=clear, border=5, bg="#ff6666", fg="white")
button1.grid(row=3, column=0, padx=5, pady=5)
button2 = Button(frame, text=0, height=3, width=8, font=("Helvetica", 15),  command=lambda: press_button(0), border=5, fg="white",
                 bg="#A7A5A5")
button2.grid(row=3, column=1, padx=5, pady=5)
button3 = Button(frame, text="00", height=3, width=8, font=("Helvetica", 15), command=lambda: press_button("00"), border=5, fg="white",
                 bg="#A7A5A5")
button3.grid(row=3, column=2, padx=5, pady=5)
button4 = Button(frame, text=".", height=3, width=8, font=("Helvetica", 15),  command=lambda: press_button("."), border=5, fg="white",
                 bg="#A7A5A5")
button4.grid(row=3, column=3, padx=5, pady=5)
button5 = Button(frame, text="+", height=3, width=8, font=("Helvetica", 15),  command=lambda: press_button("+"), border=5, fg="white",
                 bg="#101014")
button5.grid(row=3, column=4, padx=5, pady=5)
button6 = Button(frame, text="=", height=3, width=8, font=("Helvetica", 15),  command=result, border=5, fg="white", bg="#101014")
button6.grid(row=3, column=5, padx=5, pady=5)
button7 = Button(frame, text="\u221A", height=3, width=8, font=("Helvetica", 15),  command=sqrt, border=5,
                 fg="white", bg="#101014")
button7.grid(row=2, column=0, padx=5, pady=5)
button8 = Button(frame, text=1, height=3, width=8, font=("Helvetica", 15),  command=lambda: press_button(1), border=5, fg="white",
                 bg="#A7A5A5")
button8.grid(row=2, column=1, padx=5, pady=5)
button9 = Button(frame, text=2, height=3, width=8, font=("Helvetica", 15),  command=lambda: press_button(2), border=5, fg="white",
                 bg="#A7A5A5")
button9.grid(row=2, column=2, padx=5, pady=5)
button10 = Button(frame, text=3, height=3, width=8, font=("Helvetica", 15),  command=lambda: press_button(3), border=5, fg="white",
                  bg="#A7A5A5")
button10.grid(row=2, column=3, padx=5, pady=5)
button11 = Button(frame, text="+",height=8, width=8, font=("Helvetica", 15),  command=lambda: press_button("+"), border=5, fg="white",
                  bg="#101014")
button11.grid(row=2, column=4, rowspan=2, padx=5, pady=5)
button12 = Button(frame, text="=", height=8, width=8, font=("Helvetica", 15),  command=result, border=5, fg="white",
                  bg="#101014")
button12.grid(row=2, column=5, rowspan=2, padx=5, pady=5)
button13 = Button(frame, text="+/-", height=3, width=8, font=("Helvetica", 15),  command=changeplusminus, border=5, fg="white",
                  bg="#101014")
button13.grid(row=1, column=0, padx=5, pady=5)
button14 = Button(frame, text=4, height=3, width=8, font=("Helvetica", 15),  command=lambda: press_button(4), border=5, fg="white",
                  bg="#A7A5A5")
button14.grid(row=1, column=1, padx=5, pady=5)
button15 = Button(frame, text=5,height=3, width=8, font=("Helvetica", 15),  command=lambda: press_button(5), border=5, fg="white",
                  bg="#A7A5A5")
button15.grid(row=1, column=2, padx=5, pady=5)
button16 = Button(frame, text=6, height=3, width=8, font=("Helvetica", 15),  command=lambda: press_button(6), border=5, fg="white",
                  bg="#A7A5A5")
button16.grid(row=1, column=3, padx=5, pady=5)
button17 = Button(frame, text="*", height=3, width=8, font=("Helvetica", 15),  command=lambda: press_button("*"), border=5, fg="white",
                  bg="#101014")
button17.grid(row=1, column=4, padx=5, pady=5)
button18 = Button(frame, text="-", height=3, width=8, font=("Helvetica", 15),  command=lambda: press_button("-"), border=5, fg="white",
                  bg="#101014")
button18.grid(row=1, column=5, padx=5, pady=5)
button19 = Button(frame, text="00→0", height=3, width=8, font=("Helvetica", 15),  command=backspace, border=5,
                  fg="white", bg="#101014")
button19.grid(row=0, column=0, padx=5, pady=5)
button20 = Button(frame, text=7, height=3, width=8, font=("Helvetica", 15),  command=lambda: press_button(7), border=5, fg="white",
                  bg="#A7A5A5")
button20.grid(row=0, column=1, padx=5, pady=5)
button21 = Button(frame, text=8, height=3, width=8, font=("Helvetica", 15),  command=lambda: press_button(8), border=5, fg="white",
                  bg="#A7A5A5")
button21.grid(row=0, column=2, padx=5, pady=5)
button22 = Button(frame, text=9, height=3, width=8, font=("Helvetica", 15),  command=lambda: press_button(9), border=5, fg="white",
                  bg="#A7A5A5")
button22.grid(row=0, column=3, padx=5, pady=5)
button23 = Button(frame, text="/", height=3, width=8, font=("Helvetica", 15),  command=lambda: press_button("/"), border=5, fg="white",
                  bg="#101014")
button23.grid(row=0, column=4, padx=5, pady=5)
button24 = Button(frame, text="%", height=3, width=8, font=("Helvetica", 15),  command=percent, border=5, fg="white",
                  bg="#101014")
button24.grid(row=0, column=5, padx=5, pady=5)
window.bind("<Key>", key_press)
window.mainloop()
