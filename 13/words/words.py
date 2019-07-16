def einlesen_datei(namen):
	liste = []
	for zeile in open(namen, "r", encoding='utf-8', errors='ignore'):
		zeile = zeile.rstrip('\n')
		liste.append(zeile)
	return liste

def passt_vorne(wort, kette):
	if wort[-1] == kette[0][0]:
		return True
	else
		return False

def passt_hinten(wort, kette):
	if wort[0] == kette[-1][-1]:
		return True
	else
		return False

def add_wort(wort, kette):
	if passt_vorne(wort, kette):	
		kette.insert(wort, 0)
	if passt_hinten(wort, kette):
		kette.append(wort)
	return kette	

def woerter_aufgebraucht(liste, kette):
	for wort in liste:
		if passt_vorne(wort, kette) or passt_hinten(wort, kette):
			return False
	return True	

def zeige_liste(liste):
	for wort in liste:
		print(wort)

def eingabe_spieler():
	return input("Next word: ")

kette = ["hallo"]
liste = einlesen_datei("cities.txt")
print(str(len(liste)) + " words left.")

while True:
	wort = eingabe_spieler()
	if wort == "q":
		break
	if wort = "":
		zeige_liste(liste)
		continue
	if wort in liste:
		print("Wort vorhanden")
		neue_kette = add_wort(wort, kette)
		if kette == neue_kette:
			print("Passt nicht !")
			continue
		else: 
			kette = neue_kette
			liste.remove(wort)
			print("Hinzugefügt !")
	else:
		print("Wort nicht in Liste !")

	print(str(len(liste)) + " words left.")
	print("Current chain of " + str(len(kette)) + " words: " + kette[0] + " ... " + kette[-1])
	if woerter_aufgebraucht(liste, kette):
		print("No further words matching, starting with new chain")
		kette = []


