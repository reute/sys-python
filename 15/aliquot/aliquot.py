import random

def turn_player():
	while True:
		player = int(input('Your move: '))
		if number % player != 0:
			print('{0:d} is not a proper divisor of {1:d}!'.format(player, number))
		else:
			return player

def turn_comp():
	while True:
		comp = random.randint(1, number-1)
		if number % comp == 0:
			print('My Move: {0:d}'.format(comp))
			return comp

print('*** Aliquot Game ***')
number = random.randint(1, 100)

while True:
	print('Number: {0:d}'.format(number))
	player = turn_player()
	number -= player
	if number == 1:
		print('You win')
		break

	print('Number: {0:d}'.format(number))
	comp = turn_comp()
	number -= comp
	if number == 1:
		print('You lose')
		break




