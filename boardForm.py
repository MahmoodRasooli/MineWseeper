from tkinter import *
from tkinter import ttk

class boardForm:

    def __init__(boardSize):
        """
        The main form of the Mine Sweeper game
        It generates buttons and shows the form
        """
        
        window = Tk()
        window.title("Mine Sweeper")
        window.geometry('1000x900')
        window.configure(background = "white", padx = 50, pady = 50)
        
        for i in range(boardSize):
            for j in range(boardSize):
                btn = ttk.Button(window, text="").grid(row = i + 5, column = j + 5, padx = 2, pady = 2, ipadx=7, ipady=30)


        window.mainloop()


        #btn = ttk.Button(window ,text="Submit").grid(row=4,column=0)
