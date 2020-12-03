from boardForm import boardForm
from board import board

def main():
    print(board(10)._getBombNumbers())
    print(board(8)._getBombNumbers())
    #boardForm.__init__(8)

if __name__ == "__main__":
    main()