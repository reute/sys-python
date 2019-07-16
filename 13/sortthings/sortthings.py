import random, sys

def einlesen_datei(namen):
	unsortiert = []
	for index, zeile in enumerate(open(namen, "r", encoding='utf-8', errors='ignore')):
		namen, hoehe = zeile.rstrip('\n').split(":")
		hoehe = int(hoehe)
		berg = namen, hoehe
		if index < MAX_BERGE:
			unsortiert.append(berg)
		else:
			r = random.randint(0, index)
			if r < MAX_BERGE:
				unsortiert[r] = berg
	return unsortiert

def ausgabe_spielstand(unsortiert, spieler):
	print("Current state:")
	for index, zeile in enumerate(spieler):
		print(str(index + 1) + ": " + zeile[0])
	print("Still to be sorted:")
	for index, zeile in enumerate(unsortiert):
		print(str(index + 1) + ": " + zeile[0])

def ausgabe_endergebnis(spieler):
	for zeile in spieler:		
		print("{0:5d} {1:s}".format(zeile[1], zeile[0]))

def eingabe_spieler():
	eingabe = (input("What is to be inserted where ? ")).split()
	eingabe = [int(i) for i in eingabe]
	return eingabe

def spieler_unsortiert(spieler):
	max_hoehe = 0
	for index, zeile in enumerate(spieler):		
		tmp = zeile[1]
		if tmp > max_hoehe:
			max_hoehe = tmp
		else:
			return True
	return False 

def einfuegen(berg, index_spieler, spieler):	
	if index_spieler > len(spieler):
		spieler.append(berg)
	else:
		spieler.insert(index_spieler, berg)
	return spieler

def entfernen(unsortiert, index_unsortiert):
	del unsortiert[index_unsortiert]
	return unsortiert

MAX_BERGE = 8
spieler = []
unsortiert = einlesen_datei("berge")

while True:
	ausgabe_spielstand(unsortiert, spieler)
	index_unsortiert, index_spieler = eingabe_spieler()
	if index_unsortiert == 0:
		break
	berg = unsortiert[index_unsortiert - 1]
	spieler = einfuegen(berg, index_spieler, spieler)
	unsortiert = entfernen(unsortiert, index_unsortiert)
	if spieler_unsortiert(spieler):	
		print("Sorry, then it is no longer sorted")	
		break
ausgabe_endergebnis(spieler)
