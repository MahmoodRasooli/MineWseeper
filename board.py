from piece import piece
from math import ceil
from random import randint

### Represents a board which contains the placeholders
class board:

    def __init__(self, size: int, pieces: list = None) -> None:
        super().__init__()

        if size <= 2:
            raise Exception("size in not valid")

        self.size = size        

        if pieces is not None:
            self.pieces = pieces
        else:            
            self._generatePieces()
            self._setBombs()
            # self._determinePiecesNeighboursBombsCount()

    def _getBombNumbers(self) -> int:
        """
        Returns the number of the bombs on the board
        """
        return int(ceil((self.size ** 2) * 15 / 100))

    def _generatePieces(self) -> None:
        """
        Initialize the pieces and their states on the board
        """        
        self.pieces = [[piece(y, x) for x in range(self.size)] for y in range(self.size)]

    def _setBombs(self) -> None:
        """
        Sets the bombs in the pieces and also corrects the adjacent pieces neighboursBombsCount property
        """
        for i in range(self._getBombNumbers()):
            random_row = randint(0, self.size - 1)
            random_col = randint(0, self.size - 1)
            
            # Checks if the picked random piece is already bombed
            while(self.pieces[random_row][random_col].haveBomb):
                random_row = randint(0, self.size - 1)
                random_col = randint(0, self.size - 1)

            self.pieces[random_row][random_col].haveBomb = True

            # Sets the neiboursBombCount of the adjacent pieces
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    if(i == 0 and j == 0):
                        continue

                    if(random_row + i < 0 or random_row + i >= self.size or
                        random_col + j < 0 or random_col + j >= self.size):
                        continue

                    self.pieces[random_row + i][random_col + j].neiboursBombCount += 1

    def _determinePiecesNeighboursBombsCount(self) -> None:
        """
        Fill the neiboursBombCount in each piece
        """
        # for i in range(self.size):
        #     for j in range(self.size):
        #         self.pieces[i][j].
        pass

    def clearPiece(self, i_index: int, j_index: int) -> bool:
        """
        Clears the piece, meaning the player left-clicked on the piece
        """
        return self.pieces[i_index][j_index].clear()

    def changeFlagState(self, i_index: int, j_index: int, flagState: bool) -> None:
        """
        Changes the flag state of the given piece
        """
        self.pieces[i_index][j_index].changeFlagState(flagState)