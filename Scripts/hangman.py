
# Importing libraries
import random
import time

print("\nWelcome to Hangman game\n")
name = input("Enter your name: ")

print("Hi " + name + "! Best of luck!")
time.sleep(2)

print("Let's play Hangman!")
time.sleep(3)

# Main Function

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    word_to_guess = ["january", "border", "cookie", "ball", "soccer", "doll", "chocolate", "image", "film", "promise", "kids", "lungs", "rhyme", "damage", "plants"]
    word = random.choice(word_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = " "
    
# Develop a loop

def play_loop():
    global play_game
    play_game = input("Do you want to play again? Y = Yes, N = No\n")
    if play_game == "Y":
        main()
    elif play_game == "N":
        print("Thank you for playing!")
        exit()
        
# Initialize Conditions

def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the Hagman Word: " +
                  display + " Enter you guess: \n")
    guess = guess.strip()
    if len (guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "12":
        print("Invalid, Try a letter\n")
        hangman()
        
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + guess + display[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")
        
    elif guess in already_guessed:
        print("Try another letter.\n")
        
    else:
        count += 1
        
        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
            
        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        
        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        
        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) +
                  " last guess remaining\n")
        
        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")

        print("Wrong guess. You are hanged!!!\n")
        print("The word was: ", already_guessed)
        
    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()
        
    elif count != limit:
        hangman()

main()

hangman()
