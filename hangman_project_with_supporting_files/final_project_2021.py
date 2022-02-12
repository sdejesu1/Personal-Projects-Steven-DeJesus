# author: Steven De Jesus


# program description: this program is a hangman game, where a word is chosen at random from a large set list of words
# this program will do so by combining techinques such as lists, strings, functions, loops, conditions,
# and booleans.


import time
import random

def main():
     # get user name 
     main_name = input('What is your name, player?\n\n')

     # have user download txt file that u upload with program
     print(f'''So {main_name}, to get this game started, make sure you downloaded the txt.file
I provided along with the program so that you can choose which type of words to guess from.''')
     download_dictionary_question = input('Continue? (y or n): \n\n')
     download_dictionary_question.lower()
                    
     download_loop = False
     
     # establish little loop for validation
     while download_loop == False:                    

          while download_dictionary_question != 'n' and download_dictionary_question != 'y':
               print('You must answer "y" or "n".')
               download_dictionary_question = input('Continue? (y or n):\n\n')
               download_dictionary_question.lower()
               
          
          while download_dictionary_question == 'n':
               download_dictionary_question = input('Ready? (y or n):\n\n')
               download_dictionary_question.lower()
               
     
          if download_dictionary_question == 'y':
               # have exception handling for FileNotFoundError and IOError
               try:
                    infile = open("final_hangman_words.txt", "r")
                    contents = infile.read().split()
                    hangman_list = []
                    for word in contents:
                         hangman_list.append(word)
                    infile.close()
                    
                    # establish boolean var for loop in case player wants to play again
                    continue_loop = True
                    download_loop = True
                    
               except FileNotFoundError or IOError:
                    print('''Make sure you have final_hangman_dictionary.txt downloaded to have access to the library of words!''')
                    download_dictionary_question = input('Continue? (y or n):\n\n')
                    download_dictionary_question.lower()


     first_time = True
     # while loop for continuing game
     while continue_loop == True:
          # boolean for initial start sequence
          menu_option = get_menu_option(main_name, first_time)
          
          # make first_time = false after first run
          first_time = False
          
          # use menu_option to call different fxns
          # use some exception handling
          try:
               if menu_option == 1:
                    # play the game fxn
                    start_game(hangman_list, main_name, first_time)
               elif menu_option == 2:
                    # win / loss record counter (check previous program for this)
                    continue_loop = program_exit()
                    
          except ValueError:
               print('Please choose a value which is either 1 or 2.')
               menu_option = get_menu_option(main_name, first_time)
               


# define main screen title
def display_game_screen(display_name, first_time):
     # first time loop so that u only see this once
     if first_time == True:
          print('+---+')
          time.sleep(1)
          print(' O   |')
          time.sleep(1)
          print('/|\  |')
          time.sleep(1)
          print('/ \  |')
          time.sleep(1)
          print('===')
          time.sleep(1)
          print('=' * 7)
          print('HANGMAN')
          print('=' * 7)
          time.sleep(1)
          print(f'Hello, {display_name}. Welcome to...')
          time.sleep(1)
          print('HANGMAN!')
     elif first_time == False:
          print('=' * 7)
          print('HANGMAN')
          print('=' * 7)
     
     

# define get_menu_option
def get_menu_option(menu_name, first_time):
     display_game_screen(menu_name,first_time)
     print( 'Please select from the following options: ' + '\n' )
     print( '1. Play game' )
     print( '2. Quit' + '\n' )
     # include user validation
     choice = int(input('>>>: '))
     if choice != 1:
          if choice != 2:
               print('Please choose only 1 or 2.')
               choice = int(input('\n\n>>>: '))
     # return user's choice as an integer
     return choice

# define start game fxn
def start_game(game_list, game_name, first_time):
     secret_word = random.choice(game_list)
     secret_hint = list(len(secret_word) * '_')
     chances = 8
     game_won = False
     game_lost = False
     while game_won == False and game_lost == False:
          print(secret_hint)
          guess_letter = input('Guess a letter of the word!: \n\n')
          guess_letter = guess_letter.lower()

          letters_already_guessed = ''

          if len(guess_letter) == 1:
               if guess_letter in secret_word:
                    for ch in range(0, len(secret_word)):
                         revealed_letter = secret_word[ch]
                         if guess_letter == revealed_letter:
                              if guess_letter not in letters_already_guessed:
                                   secret_hint[ch] = guess_letter
                                   letters_already_guessed += guess_letter
                              elif guess_letter in letters_already_guessed:
                                   if chances == 0:
                                        print(f'You have {chances} chances left! You died!')
                                        print(f'The word was {secret_word}')
                                        game_lost = True
                                   else:
                                        chances -= 1
                                        print(f'You have {chances} chances left! Be careful!')
                              
               elif guess_letter not in secret_word:
                    if chances == 0:
                         print(f'You have {chances} chances left! You died!')
                         print(f'The word was {secret_word}')
                         game_lost = True
                    else:
                         chances -= 1
                         print(f'You have {chances} chances left! Be careful!')
                    
          if '_' not in secret_hint:
               print("\nCongrats on winning my hangman game! I know it wasn't anything")
               print('crazy, but thank you for playing my game. It was a pleasure.\n')
               game_won = True

          if chances == 0:
               print(f'You have {chances} chances left! You died!')
               print(f'The word was {secret_word}')
               game_lost = True
     
     
          

def program_exit():
    exit_choice = input('Would you like to continue? (y/n): ')
    if exit_choice == 'y':
        return True
    elif exit_choice == 'n':
        print('Thank you for playing my Hangman game!')
        return False
    else:
         exit_choice = input('Invalid response. (y or n):\n\n')
         program_exit()



# call main
if __name__ == '__main__':
     main()
