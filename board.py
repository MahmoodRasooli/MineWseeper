from piece import piece


### Represents a board which contains the placeholders
class board:
    def __init__(self, size: int) -> None:
        super().__init__()

        if size <= 2:
            raise Exception("size in not valid")

        self.size = size
        self.pieces = []

    def __init__(self, size: int, pieces: list) -> None:
        super().__init__()

        if size <= 2:
            raise Exception("size in not valid")

        self.size = size
        self.pieces = pieces

    def clearPiece(self, i_index: int, j_index: int) -> bool:
        """
        Clears the piece, meaning the player left-clicked on the box
        """
        return self.pieces[i_index, j_index].clear()

    def changeFlagState(self, i_index: int, j_index: int, flagState: bool) -> None:
        """
        Changes the flag state of the given box
        """
        self.pieces[i_index, j_index].changeFlagState(flagState)