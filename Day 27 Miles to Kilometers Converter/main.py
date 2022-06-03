from tkinter import *
FONT = ("Times New Roman", 16, "normal")

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=300, height=100)
window.config(padx=50, pady=20)


def calculate():
    user_input = float(num.get())
    user_input *= 1.60934
    km_num["text"] = user_input


miles_label = Label(text="Miles", font=FONT)
miles_label.grid(row=0, column=2)

km_label = Label(text="Km", font=FONT)
km_label.grid(row=1, column=2)

equal_label = Label(text="is equal to", font=FONT)
equal_label.grid(row=1, column=0)

num = Entry(width=15)
num.grid(row=0, column=1)

button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

km_num = Label(text=0, font=FONT)
km_num.grid(row=1, column=1)

window.mainloop()
