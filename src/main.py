
"""

movement_dictionary = {
    'Pawn': set(),
    'Rook': set(),
    'Knight': set(),
    'Bishop': set(),
    'Queen': set(),
    'King': set(),
}


Rook movement:
    Any number of squares on the same file,
    Any number of squares on the same rank.

    current_position_rank = 'A'
    current_position_file = '1'

        ranks = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'}
        files = {'1', '2', '3', '4', '5', '6', '7', '8'}

        ranks.remove(current_position_rank)
        files.remove(current_position_file)


        zip(position_ranks, position_files)

"""


class BoardState:
    state: dict

    def __init__(self):

        self.state = {
            'A1': '',
            'B1': '',
            'C1': '',
            'D1': '',
            'E1': ''

        }


class ChessPiece:
    name: str
    colour: str
    position: tuple
    # pawn_double_move: bool

    def __init__(self, name, colour, position):
        self.name = name
        self.colour = colour
        self.position = position

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

        print(all_legal_moves)
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


def visualise_moves_for(piece):
    ...


def main():
    rook = ChessPiece(name='Rook', colour='White', position=('A', '1'))
    generate_legal_moves_for(rook)


if __name__ == '__main__':
    main()
