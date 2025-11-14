# -------------------------------------------------------------------------------------------
# File: Word_Ella_Marcus.py
# By: Ella Marcus
# Date: 11/4/2025
# Description: Play Guess the Word game where user guesses a word.
# -------------------------------------------------------------------------------------------
# Pseudocode for Guess the Word:
# import random for game
# set lists for categories
#     animal list
#     foods list
#     sports list
# Define ask_level()
#     while loop- while true
#         set level = input(
#             f"Please choose your difficulty level: "
#             (easy [10 tries] / medium [8 tries] / hard [6 tries]) "
#         ).strip().lower()
#         if level input not in easy or medium or hard:
#             print "Invalid level entered. Please try again."
#             continue
#         return level for later uses
# Define ask_category()
#     while loop- while true
#         set category = input(f"Please enter a category: (animals / foods / sports): ").strip().lower()
#         if category input not in animals or foods or sports:
#             print "Invalid category entered. Please try again."
#             continue
#         return category for later uses
# Define pick_random(category_name)
#     if category_name = animals:
#         set category to animals
#     if category_name = foods:
#         set category to foods
#     else:
#         set category to sports
#     set random_word to random.choice(category)
#     return random_word
# Define game_level(level):
#     set tries to 0
#     if level input is easy:
#         set count to 10
#     elif level input is medium:
#         set count to 8
#     else:
#         set count to 6
#     return count, tries for later usage
# Define output(word, guessed_letters, count, tries)
#     for letter in word loop
#         if letter in guessed_letters:
#             print (letter, end=" ")
#         else:
#             print ("_", end=" ")
#     print()
#     print(f"Remaining tries = {count - tries}")
#     print(f"Guessed letters = {sorted(guessed_letters)}")
# Define hint(tries, word, guessed_letters, count)
#     add 2 hint to tries
#     for letter in word loop
#         if letter not in guessed_letters:
#             print(f"Your revealed letter is {letter}")
#             guessed_letters.append(letter)
#             break
#     call output function- output(word, guessed_letters, count, tries)
#     return tries
# Define validate_word_input(user_guess, guessed_letters)
#     if user_guess is hint:
#         return False
#     if len(user_guess) is more than 1 or not a letter:
#         print("Please enter 1 valid letter or the word 'hint'.")
#         return True
#     if user_guess is in guessed_letters:
#         print(f"You have already guessed this letter. Please enter another letter besides for those that have "
#               f"already been guessed: {guessed_letters}")
#         return True
#     return False
# Define game_win(word, guessed_letters)
#     if all (letter in guessed_letters for letter in word):
#         print(f"You Win! You guessed all the letters in the word '{word}'.")
#         return True
#     return False
# Define game_response(user_guess, tries, word, count, guessed_letters)
#     if user_guess not in word:
#         add 1 to tries
#     call output(word, guessed_letters, count, tries)
#     return tries
# Define play_again()
#     while loop for true
#         set again to input(f"Would you like to play again? (y/n) ").strip().lower()
#         if again not in y or n
#             print "Please enter a valid response in y/n."
#             continue
#     if again is "y":
#         return True
#     else:
#         return False
# Define guess_input(count, tries, word, guessed_letters, wins)
#     while loop for True
#         set user_guess to input("Please guess a letter or enter 'hint' (costs two tries): ").strip().lower()
#         if user_guess is "hint":
#             if count - tries is less than 2:
#                 print "Not enough tries left for a hint. Please guess a letter."
#                 continue
#             set tries to function hint(tries, word, guessed_letters, count)
#             if game_win(word, guessed_letters):
#                 break
#             continue
#         if validate_word_input(user_guess, guessed_letters):
#             continue
#         else:
#             break
#     return tries, user_guess
# Define play_game(wins, losses, word, count, tries)
#     set guessed_letters to be empty list
#     while tries less than count loop
#         set tries and user_guess to guess_input(count, tries, word, guessed_letters, wins)
#         guessed_letters.append(user_guess)
#         if game_win(word, guessed_letters):
#             add 1 to wins
#             break
#         set tries to game_response(user_guess, tries, word, count, guessed_letters)
#     else:
#         print "No more tries left. Game failed."
#         print f"Your secret word was {word}."
#         add 1 to losses
#     return wins, losses
# Define end_output(wins, losses)
#     print f"Good Game!"
#     print f"wins: {wins}"
#     print f"losses: {losses}"
# Define main()
#     print "Welcome to Guess the Word!"
#     print "You will pick a level and category, and then try to guess the word one letter at a time!"
#     set wins = 0
#     set losses = 0
#     while True loop
#         set level = ask_level()
#         set category_name = ask_category()
#         set word = pick_random(category_name)
#         set count, tries = game_level(level)
#         set wins, losses = play_game(wins, losses, word, count, tries)
#         if not play_again():
#             break
#     end_output(wins, losses)
# if __name__ == "__main__":
#     main()


