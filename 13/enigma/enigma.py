from collections import deque

MAX_ZEICHEN = 37
clear = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ")
key  = deque("EKLMF6GDQVZ0TO8Y XUSP2IB4CJ5AR197W3NH")

def verschlüsseln(text, walzenstellung):
	for i, c in enumerate(text):	
		if c not in clear:
			i_key = clear.index(" ")
		else:
			i_key = clear.index(c)
		text[i] = key[i_key];		
		key.rotate(-1)
	print("Verschlüsselter Text: " + str(text))

def entschlüsseln(text, walzenstellung):
	for i, c in enumerate(text):
		i_key = list(key).index(c)
		text[i] = clear[i_key];
		key.rotate(-1)
	print("Entschluesselter Text:\n" + str(text));

def eingabe_auswahl():
	while True:
		try:
			eingabe = int(input("1 - Verschlüsseln\n2 - Entschlüsseln\n"))
			if eingabe not in range(1, 3):
				print("Bitte wiederholen")
			else:
				break
		except ValueError:
			print("Bitte wiederholen")
	return eingabe

def eingabe_text():
	return list(input("Bitte Text eingeben: ").upper())

def eingabe_walzenstellung():
	while True:
		try:
			eingabe = int(input("Bitte Walzenstellung eingeben (0 - " + str(MAX_ZEICHEN) + ") ")) 
			if eingabe not in range(38):
				print("Bitte wiederholen")
			else:
				break
		except ValueError:
			print("Bitte wiederholen")
	return eingabe

print(" * * * * ENIGMA * * * * *")
text = eingabe_text()
auswahl = eingabe_auswahl()
walzenstellung = eingabe_walzenstellung()
key.rotate(walzenstellung * -1)
if auswahl == 1:
	verschlüsseln(text, walzenstellung)
elif auswahl == 2:
	entschlüsseln(text, walzenstellung)
