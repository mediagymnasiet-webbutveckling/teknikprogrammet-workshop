from random import randint
# print("Rock...")
# print("Paper...")
# print("Scissors...")

player = input("Gör ditt drag - sten, sax eller påse: ").lower()
rand_num = randint(0,2)
if rand_num == 0:
	computer = "sten"
elif rand_num == 1:
	computer = "påse"
else:
	computer = "sax"

print(f"Datorns tur {computer}" )

if player == computer:
	print("Lika!")
elif player == "sten":
	if computer == "sax":
		print("Du vinner!")
	else:
		print("Datorn vinner!")
elif player == "påse":
	if computer == "sten":
		print("Du vinner!")
	else:
		print("Datorn vinner!")
elif player == "sax":
	if computer == "påse":
		print("Du vinner!")
	else:
		print("Datorn vinner!")	
else:
	print("Skriv sten, sax eller påse!")