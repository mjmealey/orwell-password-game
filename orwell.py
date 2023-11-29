print("Welcome to the Orwell Password Game! You only have 3 attempts to guess the right year. Press Enter to Start")
input()

password = 1984
winner = "Orwell"


def game():
    number_of_attempts = 3
    remove_attempts_by = 1
    game_over = 0
    while number_of_attempts > game_over:
        try:
            guess_the_password = int(input("Guess the Year: "))
            if guess_the_password == password:
                print(winner)
                break
            else:
                if guess_the_password > password:
                    print(f"{guess_the_password} is greater than than the expected year.")
                elif guess_the_password < password:
                    print(f"{guess_the_password} is less than the expected year.")

                number_of_attempts -= remove_attempts_by
                if number_of_attempts != game_over:
                    print(f"You have {number_of_attempts} guesses left. Keep trying!")
                else:
                    print("You have ran out of attempts.")
        except ValueError as ve:
            print(f"Invalid Answer {ve}")


game()

