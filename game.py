
import time

str_list = ["Paragraphs are the building blocks of papers.",
            "Many students define paragraphs in terms of length: a paragraph is a group of at least five sentences, a paragraph is half a page long, etc.",
            "In reality, though, the unity and coherence of ideas among sentences is what constitutes a paragraph."]


def is_correct(user_input, string):
    """checks if the string typed in is correct"""
    if(user_input == string):
        return True
    else:
        return False

def calculate_WPM(num_errors, typed_length, minutes):
    """Calculate the net WPM"""
    words = (typed_length/5) - num_errors
    if words > 0:
        return words/minutes
    return 0

def start_word_game(sentence_list):
    """Start the game"""
    game_running = True
    i = 0
    output = ''
    sum = 0
    error = 0
    len_str_list = 0
    start_time = time.time()
    while game_running:
        user_input = input('\n' + sentence_list[i] + '\n\nType the sentence shown above!\n')
        index = 0
        len_str_list += len(user_input)

        if is_correct(user_input, sentence_list[i]):
            print('Correct\n')
        else:
            print('Incorrect\n')
            for user_char, orig_char in zip(user_input, sentence_list[i]):
                if user_char != orig_char:
                    error += 1
                index += 1
            for sen_index in range(index, len(sentence_list[i])):
                error += 1
            index = 0
        
        i += 1
        valid_input = False

        if(i == len(sentence_list)):
            end_time = time.time()
            elasped_time_min = (end_time - start_time)/60

            WPM = calculate_WPM(error, len_str_list, elasped_time_min)
            if(error == 1):
                print('\nYou have completed {} characters with {} error in {} minutes'.format(len_str_list, error, elasped_time_min))
            else:
                print('\nYou have completed {} characters with {} errors in {} minutes'.format(len_str_list, error, elasped_time_min))
            print('Your WPM is {}\n'.format(WPM))

            while not valid_input:
                input_lower = input('[R]eset the game    [M]enu to return menu    [E]xit the game\n').lower()
                if input_lower == 'r' or input_lower == 'reset':
                    i = 0
                    error = 0
                    valid_input = True

                elif input_lower == 'm' or input_lower == 'menu':
                    game_running = False
                    valid_input = True
                
                elif input_lower == 'e' or input_lower == 'exit':
                    valid_input = True
                    game_running = True 

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
            user_input = input('\n[S]tart to start    [E]xit:\n').lower()
            valid_input = False
            while not valid_input:
                if user_input == 's' or user_input == 'start' or user_input == 'e' or user_input == 'exit':
                    valid_input = True
                else:
                    print('\nEnter valid input shown below')

        #Start Game
        elif user_input == 's' or user_input == 'start':
            user_input = start_word_game(str_list)

        #End Game
        elif user_input == 'e' or user_input == 'exit':
            menu_running = False
    
