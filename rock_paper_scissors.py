import random
rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
player_choice = input("Choose [r]rock, [p]aper or [s]cissors: ")
if player_choice == 'r':
    player_choice = rock
elif player_choice == 'p':
    player_choice = paper
elif player_choice == 's':
    player_choice = scissors
else:
    raise SystemExit("Invalid Input. Try again...")


computer_random_number = random.randint(1, 3)
computer_move = ''
if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
elif computer_random_number == 3:
    computer_move = scissors
print(f"The computer chose {computer_move}")

if (player_choice == rock and computer_move == scissors) or \
        (player_choice == paper and computer_move == rock) or \
        (player_choice == scissors and computer_move == paper):
    print("You win!")
elif player_choice == computer_move:
    print("Draw!")
else:
    print("You lose!")
