import src.main as m
import pytest

'''
This program aims to provide visual representation of all legal chess moves in any given board 
state, by drawing arrows from the origin cell to the destination cell. 

Capture moves can have a different arrow colour than simple moves. 

Capture moves of defended pieces should have an extra arrow drawn that originates in the origin 
from which the piece can capture back and end on the capture square.
'''

board_parametrize = m.BoardState()

white_pawn = m.Pawn(
    colour='White',
    position='A2',
    board=board_parametrize
)

"""pytest_mark_pawn = pytest.mark.parametrize(
    'piece,board,legal_moves'
    [
        (white_pawn, board_parametrize, ()),
        (),
    ]
)"""


def setup_board():
    return m.BoardState()


class TestPiece:
    def test_chess_piece(self):
        assert isinstance(m.Rook(colour='White', position='A1', board=setup_board()), m.ChessPiece)

    def test_new_piece_board_update(self):
        board = setup_board()
        m.Rook(colour='White', position='A1', board=board)
        assert board.state == {'A1': 'Rook', 'B1': '', 'C1': '', 'D1': '', 'E1': '', 'F1': '', 'G1': '', 'H1': '', 'A2': '', 'B2': '', 'C2': '', 'D2': '', 'E2': '', 'F2': '', 'G2': '', 'H2': '', 'A3': '', 'B3': '', 'C3': '', 'D3': '', 'E3': '', 'F3': '', 'G3': '', 'H3': '', 'A4': '', 'B4': '', 'C4': '', 'D4': '', 'E4': '', 'F4': '', 'G4': '', 'H4': '', 'A5': '', 'B5': '', 'C5': '', 'D5': '', 'E5': '', 'F5': '', 'G5': '', 'H5': '', 'A6': '', 'B6': '', 'C6': '', 'D6': '', 'E6': '', 'F6': '', 'G6': '', 'H6': '', 'A7': '', 'B7': '', 'C7': '', 'D7': '', 'E7': '', 'F7': '', 'G7': '', 'H7': '', 'A8': '', 'B8': '', 'C8': '', 'D8': '', 'E8': '', 'F8': '', 'G8': '', 'H8': ''}

    def test_white_pawn(self):
        board = setup_board()
        white_a_pawn = m.Pawn(colour='White', position='A2', board=board)
        assert white_a_pawn.find_legal_moves_for() == ('A3', 'A4')

    def test_black_pawn(self):
        board = setup_board()
        black_b_pawn = m.Pawn(colour='Black', position='B7', board=board)
        assert black_b_pawn.find_legal_moves_for() == ('B6', 'B5')


class TestVisualisationEngine:
    def test_generate_legal_moves_for(self):
        board = setup_board()
        piece = m.Rook(colour='White', position='A1', board=board)
        assert m.generate_legal_moves_for(piece) == ('A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1')

    def test_generate_legal_moves_with_obstruction(self):
        board = setup_board()
        m.Pawn(colour='Black', position='A5', board=board)
        piece = m.Rook(colour='White', position='A1', board=board)

        assert m.generate_legal_moves_for(piece) == ('A2', 'A3', 'A4', 'A5', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1')

    def test_visualise_moves_for(self):
        ...


class TestBoard:
    def test_board_state(self):
        assert len(list(setup_board().state.keys())) == 64

