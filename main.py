import argparse

from game_state import GameState
from player import RandomPlayer, HumanPlayer

def main(p1, p2, stones_per_turn):
	
	players = []
	if p1 == 'human' or p1 == 'h':
		players.append(HumanPlayer())
	elif p1 == 'random' or p1 == 'r':
		players.append(RandomPlayer())
	else:
		raise Exception("Unkown player 1 type.")

	if p2 == 'human' or p2 == 'h':
		players.append(HumanPlayer())
	elif p2 == 'random' or p2 == 'r':
		players.append(RandomPlayer())
	else:
		raise Exception("Unkown player 2 type.")
	
	GS = GameState(stones_per_turn, players)

	while not GS.game_is_over():
		GS.play()

	return

if __name__ == "__main__":

	parser = argparse.ArgumentParser()

	parser.add_argument('p1', help='Type of agent. Options: human, random, ...')

	parser.add_argument('p2', help='Type of agent. Options: human, random, ...')
	
	# Optional Arguments
	parser.add_argument('-s', help='Stones per turn. Defaults to 1.', dest='stones_per_turn', default=1, type=int)


	args = parser.parse_args()


	main(p1=args.p1, p2=args.p2, stones_per_turn=args.stones_per_turn)