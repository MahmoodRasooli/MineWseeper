from board import board
from tkinter import *
from tkinter import ttk


class boardForm:

    def __init__(self, boardSize: int) -> None:
        """
        The main form of the Mine Sweeper game
        It generates buttons and shows the form
        """

        self.board = board(size=boardSize)

        window = Tk()
        window.title("Mine Sweeper")
        window.geometry('1000x900')
        window.configure(background="white", padx=50, pady=50)

        for i in range(boardSize):
            for j in range(boardSize):
                btn = ttk.Button(window, text="").grid(
                    row=i, column=j, padx=2, pady=2, ipadx=7, ipady=30)
                btn.bind('<Button-1>', self.left_click)
                btn.bind('<Button-2>', self.right_click)

        window.mainloop()

        #btn = ttk.Button(window ,text="Submit").grid(row=4,column=0)
    
    def left_click(self, btn, event):
        btn.config(Image=PhotoImage(file='bomb.png'))
    
    def right_click(self, btn, event):
        btn.config(Image=PhotoImage(file='flag.png'))
