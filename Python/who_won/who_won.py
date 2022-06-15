
class TicTak():
	def __init__(self, board):
		self.board = board

		self.rows = [row for row in self.board]
		# for i in range(len(self.board)):
		# 	col = []
		# 	for j in range(len(self.board[0])):
		# 		col.append(self.board[j][i])
		# 	self.cols.append(col)
		self.cols = [[self.board[j][i] 
				for j in range(len(self.board))] 
					for i in range(len(self.board))]
		self.diagonal_left_right = [[self.board[i][i] 
			for i in range(len(board))]]

		self.diagonal_right_left = [[self.board[i-1][-i] 
			for i in range(1,len(board)+1 ) ]]
		
		self.all_ = sum([self.rows, self.cols, 
			self.diagonal_left_right, self.diagonal_right_left], [])

		self.winner = [i for i in self.all_ if len(set(i)) == 1][0][0]

def who_won(board):
	t = TicTak(board)
	return t.winner

# Best Solution: "persolut"
# def who_won(board):
# 	return 'X' if sum(sq == 'X' for row 
# 			in board for sq in row) == 5 else 'O'



