import random

def generate_secret_number():
    """Generate a random 4-digit number with unique digits"""
    digits = list(range(10))
    random.shuffle(digits)
    return ''.join(map(str, digits[:4]))

def calculate_cows_and_bulls(secret, guess):
    """Calculate the number of cows and bulls for a guess"""
    cows = 0
    bulls = 0
    
    # Count cows (correct digit in correct position)
    for i in range(4):
        if secret[i] == guess[i]:
            cows += 1
    
    # Count bulls (correct digit in wrong position)
    for digit in guess:
        if digit in secret:
            bulls += 1
    
    # Subtract cows from bulls to get actual bulls
    bulls -= cows
    
    return cows, bulls

def is_valid_guess(guess):
    """Check if the guess is a valid 4-digit number"""
    if len(guess) != 4:
        return False, "Please enter exactly 4 digits."
    
    if not guess.isdigit():
        return False, "Please enter only numbers."
    
    return True, ""

def play_game():
    """Main game function"""
    print("🐄🐂 Welcome to Cows and Bulls! 🐂🐄")
    print("=" * 40)
    print("I've generated a secret 4-digit number.")
    print("Your goal is to guess it!")
    print("\nRules:")
    print("• COWS = Correct digit in correct position")
    print("• BULLS = Correct digit in wrong position")
    print("=" * 40)
    
    secret_number = generate_secret_number()
    guess_count = 0
    game_over = False
    
    # For debugging - uncomment the line below to see the secret number
    # print(f"DEBUG: Secret number is {secret_number}")
    
    while not game_over:
        print(f"\nGuess #{guess_count + 1}")
        guess = input("Enter your 4-digit guess: ").strip()
        
        # Validate the guess
        valid, error_message = is_valid_guess(guess)
        if not valid:
            print(f"❌ {error_message}")
            continue
        
        guess_count += 1
        
        # Check if the guess is correct
        if guess == secret_number:
            print(f"\n🎉 CONGRATULATIONS! 🎉")
            print(f"You guessed the number {secret_number} correctly!")
            print(f"It took you {guess_count} guess{'es' if guess_count != 1 else ''}!")
            game_over = True
        else:
            # Calculate cows and bulls
            cows, bulls = calculate_cows_and_bulls(secret_number, guess)
            print(f"Result: {cows} cow{'s' if cows != 1 else ''} 🐄, {bulls} bull{'s' if bulls != 1 else ''} 🐂")
            
            # Give some encouragement
            if cows + bulls == 0:
                print("💭 No correct digits. Try completely different numbers!")
            elif cows == 0 and bulls > 0:
                print("💭 You have some correct digits, but they're all in wrong positions!")
            elif cows > 0 and bulls == 0:
                print("💭 Some digits are in the right positions!")
            else:
                print("💭 You're getting closer! Mix of right positions and wrong positions.")

def main():
    """Main function to handle game loop and replay"""
    while True:
        play_game()
        
        print("\n" + "=" * 40)
        play_again = input("Would you like to play again? (y/n): ").strip().lower()
        
        if play_again not in ['y', 'yes']:
            print("\nThanks for playing Cows and Bulls! 👋")
            break
        else:
            print("\n" * 2)  # Add some space before new game

if __name__ == "__main__":
    main()