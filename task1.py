# FOCP FINAL TASK 1
import random 
import os
#creating three new lists with unique characters to generate around 500 passwords at a time. 9*9*9 = 514 possibilites
moods=['affectionate', 'angry', 'blah', 'bored', 'calm', 'chilled', 'flirty', 'happy','negative']  
color=['teal', 'orchid', 'navy', 'crimson', 'turquoise', 'salmon', 'azure', 'navy','lime']
animal=['mammoth', 'cat', 'dodo', 'glyptodon', 'tasmanian', 'eagle','shrub','pyrenean','dinosaur']
password_generator=0
def user(password_generator):
    '''Asks user to generate password'''
    password_generator=int(input("Password Generator\n==================\n\nHow many passwords are needed?: ")) 
    check_condition(password_generator)
def error_hand():
    '''Clears Shell'''
    os.system('pause')
    os.system('cls')
    user(password_generator)
def check_condition(password_generator):
    '''Checks conditions of generating password'''
    if password_generator > 0 and password_generator <= 24:
        generate_password(password_generator)
    elif password_generator <= 0 or password_generator > 24: 
        print("Please enter a value between 1 and 24") 
        error_hand()
def generate_password(password_generator): 
    '''Prints password'''
    for i in range(password_generator): 
        password=random.choice(moods)+random.choice(color)+random.choice(animal) 
        print(i+1, "-->", password)
def main():
    try:
        user(password_generator)
    except:
        print("please enter a number")
        error_hand()   

if __name__ == '__main__':
  main()