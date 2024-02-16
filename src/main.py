
class BoardState:
    state: dict

    def __init__(self) -> None:

        self.state = {
            'A1': '',
            'B1': '',
            'C1': '',
            'D1': '',
            'E1': '',
            'F1': '',
            'G1': '',
            'H1': '',
            'A2': '',
            'B2': '',
            'C2': '',
            'D2': '',
            'E2': '',
            'F2': '',
            'G2': '',
            'H2': '',
            'A3': '',
            'B3': '',
            'C3': '',
            'D3': '',
            'E3': '',
            'F3': '',
            'G3': '',
            'H3': '',
            'A4': '',
            'B4': '',
            'C4': '',
            'D4': '',
            'E4': '',
            'F4': '',
            'G4': '',
            'H4': '',
            'A5': '',
            'B5': '',
            'C5': '',
            'D5': '',
            'E5': '',
            'F5': '',
            'G5': '',
            'H5': '',
            'A6': '',
            'B6': '',
            'C6': '',
            'D6': '',
            'E6': '',
            'F6': '',
            'G6': '',
            'H6': '',
            'A7': '',
            'B7': '',
            'C7': '',
            'D7': '',
            'E7': '',
            'F7': '',
            'G7': '',
            'H7': '',
            'A8': '',
            'B8': '',
            'C8': '',
            'D8': '',
            'E8': '',
            'F8': '',
            'G8': '',
            'H8': '',

        }

    def __setitem__(self, key, value) -> None:
        self.state[key] = value


class ChessPiece:

    def __init__(self, board):
        self.update_board_state(board)

    def __str__(self):
        return f'{self.name}({self.position})'

    def update_board_state(self, board: BoardState) -> None:
        board[f'{self.current_rank}{self.current_file}'] = self.name


class Rook(ChessPiece):
    name: str
    colour: str
    position: str
    current_rank: str
    current_file: str

    def __init__(self, colour, position, board):
        self.name = 'Rook'
        self.colour = colour
        self.position = position
        self.current_rank = position[0]
        self.current_file = position[1]
        super().__init__(board)

    def find_legal_moves(self) -> tuple:

        all_legal_moves = list()

        for file in files:
            if file == self.current_file:
                continue
            all_legal_moves.append(f'{self.current_rank}{file}')

        for rank in ranks:
            if rank == self.current_rank:
                continue
            all_legal_moves.append(f'{rank}{self.current_file}')

        return tuple(all_legal_moves)


class Pawn(ChessPiece):
    name: str
    colour: str
    position: str
    current_rank: str
    current_file: str

    def __init__(self, colour, position, board):
        self.name = 'Pawn'
        self.colour = colour
        self.current_rank = position[0]
        self.current_file = position[1]
        super().__init__(board)

    def find_legal_moves(self) -> tuple:

        """if self.current_file == '2':
            all_legal_moves = [f'{self.current_rank}3', f'{self.current_rank}4']
        elif self.current_file == '7':
            all_legal_moves = [f'{self.current_rank}6', f'{self.current_rank}5']
        elif self.current_file == '1':
            all_legal_moves = ['']
        elif self.current_file == '8':
            all_legal_moves = ['']
        else:"""

        # if self.colour == 'White':
            # all_legal_moves = [f'{self.current_rank}{int(self.current_file)+1}']

        all_legal_moves = list()

        # pawn white
        if self.colour == 'White':
            if self.current_file == '2':
                all_legal_moves = [f'{self.current_rank}3', f'{self.current_rank}4']
            elif self.current_file == '1':
                all_legal_moves = ['Promotion']
            else:
                all_legal_moves = [f'{self.current_rank}{int(self.current_file)+1}']

        # pawn black
        elif self.colour == 'Black':
            if self.current_file == '7':
                all_legal_moves = [f'{self.current_rank}6', f'{self.current_rank}5']
            elif self.current_file == '8':
                all_legal_moves = ['Promotion']
            else:
                all_legal_moves = [f'{self.current_rank}{int(self.current_file)-1}']

        return tuple(all_legal_moves)


class Knight(ChessPiece):
    name: str
    colour: str
    position: str
    current_rank: str
    current_file: str

    def __init__(self, colour, position, board):
        super().__init__(board)
        self.name = 'Knight'
        self.colour = colour
        self.current_rank = position[0]
        self.current_file = position[1]
        super().__init__(board)

    def find_legal_moves(self) -> tuple:
        all_legal_moves = list()

        # self.current_rank + 2, self.current_file + 1
        # self.current_rank + 2, self.current_file - 1
        # self.current_rank - 2, self.current_file - 1
        # self.current_rank - 2, self.current_file + 1
        # self.current_file + 2, self.current_rank + 1
        # self.current_file + 2, self.current_rank - 1
        # self.current_file - 2, self.current_rank + 1
        # self.current_file - 2, self.current_rank - 1

        return tuple(all_legal_moves)


ranks = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
files = ['1', '2', '3', '4', '5', '6', '7', '8']


def generate_legal_moves_for(piece) -> tuple:

    pieces = {
        0: Rook,
        1: Pawn,
        2: Knight,
    }

    if piece.name == 'Rook':
        return pieces[0].find_legal_moves(piece)


def visualise_moves_for(piece):
    ...


def main():
    board = BoardState()

    rook_white = Rook(colour='White', position='A1', board=board)
    pawn_black = Pawn(colour='Black', position='A2', board=board)

    # print(list(map(generate_legal_moves_for, [pawn_black, rook_white])))

    # print(rook_white)
    # generate_legal_moves_for(rook_white)
    # print(pawn_black.instructions())

    # print(board.state)
    # print(len(list(board.state.keys())))


if __name__ == '__main__':
    main()
