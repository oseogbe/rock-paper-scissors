import random


options = {
    "R": "Rock",
    "P": "Paper",
    "S": "Scissors"
}

print("Welcome to the rock, paper, scissors game.")

while True:
    player_choice = input("Pick an option between R(Rock), P(Paper) and S(Scissors): ")

    if player_choice not in list(options.keys()):
        print("Invalid Input!")
        continue
    else:
        cpu_choice = random.choice(list(options.keys()))
        print(f"Player ({options.get(player_choice)}) : CPU ({options.get(cpu_choice)})")

        if player_choice == cpu_choice:
            print("Draw!")
            continue
        elif player_choice == 'R' and cpu_choice == 'S':
            print("Player Wins!")
            break
        elif player_choice == 'R' and cpu_choice == 'P':
            print("CPU Wins!")
            break
        elif player_choice == 'P' and cpu_choice == 'R':
            print("Player Wins!")
            break
        elif player_choice == 'P' and cpu_choice == 'S':
            print("CPU Wins!")
            break
        elif player_choice == 'S' and cpu_choice == 'P':
            print("Player Wins!")
            break
        elif player_choice == 'S' and cpu_choice == 'R':
            print("CPU Wins!")
            break
