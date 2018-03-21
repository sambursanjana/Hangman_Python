#importing the random module
import random
#importing the time module
import time
#function for drawing hangman
def draw(turns) :

    if(turns==1) :
        print("+---+")
        print ("|  |")
        print ("   |")
        print ("   |")
        print ("   |")
        print ("   |")
        print("=========''', '''")
    elif(turns==2):
        print ("+---+")
        print ("|   |")
        print ("0   |")
        print ("    |")
        print ("    |")
        print ("    |")
        print("========''', '''")
    elif(turns==3):
        print("+----+")
        print ("|   |")
        print ("0   |")
        print ("|   |")
        print ("    |")
        print ("    |")
        print("========''', '''")
    elif(turns==4):
        print("  +----+")
        print (" |   |")
        print (" 0   |")
        print ("/|   |")
        print ("     |")
        print ("     |")
        print("  ========''', '''")
    elif(turns==5):
        print("  +----+")
        print (" |   |")
        print (" 0   |")
        print ("/|\  |")
        print ("     |")
        print ("     |")
        print("  ========''', '''")
    elif(turns==6):
        print("  +----+")
        print (" |   |")
        print (" 0   |")
        print ("/|\  |")
        print ("/    |")
        print ("     |")
        print("  ========''', '''")
    elif(turns==7):
        print("  +----+")
        print (" |   |")
        print (" 0   |")
        print ("/|\  |")
        print ("/ \  |")
        print ("     |")
        print("  ========''', '''")
     

print ("Time to play hangman!")

print ("")


print ("Start guessing...")
time.sleep(0.5)

#here we set the secret words
word = ["secret", "gift", "high", "tent", "apple", "bat", "english", "wooden", "xerox",]

#creates an variable with an empty value
guesses = ''

#determine the number of turns
turns = 0

# Create a while loop
r=random.choice(word)
#check if the turns are greater than or equal to zero
while turns >= 0:         

    # make a counter that starts with zero
    failed = 0             

    # for every character in secret_word    
    
    for char in r:      

    # see if the character is in the players guess
        if char in guesses:    
    
        # print then out the character
            print (char,)    

        else:
    
        # if not found, print a dash
            print ("_",)     
       
        # and increase the failed counter with one
            failed += 1    

    # if failed is equal to zero

    # print You Won
    if failed == 0:        
        print ("You won")  

    # exit the script
        break              

    print

    # ask the user go guess a character
    guess = input("guess a character:") 

    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the secret word
    if guess not in r:  
 
     # turns counter increases with 1 (now 0)
        turns += 1
        draw(turns)
 
    # print wrong
        print ("Wrong")    
 
    # how many turns are left
        print ("You have", +(7-turns), 'more guesses')
         
 
    # if the turns are equal to seven i.e max trails for a hangman
        if turns == 7:           
    
        # print "You Loose"
            print ("You Loose")
    # exit the script    
            break