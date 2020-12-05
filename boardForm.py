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

        for i_index in range(boardSize):
            for j_index in range(boardSize):
                icon = PhotoImage(Image.open("flag.png"))
                btn = ttk.Button(self.window, image=icon)#.grid(row=i, column=j, padx=2, pady=2, ipadx=7, ipady=30)
                btn.grid(row=i_index, column=j_index, padx=2, pady=2, ipadx=7, ipady=30)
                # btn.configure(image = icon)
                btn.bind('<Button-1>', self.left_click)
                btn.bind('<Button-3>', self.right_click)
                # btn.pack()

        self.window.pack_propagate()
        self.window.mainloop()

        #btn = ttk.Button(window ,text="Submit").grid(row=4,column=0)
    
    def _addBox(self, i_index: int, j_index: int):
        # text = "Bomb" if self.board.pieces[i_index][j_index].haveBomb else str(self.board.pieces[i_index][j_index].neiboursBombCount)
        pass

    def left_click(self, event):
        event.widget.configure(text = "Left Clicked")
    
    def right_click(self, event):
        event.widget.configure(text = "Right Clicked")