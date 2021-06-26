from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title("ATM")
window.resizable(False, False) 

# Main frame
mainFrame = Frame(window, bg='#D4D4D3')
mainFrame.grid(columnspan=5)


# Page 0
page0 = LabelFrame(mainFrame, bg='Light blue')
page0.grid(columnspan=5, ipadx=270, ipady=110, padx=10, pady=10)

# Assigning a global page to access each page from anywhere
globalPageKey = page0

# Welcome text
welcomeText = Label(page0, text='Welcome to INAXIA bank atm', font=('Courier', 20), bg='Light blue')
welcomeText.place(relx=0.5, rely=0.35, anchor='center')

# Next button
nextbutton = Button(page0, text='Next', bg='White', height=2, width=10)
nextbutton.place(relx=0.5, rely=0.65, anchor='center')


# Full frame for buttons
bottomFrame = Frame(window, bg='#D4D4D3')
bottomFrame.grid(columnspan=5, ipadx=140)

# Frame for fixed buttons
buttonsFrame = LabelFrame(bottomFrame, bg='#AAA9A8')
buttonsFrame.grid(columnspan=5, padx=10, pady=10, sticky='')
bottomFrame.grid_rowconfigure(0, weight=1)
bottomFrame.grid_columnconfigure(0, weight=1)


# Button shapes
img1 = ImageTk.PhotoImage(Image.open("btn1.png"))
img2 = ImageTk.PhotoImage(Image.open("btn2.png"))
img3 = ImageTk.PhotoImage(Image.open("btn3.png"))
img4 = ImageTk.PhotoImage(Image.open("btn4.png"))
img5 = ImageTk.PhotoImage(Image.open("btn5.png"))
img6 = ImageTk.PhotoImage(Image.open("btn6.png"))
img7 = ImageTk.PhotoImage(Image.open("btn7.png"))
img8 = ImageTk.PhotoImage(Image.open("btn8.png"))
img9 = ImageTk.PhotoImage(Image.open("btn9.png"))
img10 = ImageTk.PhotoImage(Image.open("btn10.png"))


# Fixed buttons
button1 = Button(buttonsFrame, image=img1, fg='Black', bg='Black', command=lambda: pressButton(globalList[0]), height=40, width=40)
button1.grid(row=1, column=0, padx=5, pady=5)

button2 = Button(buttonsFrame, image=img2, fg='Black', bg='Black', command=lambda: pressButton(globalList[1]), height=40, width=40)
button2.grid(row=1, column=1, padx=5, pady=5)

button3 = Button(buttonsFrame, image=img3, fg='Black', bg='Black', command=lambda: pressButton(globalList[2]), height=40, width=40)
button3.grid(row=1, column=2, padx=5, pady=5)

button4 = Button(buttonsFrame, image=img4, fg='Black', bg='Black', command=lambda: pressButton(globalList[3]), height=40, width=40)
button4.grid(row=2, column=0, padx=5, pady=5)

button5 = Button(buttonsFrame, image=img5, fg='Black', bg='Black', command=lambda: pressButton(globalList[4]), height=40, width=40)
button5.grid(row=2, column=1, padx=5, pady=5)

button6 = Button(buttonsFrame, image=img6, fg='Black', bg='Black', command=lambda: pressButton(globalList[5]), height=40, width=40)
button6.grid(row=2, column=2, padx=5, pady=5)

button7 = Button(buttonsFrame, image=img7, fg='Black', bg='Black', command=lambda: pressButton(globalList[6]), height=40, width=40)
button7.grid(row=3, column=0, padx=5, pady=5)

button8 = Button(buttonsFrame, image=img8, fg='Black', bg='Black', command=lambda: pressButton(globalList[7]), height=40, width=40)
button8.grid(row=3, column=1, padx=5, pady=5)

button9 = Button(buttonsFrame, image=img9, fg='Black', bg='Black', command=lambda: pressButton(globalList[8]), height=40, width=40)
button9.grid(row=3, column=2, padx=5, pady=5)

button0 = Button(buttonsFrame, image=img10, fg='Black', bg='Black', command=lambda: pressButton(globalList[9]), height=40, width=40)
button0.grid(row=4, column=1, padx=5, pady=5)

backspace = Button(buttonsFrame, text='BACKSPACE', fg='Black', bg='Light grey', command=lambda: clearOne(), height=2, width=10)
backspace.grid(row=1, column=4, padx=5, pady=5)

clear = Button(buttonsFrame, text='CLEAR', fg='Black', bg='Light grey', command=lambda: clearAll(), height=2, width=10)
clear.grid(row=2, column=4, padx=5, pady=5)

enter = Button(buttonsFrame, text='ENTER', fg='Black', bg='Light grey', command=lambda: pressEnter(), height=2, width=10)
enter.grid(row=3, column=4, padx=5, pady=5)

# To open the screen
window.mainloop()