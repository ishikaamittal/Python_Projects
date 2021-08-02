from tkinter import *


def converter():
    pound = float(entry.get())
    convert = round(pound * 0.45359237, 2)
    result.config(text=convert)


window = Tk()
window.minsize(width=200, height=100)
window.title("lbs to kg converter")
window.config(padx=25, pady=25)

entry = Entry(width=10)
entry.grid(row=0, column=2)

equal_to = Label(text="equals to")
equal_to.grid(row=1, column=0)

result = Label(text="0")
result.grid(row=1, column=2)

unit = Label(text="km")
unit.grid(row=1, column=3)

button = Button(text="Calculate", command=converter)
button.grid(row=2, column=2)
window.mainloop()
