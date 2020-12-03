from boardForm import boardForm
from board import board

def main():
    # boardForm(8)
    newBoard = board(10)
    newBoard.changeFlagState(0, 0, True)
    print("123")
    # print(board(8)._getBombNumbers())
    # #boardForm.__init__(8)

if __name__ == "__main__":
    main()