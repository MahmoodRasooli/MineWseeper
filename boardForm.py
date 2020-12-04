import tkinter
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

        self.window = Tk()
        self.window.title("Mine Sweeper")
        self.window.geometry('1000x900')
        self.window.configure(background="white", padx=50, pady=50)

        for i in range(boardSize):
            for j in range(boardSize):
                text = "Bomb" if self.board.pieces[i][j].haveBomb else str(self.board.pieces[i][j].neiboursBombCount)
                btn = ttk.Button(self.window, text=text)#.grid(row=i, column=j, padx=2, pady=2, ipadx=7, ipady=30)
                btn.grid(row=i, column=j, padx=2, pady=2, ipadx=7, ipady=30)
                btn.bind('<Button-1>', self.left_click)
                btn.bind('<Button-2>', self.right_click)

        self.window.mainloop()

        #btn = ttk.Button(window ,text="Submit").grid(row=4,column=0)
    
    def left_click(self, event):
        event.widget.configure(text = "Left Clicked")
    
    def right_click(self, event):
        event.widget.configure(text = "Right Clicked")
