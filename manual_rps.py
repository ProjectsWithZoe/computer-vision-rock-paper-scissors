import random


def get_computer_choice():
    choices =['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    return computer_choice

def get_user_choice():
    user_choice = input('Choose between rock,paper and scissors: ')
    return user_choice

def get_winner(computer_choice,user_choice):
    if computer_choice == user_choice:
        print ("It is a tie!")
    elif computer_choice =='Rock' and user_choice=='Scissors' or computer_choice=='Paper' and user_choice=='Rock' or computer_choice=='Scissors' and user_choice=='Paper':
        print ('You lost!')
    else:
        print('You won!')
    
def play(get_computer_choice,get_user_choice,get_winner):
    get_computer_choice()
    get_user_choice()
    get_winner()