import random

# The ASCII art images for each life stage
# We order them from 0 lives (Death) up to 6 lives (Empty)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/       
'''
print(logo)

groups = ["Lemon", "Apple", "Orange", "Banana", "Grape", "Strawberry", "Blueberry", "Watermelon", "Peach", "Pear"]
choose = random.choice(groups).lower()

guesses = ""
lives = 6

# Print the starting state (Empty gallows)
print(stages[lives])
print("_ " * len(choose))

while True:
    print(f"\nLives left: {lives}")
    user = input(f"Guess a letter: ").lower()

    if len(user) != 1 or not user.isalpha():
        print("Please enter a single letter.")
        continue

    if user in guesses:
        print(f"You already guessed '{user}'. Try again.")
        continue

    guesses += user

    # Check if the guess is WRONG
    if user not in choose:
        lives -= 1
        print(f"Wrong! '{user}' is not in the word.")

        # Print the hangman art corresponding to current lives
        print(stages[lives])

        if lives == 0:
            print(f"\nGAME OVER! You died.")
            print(f"The word was: {choose}")
            break

    # Display the word with guessed letters
    missing_letters = 0
    for j in choose:
        if j in guesses:
            print(j, end=" ")
        else:
            print("_", end=" ")
            missing_letters += 1

    print()

    if missing_letters == 0:
        print(f"\nYOU WIN! The word was {choose}!")
        break