import src.main as m

'''
This program aims to provide visual representation of all legal chess moves in any given board 
state, by drawing arrows from the origin cell to the destination cell. 

Capture moves can have a different arrow colour than simple moves. 

Capture moves of defended pieces should have an extra arrow drawn that originates in the origin 
from which the piece can capture back and end on the capture square.
'''


def setup_board():
    return m.BoardState()


def setup_piece():
    board = setup_board()
    name = 'Rook'
    colour = 'White'
    position = 'A1'

    return board, m.ChessPiece(name=name, colour=colour, position=position, board=board)


class TestPiece:
    def test_chess_piece(self):
        assert isinstance(setup_piece()[1], m.ChessPiece)

    def test_new_piece_board_update(self):
        board, piece = setup_piece()
        assert board.state == {'A1': 'Rook', 'B1': '', 'C1': '', 'D1': '', 'E1': '', 'F1': '', 'G1': '', 'H1': '', 'A2': '', 'B2': '', 'C2': '', 'D2': '', 'E2': '', 'F2': '', 'G2': '', 'H2': '', 'A3': '', 'B3': '', 'C3': '', 'D3': '', 'E3': '', 'F3': '', 'G3': '', 'H3': '', 'A4': '', 'B4': '', 'C4': '', 'D4': '', 'E4': '', 'F4': '', 'G4': '', 'H4': '', 'A5': '', 'B5': '', 'C5': '', 'D5': '', 'E5': '', 'F5': '', 'G5': '', 'H5': '', 'A6': '', 'B6': '', 'C6': '', 'D6': '', 'E6': '', 'F6': '', 'G6': '', 'H6': '', 'A7': '', 'B7': '', 'C7': '', 'D7': '', 'E7': '', 'F7': '', 'G7': '', 'H7': '', 'A8': '', 'B8': '', 'C8': '', 'D8': '', 'E8': '', 'F8': '', 'G8': '', 'H8': ''}


class TestVisualisationEngine:
    def test_generate_legal_moves_for(self):
        board, piece = setup_piece()
        assert m.generate_legal_moves_for(piece) == ('A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1')

    def test_visualise_moves_for(self):
        ...


class TestBoard:
    def test_board_state(self):
        assert len(list(setup_board().state.keys())) == 64

