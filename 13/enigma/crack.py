from collections import deque

CLEAR = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ")
key  = deque("EKLMF6GDQVZ0TO8Y XUSP2IB4CJ5AR197W3NH")

def eingabe_suchwort():
	return input("Suchwort eingeben: ")

def eingabe_chiffre():
	return input("Bitte Text zum entschlüsseln eingeben: ")

def knacken():
	text = [0] * len(chiffre)
	for i in range(len(key)):
		walze = deque(key)
		for i, cc in enumerate(chiffre):
			i_key = list(walze).index(cc)
			text[i] = CLEAR[i_key];
			walze.rotate(-1)	
		klartext = "".join(text)
		if suchwort in klartext:
			return klartext
		key.rotate(-1)

suchwort = eingabe_suchwort().upper()
chiffre = eingabe_chiffre()
klartext = knacken()
if klartext is not None:
	print("Lösung gefunden !\nEntschlüsselter Text: \n" + str(klartext))
else:
	print("Keine Lösung")
