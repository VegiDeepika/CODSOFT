import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def main():
    user_score = 0
    computer_score = 0
    rounds = 0

    print("Welcome to Rock-Paper-Scissors Game!")
    
    while True:
        print("\nRound", rounds + 1)
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        while user_choice not in ['rock', 'paper', 'scissors']:
            user_choice = input("Invalid choice. Please choose rock, paper, or scissors: ").lower()
        
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        if winner == 'user':
            print("You win this round!")
            user_score += 1
        elif winner == 'computer':
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("It's a tie!")

        rounds += 1
        print(f"Score -> You: {user_score} | Computer: {computer_score}")
        
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break
    
    print("\nGame Over!")
    print(f"Final Score after {rounds} rounds -> You: {user_score} | Computer: {computer_score}")
    if user_score > computer_score:
        print("Congratulations! You won the game!")
    elif user_score < computer_score:
        print("Computer won the game! Better luck next time!")
    else:
        print("It's a tie game!")

if __name__ == "__main__":
    main()

