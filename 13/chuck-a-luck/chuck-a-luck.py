#!/usr/bin/env python3
# -*- coding: <utf-8> -*-

from random import randint

# komm
geld = 1000

def wuerfeln():
	return randint(1, 6)

print("**** Chuck-a-luck ****\nSie haben 1000 Geldeinheiten\nIn jeder Runde können Sie einen Teil davon auf eine der Zahlen 1 bis 6 setzen. Danach werden 3 Würfel geworfen. Falls Ihr Wert dabei ist, erhalten Sie Ihren Einsatz zurück und zusatzlich Ihren Einsatz fuer jeden Würfel,der die von Ihnen gesetzte Zahl zeigt.") 

while geld > 0:
	print(
		"Sie haben " + str(geld) + " Geldeinheiten")
	einsatz = int(input("Ihr Einsatz: "))
	if einsatz == 0:
		break
	zahl = int(input("Ihre Zahl: "))	
	print("Die Würfel sind gefallen:")
	gewinn = 0
	for i in range(3):
		wurf = wuerfeln()
		print(" " + str(wurf))
		if zahl == wurf:
			gewinn += einsatz	
	if gewinn > 0:
		geld += gewinn
		print("Glueckwunsch, Sie erhalten " + str(gewinn) + " Geldeinheiten!!")
	else:
		geld -= einsatz
		print("Pech, da war nichts fuer Sie dabei!!")


print("Glückwunsch, Sie verlassen das Casino mit " + str(geld) + " Geldeinheiten!!")