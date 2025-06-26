
from tkinter import *

import time,sys



def endprogram():
	print ("\nProgram terminated!")
	sys.exit()



def Camera1():
    import CPredict

def PTrain():
    import LiveRecognition as liv

    liv.att()
    del sys.modules["LiveRecognition"]

def Person():
    import LiveRecognition1 as liv
    liv.att()
    del sys.modules["LiveRecognition1"]



def Currency():
    import CurrencyPredict
def main_account_screen():
    global main_screen
    main_screen = Tk()
    width = 600
    height = 600
    screen_width = main_screen.winfo_screenwidth()
    screen_height = main_screen.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    main_screen.geometry("%dx%d+%d+%d" % (width, height, x, y))
    main_screen.resizable(0, 0)
    # main_screen.geometry("300x250")
    main_screen.configure()
    main_screen.title("Obstacle Detection For Blind Person ")

    Label(text="Obstacle Detection For Blind Person", width="300", height="5", font=("Calibri", 16)).pack()
    Label(text="").pack()
    Button(text="Train", font=(
        'Verdana', 15), height="2", width="20", command=PTrain).pack(side=TOP)
    Label(text="").pack()
    Button(text="Person", font=(
        'Verdana', 15), height="2", width="20", command=Person).pack(side=TOP)

    Label(text="").pack()

    Button(text="Obstacle", font=(
        'Verdana', 15), height="2", width="20", command=Camera1).pack(side=TOP)

    Label(text="").pack()

    Button(text="Currency", font=(
        'Verdana', 15), height="2", width="20", command=Currency).pack(side=TOP)

    main_screen.mainloop()


main_account_screen()

