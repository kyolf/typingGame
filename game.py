
str_list = ["Paragraphs are the building blocks of papers.",
            "Many students define paragraphs in terms of length: a paragraph is a group of at least five sentences, a paragraph is half a page long, etc.",
            "In reality, though, the unity and coherence of ideas among sentences is what constitutes a paragraph."]


def is_wrong(user_input, string):
    """checks if the string typed in is correct"""
    if(user_input == string):
        return True
    else:
        return False

# def calculate_WPM()

def start_word_game(sentence_list):
    """Start the game"""
    game_running = True
    i = 0
    output = ''
    sum = 0
    error = 0
    while game_running:
        user_input = input('\n' + sentence_list[i] + '\n\nType the sentence shown above!\n')
        
        if is_wrong(user_input, sentence_list[i]):
            print('Correct\n')
        else:
            print('Incorrect\n')
            # for char_index in range(0, len(sentence_list[i])):
            #     if()
            #     if(user_input[char_index] != sentence_list[i]):
            #         error += 1
        
        i += 1
        valid_input = False

        if(i == len(sentence_list)):
            if(error == 1):
                print('\n You have {} error'.format(error))
            else:
                print('\nYou have {} errors'.format(error))
        
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
    