import random
animals = [
    "tiger", "lion", "bear", "giraffe", "elephant", "zebra", "turtle", "leopard", "wolf", "deer", "kangaroo",
    "panda", "fox", "monkey", "penguin", "owl", "rabbit", "dog", "cat", "camel"
]
foods = [
    "pizza", "bagel", "apple", "cake", "chicken", "banana", "bread", "yogurt", "pasta", "cheese", "potato",
    "burger", "sushi", "chocolate", "muffin", "spinach", "cucumbers", "pepper", "popcorn", "donut"
]
sports = [
    "swimming", "rugby", "surfing", "running", "snowboarding", "sledding", "boxing", "basketball", "tennis",
    "baseball", "football", "handball", "gymnastics", "fencing", "volleyball", "cricket", "golf", "hockey",
    "cycling", "soccer"
]

def ask_level():
    """
    Prompt the user for a level and reprompt an invalid input.

    In a while loop (continues until True), ask for a valid level from easy/medium/hard.
    Print an error if an incorrect level is given.
    Reprompt the user until a correct level is entered.
    Prompt for:
        1. level
    Returns:
        str: the string that user enters as input
    """
    # Set loop to go on forever until user enters a valid level.
    while True:
        level = input(
            f"Please choose your difficulty level: "
            f"(easy [10 tries] / medium [8 tries] / hard [6 tries]) "
        ).strip().lower()
        if level not in ("easy", "medium", "hard"):  # Prompt error if level is not valid
            print(f"Invalid level entered. Please try again.")
            continue
        return level


def ask_category():
    """
    Prompt the user for a category and reprompt an invalid input.

    In a while loop (continues until True), ask for a valid category from animals/food/sports.
    Print an error if an incorrect category is given.
    Reprompt the user until a correct category is entered.
    Prompt for:
        1. category
    Returns:
        str: the string that user enters as input
    """
    # Set loop to go on forever until user enters valid category
    while True:
        category = input(f"Please enter a category: (animals / foods / sports): ").strip().lower()
        if category not in ("animals", "foods", "sports"):  # Error if invalid category entered
            print(f"Invalid category entered. Please try again. ")
            continue
        return category


def pick_random(category_name):
    """
    Pick random word from the lists defined above.

    Set the input from the user to one of the three categories.
    Use random to choose a random word from the chosen category.
    Parameters:
        category_name (str): name of category user picked
    Returns:
        str: random word chosen from category list
    """
    # Set category to user input
    if category_name == "animals":
        category = animals
    elif category_name == "foods":
        category = foods
    else:
        category = sports
    random_word = random.choice(category)  # Choose random word from category list
    return random_word


def game_level(level):
    """
    Set count of attempt allowed based on user choice of level.

    Set count to 10/8/6 based off user's choice of easy/medium/hard.
    Parameters:
        level (str): name of level user picked
    Returns:
        tuple: count of how many attempts user can have and tries of how many attempts by user
    """
    # Track tries of user for duration of game
    tries = 0
    # Set tries based on level
    if level == "easy":
        count = 10
    elif level == "medium":
        count = 8
    else:
        count = 6
    return count, tries


