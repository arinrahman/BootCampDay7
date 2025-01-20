def switch_example(option):
    switch = {
        1: r"""
         -----
     |   |
         |
         |
         |
         |
    =========
        """,
        2: r"""
         -----
     |   |
     O   |
         |
         |
         |
    =========
        """,
        3: r"""
         -----
     |   |
     O   |
     |   |
         |
         |
    =========
        """,
        4: r"""
         -----
     |   |
     O   |
    /|   |
         |
         |
    =========
        """,
        5: r"""
         -----
     |   |
     O   |
    /|\  |
         |
         |
    =========
        """,
        6: r"""
         -----
     |   |
     O   |
    /|\  |
    /    |
         |
    =========
        """,
        7: r"""
         -----
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========
        """
    }
    return switch.get(option, "Invalid stage!")



# Initialize the game
word = input("Type the word you want to give to the player:\n").lower()

# Create a list to store the guessed word with underscores
l = ["_"] * len(word)
print("The word you need to guess is:\n" + " ".join(l))

word_l = list(word)  # Convert the word to a list of characters
count = 0  # Wrong guess count

# Main game loop
while count < 7:
    resp = input("Type a letter that you think is in the unknown word:\n").lower()

    if resp in word_l:
        for index, value in enumerate(word_l):
            if resp == value:
                l[index] = resp  # Replace the underscore with the correct letter
                word_l[index] = "_"  # Mark the letter as guessed in the original list
        print("Good guess!\n")
        print(" ".join(l))  # Print the updated guessed word
    else:
        print("You are wrong!")
        count += 1
        print(switch_example(count))  # Show the hangman stage for the current count

    # Check if the player has won
    if "_" not in l:
        print("Congratulations! You guessed the word:", word)
        break

# Check if the player has lost
if count == 7:
    print("Game Over! The word was:", word)



