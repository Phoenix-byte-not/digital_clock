from tkinter import *
from time import strftime

# Create the window
root = Tk()
root.title("Simple Clock")

# Create the label to show time
def time():
    current = strftime('%H:%M:%S')
    label.config(text=current)
    label.after(1000, time)

label = Label(root, font=('Arial', 40), bg='black', fg='white')
label.pack()

time()  # start the clock
root.mainloop()  # run the window
