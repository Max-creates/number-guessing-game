from random import randint

lower_num, higher_num = 1, 10
random_number: int = randint(lower_num, higher_num)
print(f"Guess the number in the range from {lower_num} to {higher_num}.\n"
      f"You have 3 tries.")
tries = 3
while True:
    try:
        user_guess: int = int(input('Guess: '))
    except ValueError as e:
        print('Please a valid number.')
        continue
    
    if user_guess > random_number:
        if tries > 1:
            print("The number is lower")
            tries = tries - 1
            print(f"Tries left: {tries}")
        else:
            print(f"No tries left..."
                  f"Game Over")
            break
    elif user_guess < random_number:
        if tries > 1:
            print("The number is higher")
            tries = tries - 1
            print(f"Tries left: {tries}")
        else:
            print(f"No tries left..."
                  f"Game Over")
            break
    else:
        print("You guessed!")
        break
        
        
        
