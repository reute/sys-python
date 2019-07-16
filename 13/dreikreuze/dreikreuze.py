
from random import randint

word_bit = 23
spielfeld = 0
gewinner = ""

def feld_belegt(pos):
	tmp = 1 << pos
	if tmp & spielfeld == tmp:
		return True
	else:
		return False

def feld_belegen(pos):
	global spielfeld
	if not feld_belegt(pos):
		tmp = 1 << pos
		spielfeld = spielfeld | tmp
		return True
	else:
		return False

def zeichne_spielfeld():
	for i in range(1, word_bit + 1):
		if feld_belegt(i):
			print("\\/", end=" ")
		else:
			print("  ", end=" ")
	print()

	for i in range(1, word_bit + 1):
		if feld_belegt(i):
			print("/\\", end=" ")
		else:
			print("  ", end=" ")	
	print()	

	for i in range(1, word_bit + 1):
		print('{0:02}'.format(i), end=" ")
	print()

def zug_computer():
	while True:
		zug = randint(1, word_bit)
		if feld_belegen(zug):
			return zug
			break		

def zug_spieler():
	while True:
		try:
			zug = int(input("Your move: "))
		except ValueError:			
			print("Bitte Zahl zwischen 1 und " + str(word_bit) + " eingeben")
			continue
		if zug <= 0 or zug > word_bit:
			print("Bitte Zahl zwischen 1 und " + str(word_bit) + " eingeben")
		elif feld_belegt(zug):
			print("Feld schon belegt, bitte freies Feld auswählen")
		else:
			feld_belegen(zug)
			return zug

def gewonnen():
	kreuze = 0
	for i in range(word_bit):
		if feld_belegt(i):
			kreuze += 1
			if kreuze == 3:
				return True
		else:
			kreuze = 0
	return False

print("*** Drei Kreuze ***\nGegeben ist eine Kette von 23 freien Feldern. In jedem Zug setzt jeder der Spieler ein X auf ein freies Feld. Wenn dadurch drei oder mehr X benachbart sind, hat der Spieler gewonnen.  ")
sp_anfangen = int(input("Wollen Sie anfangen? Ja=1 Nein=2 "))
print("\n")
if sp_anfangen == 1:
	zug_spieler()	
	zeichne_spielfeld()

while spielfeld < 2 ** word_bit:
	zug = zug_computer()
	print("Computer sets X at position " + str(zug))
	zeichne_spielfeld()
	if gewonnen():
		gewinner = "com"
		break
	zug = zug_spieler()
	zeichne_spielfeld()
	if gewonnen():
		gewinner = "spieler"
		break

if gewinner == "com":
	print("You lose !")
elif gewinner == "spieler":
	print("Gewonnen !")
