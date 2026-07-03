import tkinter as tk   
from tkinter import messagebox


def Addition():
    number1 = float(entry1.get())
    number2 = float(entry2.get())
    result_Label.config(text =f"Answer = {number1 + number2}")


def Substract():
    number1 = float(entry1.get())
    number2 = float(entry2.get())
    result_Label.config(text =f"Answer = {number1 - number2}")


def Multiply():
    number1 = float(entry1.get())
    number2 = float(entry2.get())
    result_Label.config(text =f"Answer = {number1 * number2}")


def Divide():
    number1 = float(entry1.get())
    number2 = float(entry2.get())
    
    if(number2 == 0):
        messagebox.showerror("Error","cannot divide by zero!")

    else:
        result_Label.config(text = f"Answer = {number1 / number2}")


window = tk.Tk()
window.title("calculator")
window.geometry("400x500")
window.config(bg = "#1a102e")

title = tk.Label(window , text = "Calculator" , bg = "#1a102e" , fg = "#38bdf8" , font = ("Arial" , 20 , "bold"))
title.pack(pady = 15)

entry1 = tk.Entry(window, bg = "#2d1b4e", fg = "white", insertbackground = "white", font = ("Arial",15))
entry1.pack(pady = 10)

entry2 = tk.Entry(window, bg = "#2d1b4e", fg = "white", insertbackground = "white", font = ("Arial",15))
entry2.pack(pady = 10)

tk.Button(window, text = "+", bg="#7c3aed", fg="white", activebackground="#9333ea", font = ("Arial",15, "bold"), width = 5, command = Addition).pack(pady = 5)

tk.Button(window, text = "-", bg="#7c3aed", fg="white", activebackground="#9333ea", font = ("Arial",15, "bold"), width = 5, command = Substract).pack(pady = 5)

tk.Button(window, text = "*", bg="#7c3aed", fg="white", activebackground="#9333ea", font = ("Arial", 15, "bold"), width = 5, command = Multiply).pack(pady = 5)

tk.Button(window, text = "/", bg="#7c3aed", fg="white", activebackground="#9333ea", font = ("Arial",15, "bold"), width = 5, command = Divide).pack(pady = 5)
          

result_Label = tk.Label(window, text = "Answer = ", font = ("Arial",16),bg = "#1a102e", fg = "#38bdf8")
result_Label.pack(pady = 20)

window.mainloop()





