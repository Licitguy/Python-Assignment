print ("Welcome to quiz ")
user_choice = input ("Ready to start quiz ")

correct_number = 7
if user_choice == "yes":
	user_choice = eval(input("enter a number from 5 to 15 "))	
	
	if user_choice == correct_number:
		print("you win")
	else:
		print("You lose")
elif user_choice == "no":
	print("try again later")
else:
	print("nice try")

	