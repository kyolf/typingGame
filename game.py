
import time
import random
import psycopg2
import logging

logging.basicConfig(filename="typer.log", level = logging.DEBUG)

logging.debug("Connecting to PostgreSQL")
# Change this to your local database and database user and password
connection = psycopg2.connect(database="typer", user="dev", password="123")
logging.debug("Database connection established.")

easy1 = ["Congratulations, you have selected the easy difficulty!",
        "This should not be hard to type.",
        "This should be easy to type"]

easy2 = ["I love to go to sleep!",
        "What about you?",
        "Sleep is awesome!!!"]

easy3 = ["The club isn't the best place to find a lover",
        "So the bar is where I go",
        "Me and my friends at the table doing shots"]

medium1 = ["Paragraphs are the building blocks of papers.",
        "Many students define paragraphs in terms of length: a paragraph is a group of at least five sentences, a paragraph is half a page long, etc.",
        "In reality, though, the unity and coherence of ideas among sentences is what constitutes a paragraph."]

medium2 = ["This quote is in the article, Programming's Dirtiest Little Secret, by Steve Yegge.",
        "\"I can't understand why professional programmers out there allow themselves to have a career without teaching themselves to type.",
        "It doesn't make any sense. It's like being, I dunno, an actor without knowing how to put your clothes on.\""]

medium3 = ["\"Tests are a good thing. The knowledge gained from a night of cramming will be all but forgotten once you hit adulthood.",
        "And that's fine. The experience you gain through competition, having sharpened your skills and broadened " +
        "your minds all under the same set of rules? That's the real treasure.\"",
        "Assassination Classroom, by Korosensei"]

hard1 = ["According to Martin Krzywinski, a Canadian specialist in bioinformatics, these are some of the " + 
        "hardest words to type on a standard QWERTY keyboard: pizazz, piazzas, pizzas, suburban, assuming, obstinance, foramens.",
        "The difficulty of these words was determined by the physical effort used to type them.",
        "Doubled letters can be hard, especially when the letter is typed with one of the little."]

hard2 = ['As you can see in the title this is "A very hard typing test text." ' +
        "Someone must have the worldwide record as at least 60 seconds to he put up on my typing test wall! " +
        "I will be checking this page every day to see if someone got this score.",
        "Most likely I will! Me! It's very fun making these types of elaborate things " +
        "because you can write whatever you want! And input commonly mispeled words!",
        "As you probably noticed by now, that mistake was on purpose. Or was it? " + 
        "Do your best! I will do my best. Believe in yourself. This thing is gonna repeat for hours. And hours."]

hard3 = ["A plasma display panel (PDP) is a type of flat panel display now commonly " +
        "used for large TV displays (typically above 37-inch or 940 mm).",
        "Many tiny cells located between two panels of glass hold an inert mixture of noble gases (neon and xenon).",
        "The gas in the cells is electrically turned into a plasma which then excites phosphors to emit light. " +
        "The display panel is only about 6 cm (2.5 inches) thick, while the total " + 
        "thickness, including electronics, is less than 10 cm (4 inches)."]

easy_list = [easy1, easy2, easy3]
medium_list = [medium1, medium2, medium3]
hard_list = [hard1, hard2, hard3]

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
    print('this is random {}'.format(rand_index))
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

def start_word_game(sentence_list, difficulty):
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
                    sentence_list = select_list_by_difficulty(difficulty)
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
            user_input = start_word_game(rand_sentence_list(easy_list), "easy")

        elif user_input == 'med' or user_input == 'medium':
            user_input = start_word_game(rand_sentence_list(medium_list), "medium")

        elif user_input == 'h' or user_input == 'hard':
            user_input = start_word_game(rand_sentence_list(hard_list), "hard")
        
        #End Game
        elif user_input == 'e' or user_input == 'exit':
            menu_running = False
    
