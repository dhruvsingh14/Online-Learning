# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if (user_choice == 'r' and computer_choice == 's') or (user_choice == 'p' and computer_choice == 'r') or (user_choice == 's' and computer_choice == 'p'):
   print("I won")
elif (computer_choice == 'r' and user_choice == 's') or (computer_choice == 'p' and user_choice == 'r') or (computer_choice == 's' and user_choice == 'p'):
    print("I won")
else:
    print("It's a tie!")

