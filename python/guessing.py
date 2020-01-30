import random

random_number = random.randint(1,10)  # numbers 1 - 10
guess = None

while True:
	guess = input("Välj ett nummer mellan 1 och 10: ")
	guess = int(guess)
	if guess < random_number:
		print("För lågt!")
	elif guess > random_number:
		print("För högt!")
	else:
		print("Du vann!!!!")
		play_again = input("Vill du spela igen (y/n) ")
		if play_again == "y":
			random_number = random.randint(1,10)  # numbers 1 - 10
			guess = None
		else:
			print("Tack för att du spelade :-)")
			break

