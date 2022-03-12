import settings as s
import colorama

geusses = s.GUESSES
ANSWER = s.ANSWER

# Gets user geuss
def geussing():
    while True:
        geuss = input(f"\n{geusses} geusses left: ")
        if len(str(geuss)) != 5:
            print("Invalid, Must Input a 5 letter Word")
        else:
            if geuss.lower() in s.AVAILABLE_WORDS:
                return geuss.lower()
            else:
                print("Invalid, Must Input a Real Word")

# Compare geuss and answer
def compare(geuss):
    answer_clone = ANSWER
    geuss = str(geuss).lower()
    highlights = [None, None, None, None, None]
    i = 0
    for letter in geuss:
        if letter == answer_clone[i]:
            if answer_clone.count(letter) > 1:
                 answer_clone =  answer_clone[:i] + answer_clone[i+1:] # Bug: when anwer is lets say askew and you geuss trees it highlights both e's
            highlights[i] = colorama.Fore.GREEN
        elif letter in answer_clone:
            if answer_clone.count(letter) > 1:
                 answer_clone =  answer_clone[:i] + answer_clone[i+1:] # This was my attempt to fix the bug but it didnt work and im to lazy to fix it
            highlights[i] = colorama.Fore.YELLOW
        else:
            highlights[i] = colorama.Fore.RESET
        i += 1
    
    if geuss == ANSWER:
        return highlights, True
    return highlights, False

# Main Loop
for i in range(0, geusses):
    # Get geuss
    geuss = geussing()
    highlights, done = compare(geuss)
    
    # Print highligted word
    for x in range(0, len(str(geuss))):
        print(f"{highlights[x]} {str(geuss)[x]}", end=" ")
    print(colorama.Fore.RESET) 
    
    # If Correct
    if done == True:
        print("\nCORRECT\n")
        break
    else:
        if geusses == 1:
            print(f'\nYou Failed :( the answer was {ANSWER}\n')
        geusses -= 1