def output(word, guessed_letters, count, tries):
    """
    Print output of word, remaining tries, and guessed letters.

    Use a for loop to loop through letters in the random word.
    If letter was already guessed print letter, if not print _.
    Print remaining tries and guessed letters list.
    Parameters:
        word (str): random word user is trying to figure out
        guessed_letters (str): letters already guessed by the user
        count (int): attempts allowed based on level
        tries (int): number of attempt of user so far
    """
    # Use for loop to go through letters in random word
    for letter in word:
        if letter in guessed_letters:  # Reveal guessed letters, otherwise use '_'
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()
    print(f"Remaining tries = {count - tries}")
    print(f"Guessed letters = {sorted(guessed_letters)}")


def hint(tries, word, guessed_letters, count):
    """
    Print a letter hint, add 2 to tries of user, and print word output

    Add 2 to tries of the user.
    Use a for loop to loop through letters of random word.
    Print the first letter that hasn't been guessed.
    Add hint letter to guessed letters list.
    Call output function to print output of letters and remaining tries.
    Parameters:
        tries (int): number of attempt of user so far
        word (str): random word user is trying to figure out
        guessed_letters (str): letters already guessed by the user
        count (int): attempts allowed based on level
    Returns:
        int: number of tries user has attempted so far
    """
    # Hints count as two tries
    tries += 2
    # Use for loop to loop through letters of random word
    for letter in word:
        if letter not in guessed_letters:  # For hint print first letter not guessed
            print(f"Your revealed letter is '{letter}'")
            guessed_letters.append(letter)  # Add hint letter to guessed_letters list
            break
    output(word, guessed_letters, count, tries)  # Print output of tries remaining and word
    return tries


def validate_word_input(user_guess, guessed_letters):
    """
    Validate user input to catch mistakes.

    If user input is hint - return False
    If user input is more than one letter, not a letter, or has already been guessed - return True
    If none of these occur - return False
    Parameters:
        user_guess (str): letter that user is currently guessing
        guessed_letters (str): letters already guessed by the user
    Returns:
        bool: True if user_guess is more than one letter, is not a letter, or has already been guessed.
            False if user_guess is hint or else
    """
    # Use if statements to validate user input
    if user_guess == "hint":
        return False
    # Check for one letter and only a letter
    if len(user_guess) != 1 or not user_guess.isalpha():
        print("Please enter 1 valid letter or the word 'hint'.")
        return True
    # Check that user hasn't guessed letter yet
    if user_guess in guessed_letters:
        print(f"You have already guessed this letter. Please enter another letter besides for those that have "
              f"already been guessed: {guessed_letters}")
        return True
    return False


def game_win(word, guessed_letters):
    """
    Print game ending if game is won.

    Use a for loop to check if all letters in random word are in guessed letters list.
    If game is won print game output.
    Parameters:
        word (str): random word user is trying to figure out
        guessed_letters (str): letters already guessed by the user
    Returns:
        Bool: True if game is won, False if game not won.
    """
    # Use for loop to go through letters in random word and list of guessed_letters
    if all(letter in guessed_letters for letter in word):
        print(f"You Win! You guessed all the letters in the word '{word}'.")
        return True
    return False


def game_response(user_guess, tries, word, count, guessed_letters):
    """
    Add 1 to tries for each wrong guess by user and print word output.

    Add 1 to tries for each wrong guess by user.
    Call output function to print word output and remaining tries.
    Parameters:
        user_guess (str): letter that user is currently guessing
        tries (int): number of attempt of user so far
        word (str): random word user is trying to figure out
        count (int): attempts allowed based on level
        guessed_letters (str): letters already guessed by the user
    Returns:
        int: number of tries user has attempted so far
    """
    # Add try for wrong response
    if user_guess not in word:
        tries += 1
    output(word, guessed_letters, count, tries)  # Print game output
    return tries


