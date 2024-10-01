import random
import hangman_data

#logo call
print(hangman_data.logo)
lives = 6
chosen_word = random.choice(hangman_data.words_library)
# print(chosen_word)
guessed_letter = []

blanks =" "
for letter in chosen_word:
    blanks = blanks+"_ "
print(blanks)

game_over = False
while not game_over:
    display = " "
    print(f"\n=====================================<< Lives left = {lives} >>=====================================")
    guess = input("Enter letter: ")
    for letter in chosen_word:
        if letter == guess:
            display = display + guess +" "
            guessed_letter.append(guess)
        elif letter in guessed_letter:
            display = display + letter+" "
        else:
            display = display + "_ "

    if guess not in guessed_letter:
        lives = lives-1
        print(f"You guessed "+ guess+", which is not present in the word")
        print(f"Remaining lives = {lives}")

    print(hangman_data.hangman_art[lives])
    print(display)


    if lives == 0:
        game_over = True
        print("\n=====================================<< YOU LOOSE >>=====================================")
        print("\nThe Correct word was = "+ chosen_word+". Better luck next time :)")


    if '_' not in display:
        game_over = True
        print("\n=====================================<< YOU WON >>=====================================")
        
input("press ENTER to exit")
print(hangman_data.creator)