### This class represents a piece on the board and contains information about the state of the box
class piece(object):

    def __init__(self) -> None:
        super().__init__()
        self.i_index = 0
        self.j_index = 0
        self.neiboursBombCount = 0
        self.haveBomb = False
        self.isCleared = False
        self.isFlagged = False        

    def __init__(self, i_index: int, j_index: int, neiboursBombCount: int, haveBomb: bool) -> None:
        super().__init__()
        self.i_index = i_index
        self.j_index = j_index
        self.neiboursBombCount = neiboursBombCount
        self.haveBomb = haveBomb
        self.isCleared = False
        self.isFlagged = False

    def changeFlagState(self, flagState: bool) -> None:
        """
        Changes the isFlagged property
        """
        self.isFlagged = flagState

    def clear(self) -> bool:
        """
        Clear the piece, happens when the player left-clicks on the box
        """
        if self.haveBomb:
            return False
        else:
            self.isCleared = False
            return True