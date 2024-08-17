import random

def number_guessing_game():

    low = 1
    high = 50
    correct_answer = random.randint(low, high)  
    max_attempts = 5  

    print(f"Welcome to the Number Guessing Game!")
    print(f"Guess the number between {low} and {high}. You have {max_attempts} chances.")

    for attempt in range(max_attempts):
        try:
            
            guess = int(input("Enter your guess: "))
            
        
            if guess < low or guess > high:
                print(f"Please enter a number between {low} and {high}.")
                continue
            
        
            if guess == correct_answer:
                print("You Win!")
                break
            elif guess < correct_answer:
                print("Correct answer is greater!")
            else:
                print("Correct answer is smaller!")

            
            remaining_attempts = max_attempts - (attempt + 1)
            if remaining_attempts > 0:
                print(f"You have {remaining_attempts} chance(s) left.")
            else:
                print("You lose! The correct answer was", correct_answer)
        

        except ValueError:
            print("Invalid input. Please enter a valid number.")
number_guessing_game()
