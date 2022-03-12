from random import randrange

GUESSES = 6

# Put available words in list
with open("available_words.txt", "r") as f:
    AVAILABLE_WORDS = []
    lines = f.readlines()
    for line in lines:
        AVAILABLE_WORDS.append(line.strip())

# pick a random answer
with open("answer_list.txt", "r") as f:
    AVAILABLE_ANSWERS = []
    lines = f.readlines()
    for line in lines:
        AVAILABLE_ANSWERS.append(line.strip())
    
    ANSWER = AVAILABLE_ANSWERS[randrange(0, len(AVAILABLE_ANSWERS))]
