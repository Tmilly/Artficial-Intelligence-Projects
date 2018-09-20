#Author: Torrance Graham

from konane import *	

class MinimaxPlayer(Konane, Player):
	def __init__(self, size, depthLimit):
		Konane.__init__(self, size)
		self.limit = depthLimit
	
	def initialize(self, side):
		#complete this
		self.side = side
		self.name = "The Danger Noodles"

	def getMove(self, board):
		#complete this
		moves= self.generateMoves(board, self.side)

		bestValue = float("-inf")
		bestMove = []
		for move in moves:
			currentBoard = self.nextBoard(board, self.side, move)
			alpha = self.minimax(currentBoard, self.limit-1, self.opponent(self.side), bestValue, float("inf"))
			if alpha > bestValue or bestMove == []:
				bestMove = move
				bestValue = alpha
		return bestMove
		
	def minimax(self, board, depth, player, alpha, beta):	
		#depth limit reached, return the heuristic value of the leaf node
		if depth == 0:
			return self.eval(board)
		
		#generate the next possible moves of the current board
		moves = self.generateMoves(board, player)
		
		#Minimax is currently testing our moves (Maximizing Player)
		if player == self.side:
			value = float("-inf")
			
			for move in moves:
				currentBoard = self.nextBoard(board, player, move)
				next = self.minimax(currentBoard, depth-1, self.opponent(player), alpha, beta)
				
				value = max(value,next)
				alpha = max(value,alpha)
					
				if beta <= alpha:
					break #beta cut-off
				
			return value
		
		#Minimax is currently testing our opponents moves (Minimizing Player)
		else: 
			value = float("inf")
			
			for move in moves:
				currentBoard = self.nextBoard(board, player, move)
				next = self.minimax(currentBoard, depth-1, self.opponent(player), alpha, beta)
				
				value = min(value,next)
				beta = min(value,beta)
				
				if beta <= alpha:
					break #alpha cut-off
				
			return value
					
	def eval(self, board):
		#number of opponentsMoves
		opponentMoves = self.generateMoves(board, self.opponent(self.side))
		return -len(opponentMoves)