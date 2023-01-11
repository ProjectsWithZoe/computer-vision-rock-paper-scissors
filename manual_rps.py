import random


def get_computer_choice():
    choices =['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    return computer_choice

def get_user_choice():
    user_choice = input('Choose between rock,paper and scissors: ')
    return user_choice
    
