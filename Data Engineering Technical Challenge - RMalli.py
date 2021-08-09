#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os, random, pandas as pd


# In[2]:


#possible solutions for github
url = 'https://github.com/RajM6789/Sensyne/blob/main/ValidSolutions.csv?raw=true'
valid_solutions = pd.read_csv(url)
valid_solutions_list = valid_solutions['ValidSolutions'].tolist()


# In[3]:


#hangman images 
def display_hangman(tries):
    stages = [  
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


# In[4]:


def hangman():
    #Set up an empty scoreboard that gets refeshed everytime the script is run
    scoreboard  = pd.DataFrame(columns = ['Name','Score', 'NumberOfTries'])
    
    while input("If you would like to play a game of hangman please type 'Y' ").upper() == "Y":
        
        #player name for scoreboard
        player_name = input("please type your name: ").upper()

        #retrieve an option from the list of solutions
        word = random.choice(valid_solutions_list).upper()

        #empty string that will be displayed
        empty_string_display = "_"* len(word)

        # number of letters in the solution not including spaces
        number_of_letters = len(set(word)) - word.count(' ')

        #correct guess counter set at 0 during the start of each game
        number_of_correct_guesses = 0

        #word_guessed set to false during the start of each game
        word_guessed = False

        #letters that the user has guessed
        guessed_letters = []

        #number of tries set to 6, this will decrease by 1 after reach incorrect guess
        tries = 6

        print(display_hangman(tries))
        print(empty_string_display)
        
        while not word_guessed and tries >0:
            guess = input("please guess a letter: ").upper()
            if len(guess) == 1 and guess.isalpha():
                #checks that the guess is not a repeat
                if guess in guessed_letters:
                    print("this letter has already been guessed ", guess)
                elif guess not in word:
                    print(guess, " is not in the word, you have lost a try")
                    #the try counter is reduced by 1 everytime an incorrect guess is attempted
                    tries -= 1
                    #appends incorrect guess to list of guesses
                    guessed_letters.append(guess)
                else:
                    print("Yes!", guess, " appears in the word! :)")
                    #increases the number of correct guesses counter by 1
                    number_of_correct_guesses = number_of_correct_guesses + 1
                    #appends correct guess to list of guesses
                    guessed_letters.append(guess)
                    #index positon of the correct guess on the empty string display
                    word_as_list = list(empty_string_display)
                    position = [i for i , letter in enumerate(word) if letter == guess]
                    for x in position:
                        word_as_list[x] = guess 
                    empty_string_display = "".join(word_as_list)
                    #if the number of correct guesses is the same as the number of letters to guess the game has ben won
                    if number_of_correct_guesses == number_of_letters:
                        word_guessed = True

            else:
                print("This guess is invalid, please type in a letter")
            print(display_hangman(tries))
            print(empty_string_display)
            print('You have ',tries,' tries remaining :)')

        if word_guessed:
            print("You win!")
            if player_name in scoreboard.Name.values:
                #if the player is already on the scoreboard, increase the score by 10
                scoreboard.loc[scoreboard['Name']== player_name, 'Score'] += 10
                scoreboard.loc[scoreboard['Name']== player_name, 'NumberOfTries'] += 1
            else:
                #for a new player, add them to the scoreboard and give them a score of 10
                scoreboard.loc[len(scoreboard)] = [player_name,10,1]
            print(scoreboard)
        else:
            #if the game is lost, the scoreboard is not updated
            print("Game lost :( the word was " + word)
            print(scoreboard)
    


# In[ ]:


print(hangman())


# In[ ]:





# In[ ]:




