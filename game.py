
str_list = ["Paragraphs are the building blocks of papers.",
            "Many students define paragraphs in terms of length: a paragraph is a group of at least five sentences, a paragraph is half a page long, etc.",
            "In reality, though, the unity and coherence of ideas among sentences is what constitutes a paragraph."]


def is_wrong(user_input, string):
  """checks if the string typed in is correct"""
  if(user_input == string):
    print('Correct\n')
  else:
    print('Wrong\n')

if __name__ == "__main__":
  game_running = True
  i = 0
  while game_running:
    user_input = input('\n' + str_list[i] + '\n\nType the sentence shown above!\n')
    is_wrong(user_input, str_list[i])
    i += 1
    if(i == len(str_list)):
      game_running = False
