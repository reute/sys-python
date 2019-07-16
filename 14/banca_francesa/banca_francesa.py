from random import randint

class Kombination:

	def __init__(self, name, summe, quote):
		self.name = name
		self.summe = summe
		self.quote = quote

kombi = {}
kombi['aces'] = Kombination("Aces", [3], 61) 
kombi['pequeno'] = Kombination("Pequeno", list(range(5,8)), 1)
kombi['grande'] = Kombination("Grande", list(range(14,17)), 1)

kombi_list = [kombi['aces'], kombi['pequeno'], kombi['grande']]
konto = 1000
runde = []

print("*****Banca Francesa*****\nIn jeder Runde koennen Sie einen Teil Ihres Geldes auf eine der folgenden Kombinationen setzen:\n1: Aces, Augensumme: 3 mit einer Gewinnquote von 1 : 61.\n2: Pequeno, Augensumme: 5 6 7 mit einer Gewinnquote von 1 : 1.\n3: Grande, Augensumme: 14 15 16 mit einer Gewinnquote von 1 : 1.")

while konto > 0:
	print('Kontostand: {0:d}'.format(konto))
	eingabe = input("Einsatz und Kombination: ").split(" ")
	einsatz, tip_in = [int(i) for i in eingabe] 
	if einsatz > konto:
		print('Einsatz darf Konto nicht übersteigen')
		continue
	tip = kombi_list[tip_in - 1]
	resultat = None	

	print("{0:d} auf {1:s} gesetzt.".format(einsatz, tip.name))

	while resultat == None:
		del runde[:]
		for i in range(3):
			runde.append(randint(1, 6))
		summe = sum(runde)
		print("Würfel: {0:d} {1:d} {2:d} mit einer Augensumme von {3:d}".format(runde[0], runde[1], runde[2], summe))
		if summe in kombi['aces'].summe:
			resultat = kombi['aces']
		elif summe in kombi['pequeno'].summe:
			resultat = kombi['pequeno']
		elif summe in kombi['grande'].summe:
			resultat = kombi['grande']
		else:
			resultat = None
			print("Nichts passiert.")

	print(resultat.name + "!")
	if resultat == tip:
		gewinn = einsatz * tip.quote	
		print('Sie gewinnen {0:d}'.format(gewinn))	
	else:
		print('Sie verlieren {0:d}'.format(einsatz))
		gewinn = einsatz * -1
	konto += gewinn
	






