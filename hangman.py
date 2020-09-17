stage0 ="""
t--------
t       |
t       
t     
t       
t      
t
t----------------------
"""
stage1 ="""
t--------
t       |
t       0
t     
t       
t      
t
t----------------------
"""
stage2 ="""
t--------
t       |
t       0
t     --.
t       
t       
t
t----------------------
"""
stage3="""
t--------
t       |
t       0
t     --.--
t       
t      
t
t----------------------
"""
stage4 ="""
t--------
t       |
t       0
t     --.--
t       |
t      
t
t----------------------
"""
stage5 ="""
t--------
t       |
t       0
t     --.--
t       |
t      /  
t
t----------------------
"""
stage6 ="""
t--------
t       |
t       0
t     --.--
t       |
t      / \ 
t
t----------------------
"""

def print_stage(num):
    if num == 6:
        print(stage0)
    elif num == 5:
        print(stage1)
    elif num == 4:
        print(stage2)
    elif num == 3:
        print(stage3)
    elif num == 2:
        print(stage4)
    elif num == 1:
        print(stage5)
    elif num == 0:
        print(stage6)

import os
def file_lengthy(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    f.close()
    return i + 1
path_file = os.path.expanduser("~/Desktop/random.txt")
lines = file_lengthy(path_file)
#basically os.path.expanduser helps us access file path easily
#notetoself: windows is a lot easier to access file with but with os module from python
#mac os can be pretty easy too.
import random
ran = random.randint(1,lines)   #randomize the keyword

for i, line in enumerate(open(path_file)): #here enumerate returns 2 values: i as the iterator counter and
    if i == ran:                                  #line as the content
        key = line
key = key.lower()

original_key = key
length = len(key)-1
answer = list("_"*length)
key = list(key)
print("Hello! Welcome to Hangman. Let's begin!")
print(stage0, "Word:",*answer)
Tried = list()

state = 0
tries = 6
os.system('')
while(state!=1):
    guess = input("What's your guess (1 alphabet at a time): ").lower()
    os.system('clear')
    if guess == 'exit':
        exit()
    if len(guess) == 1:
        correct = key.count(guess)
        Tried.append(guess)
        if correct == 0:
            tries -=1
            print_stage(tries)
            print("Word:", *answer)
            if tries == 0:
                print("You failed! Try again.")
                print("The word is:",original_key)
                exit()
        elif correct > 0:
            if correct == 1:
                pos = key.index(guess)
                answer[pos] = guess
                key[pos] = 1
            else:
                while(correct>0):
                    pos = key.index(guess)
                    answer[pos] = guess
                    key[pos] = 1
                    correct -= 1
            print_stage(tries)
            print("Word:", *answer)
            if key.count(1) == length:
                print("You have won. CONGRATULATIONS")
                exit()
        print("List of tried alphabet:",*Tried)
    else:
        os.system('clear')
        print_stage(tries)
        print("Word:",*answer)
        print("List of tried alphabet:",*Tried)

        print("\nTry again")






