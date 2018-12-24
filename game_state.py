

class GameState(object):

	def __init__(self, stones_per_turn, players, width=None, height=None):

		self.width = 7
		self.height = 6

		self.grid = [[-1 for _ in range(self.width)] for _ in range(self.height)]
		# -1 is empty, 0 is player 1 and 1 is player 2
		print self.grid

		self.players = players

		self.turn = 0
		self.stones_per_turn = 1
		self.needed_to_win = 4

	def __str__(self):
		for i in self.grid:
			s = []
			for x in i:
				if x != -1:
					s.append("{:>2}".format(x))
				else:
					s.append("{:>2}".format('_'))
			print ' '.join(s)
		return ''

	def play(self):

		self.players[self.turn].play(self.stones_per_turn, self)

		# increment player
		self.turn += 1
		self.turn = self.turn % 2

	def place_stone(self, col):
		if col >= self.width:
			raise Exception("Tried to place in column index {0} of {1}.".format(col, self.width-1))
			
		i = self.height-1
		while self.grid[i][col] != -1:
			if i == 0:
				raise Exception("Tried to place in full column.")
			i -= 1
		
		self.grid[i][col] = self.turn


	def game_is_over(self):

		# TD: add check for self.stones_per_turn in a row

		return -1 not in self.grid[0]




