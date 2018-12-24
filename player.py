import random

class Player(object):

	def __init__(self):
		return

	def play(self, num_stones):
		# return list of integers
		raise Exception("play not defined for some Player")
		return


class HumanPlayer(Player):

	def __init__(self):
		return

	def play(self, num_stones, GS):

		for i in range(num_stones):
			print GS
			choice = int(raw_input("Column to place a stone in.\n"))
			GS.place_stone(choice)


class RandomPlayer(Player):

	def __init__(self):

		return

	def play(self, num_stones, GS):

		for i in range(num_stones):
			choices = [i for i in range(len(GS.grid[0])) if GS.grid[0][i] == -1]
			index = random.randrange(len(choices))
			GS.place_stone(choices[index])

			print GS



class MiniMaxPlayer(Player):

	def __init__(self):
		return

