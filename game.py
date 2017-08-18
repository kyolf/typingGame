
import time
import random
import psycopg2
import logging

logging.basicConfig(filename="typer.log", level = logging.DEBUG)
logging.debug("Connecting to PostgreSQL")
# Change this to your local database and database user and password
connection = psycopg2.connect(database="typer", user="dev", password="123")
logging.debug("Database connection established.")
cursor = connection.cursor()

def fetch_list(list_name):
    cursor.execute('SELECT * FROM ' + list_name)
    return cursor.fetchall()

easy_list = fetch_list('easy_list')
medium_list = fetch_list('medium_list')
hard_list = fetch_list('hard_list')

def select_list_by_difficulty(difficulty):
    """Returns a sentence list depending on the difficulty
    If difficulty a string other than easy or hard, a sentence list is selected from medium by default"""
    if difficulty == "easy":
        return rand_sentence_list(easy_list)
    elif difficulty == "hard":
        return rand_sentence_list(hard_list)
    else:
        return rand_sentence_list(medium_list)
  

def rand_sentence_list(sentence_list):
    """Returns a random sentence list from the difficulty list"""
    rand_index = random.randint(0, len(sentence_list) - 1)
    return sentence_list[rand_index]

def is_correct(user_input, string):
    """checks if the string typed in is correct"""
    if(user_input == string):
        return True
    else:
        return False

def calculate_num_errors(user_input, sentence):
    index = 0
    num_errors = 0
    for user_char, orig_char in zip(user_input, sentence):
        if user_char != orig_char:
            num_errors += 1
        index += 1
    for sen_index in range(index, len(sentence)):
        num_errors += 1
    return num_errors


def calculate_WPM(num_errors, typed_length, minutes):
    """Calculate the net WPM"""
    words = (typed_length/5) - num_errors
    if words > 0:
        return words/minutes
    return 0

def print_result(input_len, num_errors, minutes):
    """Prints the results"""
    if(num_errors == 1):
        print('\nYou have completed {} characters with {} error in {} minutes'.format(input_len, num_errors, minutes))
    else:
        print('\nYou have completed {} characters with {} errors in {} minutes'.format(input_len, num_errors, minutes))

def print_WPM(WPM):
    """Print a certain statement depending on your WPM"""
    print('Your WPM is {}'.format(WPM))

    if WPM > 150:
        print('Congrats you are either a GENIUS or CHEATER\n')
    elif WPM > 100:
        print('Congrats you are fast typer\n')
    elif WPM > 50:
        print('Congrats you are average typer\n')
    else:
        print('Practice more you are {} WPM from being average\n'.format( 50 - WPM ))

def outer_menu():
    print('\nWelcome to Typer: ')
    print('Come see how fast you can type')
    print('Type e for easy,  n for normal, or h for hard difficulty')
    valid_input = False
    user_input = ''
    while not valid_input:
        user_input = input('\n[E]asy    [N]ormal    [H]ard    [Q]uit:\n').lower()
        if user_input == 'e' or user_input == 'q' or user_input == 'n' or user_input == 'h':
            valid_input = True
        else:
            print('\nEnter valid input shown below')
    return user_input

def inner_menu():
    input_lower = ''
    valid_input = False
    while not valid_input:
        input_lower = input('[R]eset the game    [M]enu to return menu    [Q]uit the game\n').lower()
        if input_lower == 'r':
            valid_input = True

        elif input_lower == 'm' or input_lower == 'q':
            game_running = False
            valid_input = True
        
        else:
            print('\nEnter valid input shown below')

    return input_lower

def start_word_game(sentence_list, difficulty):
    """Start the game"""
    game_running = True
    i = 1
    output = ''
    num_errors = 0
    len_str_list = 0
    start_time = time.time()
    while game_running:
        user_input = input('\n' + sentence_list[i] + '\n\nType the sentence shown above!\n')
        len_str_list += len(user_input)

        if is_correct(user_input, sentence_list[i]):
            print('Correct\n')
        else:
            print('Incorrect\n')
            num_errors += calculate_num_errors(user_input, sentence_list[i])
        
        i += 1

        # End Menu
        if(i == len(sentence_list)):
            end_time = time.time()
            elasped_time_min = (end_time - start_time)/60

            WPM = calculate_WPM(num_errors, len_str_list, elasped_time_min)
            print_result(len_str_list, num_errors, elasped_time_min)
            print_WPM(WPM)
            output = inner_menu()

            if output == 'r':
                i = 1
                num_errors = 0
                len_str_list = 0
                start_time = time.time()
                sentence_list = select_list_by_difficulty(difficulty)
                continue
            else:
                return output

if __name__ == "__main__":
    menu_running = True
    user_input = 'm'
    while menu_running:
        #Menu
        if user_input == 'm':
            user_input = outer_menu()

        #Start Game
        elif user_input == 'e':
            user_input = start_word_game(rand_sentence_list(easy_list), "easy")

        elif user_input == 'n':
            user_input = start_word_game(rand_sentence_list(medium_list), "medium")

        elif user_input == 'h':
            user_input = start_word_game(rand_sentence_list(hard_list), "hard")
        
        #End Game
        elif user_input == 'q':
            print('\nYou have exited out of the game')
            print('Thanks for playing!! :^)')
            menu_running = False
    
