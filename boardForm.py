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
        window.configure(background = "white")
        
        for i in range(boardSize):
            for j in range(boardSize):
                btn = ttk.Button(window, text=f"{i} - {j}").grid(row = i, column = j)

        window.mainloop()


        #btn = ttk.Button(window ,text="Submit").grid(row=4,column=0)
