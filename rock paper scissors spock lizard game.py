# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

# helper functions

def name_to_number(name):
   
    if(name=="rock"):
        return 0
    elif(name=="Spock"):
        return 1
    elif(name=="paper"):
        return 2
    elif(name=="lizard"):
        return 3
    elif(name=="scissors"):
        return 4

    # convert name to number using if/elif/else
    


def number_to_name(number):
   
    
    if(number==0):
        return "rock"
    elif(number==1):
        return "Spock"
    elif(number==2):
        return "paper"
    elif(number==3):
        return "lizard"
    elif(number==4):
        return "scissors"
    
    # convert number to a name using if/elif/else
    
    

def rpsls(player_choice): 
    
    
    # print a blank line to separate consecutive games
    
    print ""
    

    # print out the message for the player's choice
    
    print "Player chooses",player_choice

    # convert the player's choice to player_number using the function name_to_number()
    
    player_value = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    
    computer_value = random.randrange(0,5)

    # convert comp_number to comp_choice using the function number_to_name()
    
    computer_name = number_to_name(computer_value)
    
    # print out the message for computer's choice
    
    print "Computer chooses",computer_name

    # compute difference of comp_number and player_number modulo five

    difference = (player_value-computer_value)%5
    
    if(difference==1) or (difference==2):
        return "Player wins!"
    elif(difference==3) or (difference==4):
        return "Computer wins!"
    else:
        return "Player and computer tie!"
    
    # use if/elif/else to determine winner, print winner message

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
print rpsls("rock")
print rpsls("Spock")
print rpsls("paper")
print rpsls("lizard")
print rpsls("scissors")



