#!/usr/bin/env python3
# -*- coding: <utf-8> -*-

from random import randint

def wuerfeln():
	return randint(1, 6)

def berechneGewinn(wuerfe, zahl, einsatz):
	gewinn = 0
	for wurf in wuerfe:
		if zahl == wurf:	# treffer			
			gewinn += einsatz
	if gewinn == 0:			# kein treffer
		gewinn = -einsatz			
	return gewinn

geld = 1000
anzahlWuerfeProRunde = 3

print("**** Chuck-a-luck ****\nSie haben 1000 Geldeinheiten\nIn jeder Runde können Sie einen Teil davon auf eine der Zahlen 1 bis 6 setzen. Danach werden 3 Würfel geworfen. Falls Ihr Wert dabei ist, erhalten Sie Ihren Einsatz zurück und zusatzlich Ihren Einsatz fuer jeden Würfel,der die von Ihnen gesetzte Zahl zeigt.") 

while geld > 0:
	print("Sie haben " + str(geld) + " Geldeinheiten")
	einsatz = int(input("Ihr Einsatz: "))
	if einsatz == 0:
		break
	zahl = int(input("Ihre Zahl: "))	
	print("Die Würfel sind gefallen:")
	wuerfe = []
	for i in range(anzahlWuerfeProRunde):
		wurf = wuerfeln()
		print(" " + str(wurf))
		wuerfe.append(wurf)
	gewinn = berechneGewinn(wuerfe, zahl, einsatz)
	if gewinn > 0:	
		print("Glueckwunsch, Sie erhalten " + str(gewinn) + " Geldeinheiten!!")
	else:	
		print("Pech, da war nichts fuer Sie dabei!!")
	geld += gewinn

print("Glückwunsch, Sie verlassen das Casino mit " + str(geld) + " Geldeinheiten!!")