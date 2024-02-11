import src.main as m

'''
This program aims to provide visual representation of all legal chess moves in any given board 
state, by drawing arrows from the origin cell to the destination cell. 

Capture moves can have a different arrow colour than simple moves. 

Capture moves of defended pieces should have an extra arrow drawn that originates in the origin 
from which the piece can capture back and end on the capture square.
'''


def setup():
    name = 'Rook'
    colour = 'White'
    position = ('A', '1')

    return m.ChessPiece(name, colour, position)


def test_chess_piece():
    assert isinstance(setup(), m.ChessPiece)


def test_generate_legal_moves_for():
    rook = setup()
    assert m.generate_legal_moves_for(rook) == ('A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1')


def test_visualise_moves_for():
    ...
