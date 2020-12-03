### This class represents a piece on the board and contains information about the state of the piece
class piece(object):

    def __init__(self, i_index: int, j_index: int) -> None:
        super().__init__()
        self.i_index = i_index
        self.j_index = j_index
        self.neiboursBombCount = 0
        self.haveBomb = False
        self.isCleared = False
        self.isFlagged = False

    def changeFlagState(self, flagState: bool) -> None:
        """
        Changes the isFlagged state
        """
        self.isFlagged = flagState

    def clear(self) -> bool:
        """
        Clear the piece, happens when the player left-clicks on the piece
        """
        if self.haveBomb:
            return False
        else:
            self.isCleared = False
            return True