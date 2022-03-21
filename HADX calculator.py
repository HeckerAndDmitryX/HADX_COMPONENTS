from tkinter import *

root = Tk()
root.title("HADX Calculator")

entry1=Entry(root, width=35, borderwidth=5)
entry1.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current_number = entry1.get()
    entry1.delete(0, END)
    entry1.insert(0, str(current_number) + str(number))
def button_clear():
    entry1.delete(0, END)
def button_plus():
    first_number=entry1.get()
    global button
    button="plus"
    global number1
    number1=int(first_number)
    entry1.delete(0, END)
def button_minus():
    first_number=entry1.get()
    global button
    button="minus"
    global number1
    number1=int(first_number)
    entry1.delete(0, END)
def button_del():
    first_number=entry1.get()
    global button
    button="del"
    global number1
    number1=int(first_number)
    entry1.delete(0, END)
def button_umn():
    first_number=entry1.get()
    global button
    button="umn"
    global number1
    number1=int(first_number)
    entry1.delete(0, END)
def button_ravno():
    second_number=entry1.get()
    entry1.delete(0, END)
    if button == "plus":
        entry1.insert(0, number1 + int(second_number))#вставляем сумму
    if button == "minus":
        entry1.insert(0, number1 - int(second_number))#вставляем разность
    if button == "umn":
        entry1.insert(0, number1 * int(second_number))#вставляем
        #умножение
    if button == "del":
        entry1.insert(0, number1 / int(second_number))#вставляем
        #деление
        
button1=Button(root, text="1", padx=40, pady=20,
               command=lambda:button_click(1))
button2=Button(root, text="2", padx=40, pady=20,
               command=lambda:button_click(2))
button3=Button(root, text="3", padx=40, pady=20,
               command=lambda:button_click(3))
button4=Button(root, text="4", padx=40, pady=20,
               command=lambda:button_click(4))
button5=Button(root, text="5", padx=40, pady=20,
               command=lambda:button_click(5))
button6=Button(root, text="6", padx=40, pady=20,
               command=lambda:button_click(6))
button7=Button(root, text="7", padx=40, pady=20,
               command=lambda:button_click(7))
button8=Button(root, text="8", padx=40, pady=20,
               command=lambda:button_click(8))
button9=Button(root, text="9", padx=40, pady=20,
               command=lambda:button_click(9))
button0=Button(root, text="0", padx=40, pady=20,
               command=lambda:button_click(0))

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=0)

b_plus=Button(root, text="+", padx=39, pady=20, command=button_plus)
b_ravno=Button(root, text="=", padx=89, pady=20, command=button_ravno)
b_clear=Button(root, text="Удалить", padx=70, pady=20, command=button_clear)
b_minus=Button(root, text="-", padx=40, pady=20, command=button_minus)
b_umn=Button(root, text="*", padx=40, pady=20, command=button_umn)
b_del=Button(root, text="/", padx=40, pady=20, command=button_del)

b_plus.grid(row=5, column=0)
b_ravno.grid(row=5, column=1, columnspan=2)
b_clear.grid(row=4, column=1, columnspan=2)
b_minus.grid(row=6, column=0)
b_umn.grid(row=6, column=1)
b_del.grid(row=6, column=2)
