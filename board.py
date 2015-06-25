import numpy as np


class chessPiece(object):
	def __init__(self, name):
		self.name = name


# board = {'a': {}, '' : {} }
Z = np.zeros((8,8),dtype=chessPiece)
# Z[1::2,::2] = '1'
Z[0,0] = chessPiece('hello')
# Z[::2,1::2] = '1'
print Z[0,0].name