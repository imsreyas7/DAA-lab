class Queens:
	
	def __init__(self, n):
		self.board = [[0 for i in range(n)] for j in range(n)]
		self.n = n

	def printBoard(self):
		for i in range(self.n):
			for j in range(self.n):
				print(self.board[i][j], end = "  ")
			print("\n")

	def isSafe(self, row, col):
		#check this row in left side
		for i in range(col):
			if(self.board[row][i] == 1):
				return False
		
		#check left side of upper diagonal
		i, j = row, col
		
		for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
			if(self.board[i][j] == 1):
				return False
			
		
		#check left side of lower diagonal
		i, j = row, col
		
		for i, j in zip(range(row, self.n, -1), range(col, -1, -1)):
			if(self.board[i][j] == 1):
				return False

		#if the conditions above aren't satisfied, then the board is in a safe state.
		return True
	
	
	def solveBoard(self, col):
		if(col >= self.n):	#base case, all columns are checked.
			print("Final Configuration: \n")
			self.printBoard()
			return True	#if this statement is removed, all solutions will be printed

		for i in range(self.n):
			if(self.isSafe(i, col) == True):	#if the board is in a safe state, place Queen in the ith row
				self.board[i][col] = 1
				if(self.solveBoard(col+1) == True):	#check recursively if it is solvable with current state
										
					return True	#if solvable, return True
				else:					#if the board isn't in a safe state, do not place Queen in that row. 
					self.board[i][col] = 0
		
		return False	#if the configuration is unsolvable, return False, so that other configurations are tried.


if __name__ == "__main__":

	queens_8 = Queens(8)
	print("\n\tInital Configuration: \n")
	queens_8.printBoard()

	print("\n\t\tSolving the Board\n")
	final = queens_8.solveBoard(0)

	if(final == False):
		print("\nThe board was not solvable.")

'''
(base) C:\Users\sreya>cd desktop

(base) C:\Users\sreya\Desktop>cd labs/DAA/Backtracking

(base) C:\Users\sreya\Desktop\labs\DAA\Backtracking>python nqueens.py

        Inital Configuration:

0  0  0  0  0  0  0  0

0  0  0  0  0  0  0  0

0  0  0  0  0  0  0  0

0  0  0  0  0  0  0  0

0  0  0  0  0  0  0  0

0  0  0  0  0  0  0  0

0  0  0  0  0  0  0  0

0  0  0  0  0  0  0  0


                Solving the Board

Final Configuration:

1  0  0  0  0  0  0  0

0  0  0  0  0  0  1  0

0  1  0  0  0  0  0  0

0  0  0  0  0  1  0  0

0  0  0  0  0  0  0  1

0  0  1  0  0  0  0  0

0  0  0  0  1  0  0  0

0  0  0  1  0  0  0  0


(base) C:\Users\sreya\Desktop\labs\DAA\Backtracking>

'''