def play_again():
    """
    Prompt user asking if they would like to play again.

    Use a while True loop to ask the user if they would like to play again.
    If input is not in y or n - print error and reprompt.
    Returns:
         bool: True if user wants to play again, False if user doesn't want to play again
    """
    # Use while loop forever until user enters correct input
    while True:
        again = input(f"Would you like to play again? (y/n) ").strip().lower()
        if again not in ("y", "n"):  # Validate input
            print("Please enter a valid response in y/n.")
            continue
        break
    if again == "y":
        return True
    else:
        return False


def guess_input(count, tries, word, guessed_letters):
    """
    Use while loop while True and prompt user for user_input.
    If user_input is hint validate there are remaining tries.
    If game won, print results.
    Call validate_word_input function to validate input.
    Parameters:
        count (int): attempts allowed based on level
        tries (int): number of attempt of user so far
        word (str): random word user is trying to figure out
        guessed_letters (str): letters already guessed by the user
    Returns:
         tuple: number of tries user has attempted so far, letter of user_guess
    """
    # Use while loop forever until user enters correct input
    while True:
        user_guess = input("Please guess a letter or enter 'hint' (costs two tries): ").strip().lower()
        if user_guess == "hint":
            if count - tries < 2:  # Check that there's enough attempts left for hint
                print(f"Not enough tries left for a hint. Please guess a letter.")
                continue
            tries = hint(tries, word, guessed_letters, count)  # Keep track of tries from hint
            if game_win(word, guessed_letters):  # Stop loop if user wins
                break
            continue
        if validate_word_input(user_guess, guessed_letters):  # If invalid input is entered- reprompt
            continue
        else:
            break
    return tries, user_guess


def play_game(wins, losses, word, count, tries):
    """
    Create list of guessed_letters, keep track of games, and print output.

    Create list of guessed_letters.
    Use a while loop to run while tries are less than count.
    Call guess_input and game_win, keep track of tries, wins and losses.
    Print output if game is failed.
    Parameters:
        wins (int): total wins from all games
        losses (int): total losses from all games
        word (str): random word user is trying to figure out
        count (int): attempts allowed based on level
        tries (int): number of attempt of user so far
    Returns:
        tuple: number of wins and number of losses
    """
    guessed_letters = []  # Create empty list to store user guesses
    # Use while loop to run as long as user has enough attempts
    while tries < count:
        # Call guess_input function to get user_guess
        tries, user_guess = guess_input(count, tries, word, guessed_letters, wins)
        if user_guess != "hint":
            guessed_letters.append(user_guess)
        if game_win(word, guessed_letters):
            wins += 1  # Keep track of wins for end of games
            break
        tries = game_response(user_guess, tries, word, count, guessed_letters)
    else:
        print("No more tries left. Game failed.")
        print(f"Your secret word was {word}.")
        losses += 1
    return wins, losses


def end_output(wins, losses):
    """
    Print final output of entire game - wins and losses.

    Print good game, total wins, and total losses of the entire game.
    Parameters:
        wins (int): total wins from all games
        losses (int): total losses from all games
    """
    # Print output from all games
    print(f"Good Game!")
    print(f"wins: {wins}")
    print(f"losses: {losses}")


def main():
    """
    Welcome user to Guess the Word and play entire game.

    Print welcoming lines and set total wins and losses to 0.
    Use a while True loop to loop through game -calling all functions-, continuing until user does not want to play anymore.
    Print end output of total wins and losses.
    """
    # Print welcome
    print("Welcome to Guess the Word!")
    print("You will pick a level and category, and then try to guess the word one letter at a time!")
    print()  # Extra space
    wins = 0
    losses = 0
    while True:  # Use while loop to run as long as user wants to play
        # Call all functions to play
        level = ask_level()
        category_name = ask_category()
        word = pick_random(category_name)
        count, tries = game_level(level)
        wins, losses = play_game(wins, losses, word, count, tries)
        if not play_again():  # Stop loop when user doesn't want to play again
            break
    end_output(wins, losses)  # Print final output


if __name__ == "__main__":
    main()
