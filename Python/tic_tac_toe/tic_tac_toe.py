def tic_tac_toe(inputs):
	rows = [row for row in inputs]
	cols = [] 
	for i in range(len(inputs)):
		col = [] 
		for row in inputs:
			col.append(row[i])
		cols.append(col)
	arr = [rows] + [cols]
	diagonals = []
	left = [inputs[i][i] for i in range(len(inputs))]
	
	right = []
	for i in range(0, len(inputs)):

		right.append( inputs[i][-i-1] )
	winner = {
	"X" : "Player 1 wins",
	"O" : "Player 2 wins",
	}
	diagonals = [left] + [right]
	for row in rows:
		if len(set(row)) != 1:
			next
		else:
			return winner[list(set(row))[0]]
	for col in cols:
		if len(set(col)) != 1:
			print(set(col))
			next
		else:
			return winner[list(set(col))[0]]
	for diagonal in diagonals:
		if len(set(diagonal)) != 1:
			print(set(diagonal))
			next
		else:
			return winner[list(set(diagonal))[0]]
	return "It's a Tie"



print( 
tic_tac_toe(
 [["X", "O", "O"],
  ["O", "X", "O"],
  ["O", "#", "X"]])
)