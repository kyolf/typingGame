
import time
easy_list = ["Congratulations, you have selected the easy difficulty!",
            "This should not be hard to type.",
            "This should be easy to type"]

medium_list = ["Paragraphs are the building blocks of papers.",
            "Many students define paragraphs in terms of length: a paragraph is a group of at least five sentences, a paragraph is half a page long, etc.",
            "In reality, though, the unity and coherence of ideas among sentences is what constitutes a paragraph."]

hard_list = ["According to Martin Krzywinski, a Canadian specialist in bioinformatics, these are some of the " + 
            "hardest words to type on a standard QWERTY keyboard: pizazz, piazzas, pizzas, suburban, assuming, obstinance, foramens.",
            "The difficulty of these words was determined by the physical effort used to type them.",
            "Doubled letters can be hard, especially when the letter is typed with one of the little."]

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

def start_word_game(sentence_list):
    """Start the game"""
    game_running = True
    i = 0
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
        valid_input = False

        # End Menu
        if(i == len(sentence_list)):
            end_time = time.time()
            elasped_time_min = (end_time - start_time)/60

            WPM = calculate_WPM(num_errors, len_str_list, elasped_time_min)
            print_result(len_str_list, num_errors, elasped_time_min)
            print_WPM(WPM)

            while not valid_input:
                input_lower = input('[R]eset the game    [M]enu to return menu    [E]xit the game\n').lower()
                if input_lower == 'r' or input_lower == 'reset':
                    i = 0
                    num_errors = 0
                    len_str_list = 0
                    start_time = time.time()
                    valid_input = True

                elif input_lower == 'm' or input_lower == 'menu' or input_lower == 'e' or input_lower == 'exit':
                    game_running = False
                    valid_input = True
                
                else:
                    print('\nEnter valid input shown below')

                output = input_lower

            if output == 'r' or output == 'reset':
                continue
            else:
                return output

if __name__ == "__main__":
    menu_running = True
    user_input = 'menu'
    while menu_running:
        #Menu
        if user_input == 'menu' or user_input == 'm':
            print('\nWelcome to Typer: ')
            print('Come see how fast you can type')
            print('Select ea for easy,  med for medium, or h for hard difficulty')
            user_input = input('\n[Ea]sy    [Med]ium    [H]ard    [E]xit:\n').lower()
            valid_input = False
            while not valid_input:
                if user_input == 'ea' or user_input == 'easy' or user_input == 'e' or user_input == 'exit' or user_input == 'med' or user_input == 'medium' or user_input == 'h' or user_input == 'hard':
                    valid_input = True
                else:
                    print('\nEnter valid input shown below')

        #Start Game
        elif user_input == 'ea' or user_input == 'easy':
            user_input = start_word_game(easy_list)

        elif user_input == 'med' or user_input == 'medium':
            user_input = start_word_game(medium_list)

        elif user_input == 'h' or user_input == 'hard':
            user_input = start_word_game(hard_list)
        
        #End Game
        elif user_input == 'e' or user_input == 'exit':
            menu_running = False
    
