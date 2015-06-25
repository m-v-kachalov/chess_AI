import numpy as np

class pieceTypes:
	PAWN = 1
	KNIGHT = 2
	BISHOP = 3
	ROOK = 4
	QUEEN = 5
	KING = 6

class chessPiece(object):
	def __init__(self, pieceType):
		self.pieceType = pieceType



# what is the best way to represent a board??
Z = np.zeros((8,8),dtype=chessPiece)
Z[0,0] = chessPiece(pieceTypes.PAWN)
# Z[::2,1::2] = '1'
print Z[0,0].pieceType