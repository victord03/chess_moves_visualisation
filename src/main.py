
class BoardState:
    state: dict

    def __init__(self):

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

    def __setitem__(self, key, value):
        self.state[key] = value


class ChessPiece:
    name: str
    colour: str
    position: str
    # pawn_double_move: bool

    def __init__(self, name, colour, position, board):
        self.name = name
        self.colour = colour
        self.position = position
        self.update_board_state(board)

    def update_board_state(self, board: BoardState):
        board[f'{self.position[0]}{self.position[1]}'] = self.name

    def rook_instructions(self) -> tuple:
        current_position_rank = self.position[0]
        current_position_file = self.position[1]

        all_legal_moves = list()

        for file in files:
            if file == current_position_file:
                continue
            all_legal_moves.append(f'{current_position_rank}{file}')

        for rank in ranks:
            if rank == current_position_rank:
                continue
            all_legal_moves.append(f'{rank}{current_position_file}')

        # print(all_legal_moves)
        return tuple(all_legal_moves)

    def pawn_instructions(self):
        ...

    def knight_instructions(self):
        ...


ranks = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
files = ['1', '2', '3', '4', '5', '6', '7', '8']


def generate_legal_moves_for(piece: ChessPiece):

    if piece.name == 'Rook':
        return piece.rook_instructions()


def visualise_moves_for(piece: ChessPiece):
    ...


def main():
    board = BoardState()

    rook = ChessPiece(name='Rook', colour='White', position=('A', '1'), board=board)
    generate_legal_moves_for(rook)

    # print(board.state)
    # print(len(list(board.state.keys())))


if __name__ == '__main__':
    main()
