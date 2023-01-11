from random import choice


def play(move):

    """Generates the computer's move and prints it. Prints and returns the result of the game."""

    computer_move = choice(("rock", "paper", "scissors"))
    print(computer_move)
    computer_move = computer_move[0]
    if computer_move == move:
        print("Draw!")
        return "draw"
    elif (computer_move == "r" and move == "p") or\
         (computer_move == "p" and move == "s") or\
         (computer_move == "s" and move == "r"):
        print("You win!")
        return "win"
    else:
        print("You lose...")
        return "loss"


player_score = 0
computer_score = 0
help_text = """
exit - prints the score and exits the game
help - prints out all commands and their descriptions
rock - plays rock
paper - plays paper
scissors - plays scissors
score - prints the score
r, p, s - shorthands for [r]ock, [p]aper and [s]cissors
"""
while True:
    command = input("Enter command: ").strip().lower()
    if command == "exit":
        print(f"You won {player_score} time(s). The computer won {computer_score} time(s).")
        break
    elif command == "help":
        print(help_text)
    elif command == "score":
        print(f"You won {player_score} time(s). The computer won {computer_score} time(s).")
    elif command in ("rock", "paper", "scissors", "r", "p", "s"):
        command = command[0]
        result = play(command)
        if result == "win":
            player_score += 1
        elif result == "loss":
            computer_score += 1
    else:
        print("Invalid input. Please try again.")
