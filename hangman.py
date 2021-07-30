
from random import choice

print('Welcome to Hangman!!!, Guess the secret word ')

org_word = choice(['father','mother','wall','dog','cat','hat','house','toy','bridge','child'])
word = set(org_word)
already_guessed = ''
correct_letters = ''
chances = 10

def hang_man():
	while not check_win():
		guess()


def guess():
	global chances
	global correct_letters
	global already_guessed

	if chances > 0:
		display_word()
		user_guess = input('\nWhat is your guess at the secret word?  ').lower()
			#check for valid input
		if len(user_guess) > 1 or not user_guess.isalpha():
			print('you entered an invalid input and you lost a guess')
			chances -= 1
			check_loss()
			#check if letter was already guessed
		elif user_guess in already_guessed:
			print('you already entered that letter and you lost a guess')
			chances -=1
			check_loss()
			#incorrect guess
		elif user_guess not in word:
			print('\nThat guess was not in the word and you lost a guess')
			chances -= 1
			already_guessed += user_guess
			check_loss()
			#correct guess
		elif len(user_guess) == 1 and user_guess in word:
			print(f'\nGreat, your guess of {user_guess} was in the word')
			correct_letters += user_guess
			word.remove(user_guess)

def display_word():
    for char in org_word:
        if char in correct_letters:
            print(char, end=' ')
        else:
            print('-', end=' ')
		
def check_win():
	if len(word) == 0:
		print(f'Congrats, you guessed the correct word {org_word}')
		return True

def check_loss():
	if chances == 0:
		print('Sorry you are out of guesses, You Lost :(')
		print(f'The word was {org_word}')
	else:
		print(f'you now have {chances} guesses left')


hang_man()


