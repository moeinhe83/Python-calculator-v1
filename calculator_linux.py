# Calculator

# Library
import os
from pyfiglet import figlet_format
from termcolor2 import colored
 
# Clear Terminal
os.system('clear')

# Welcome
print(colored('================================================', color='blue'))
print(colored(figlet_format('Welcome'), color='cyan'))
print(colored('================================================', color='blue'))
print('                                            ')
print(colored('Start Working With The Calculator', color='magenta'))
print(colored('================================================', color='blue'))
print('                                            ')

# While
while True:

    # Value Input Option
    user_op = input('''
[+]
[-]
[*]
[/]
[out]
Enter Option ===> ''')

    # IF
    if user_op == '+':
        print('                                   ')
        number1 = float(input('Enter Number1 ===> '))
        number2 = float(input('Enter Number2 ===> '))
        print('                                ')
        print(f'Answer ===> {number1}+{number2}: {number1+number2}')

    elif user_op == '-':
        print('                                   ')
        number1 = float(input('Enter Number1 ===> '))
        number2 = float(input('Enter Number2 ===> '))
        print('                                ')
        print(f'Answer ===> {number1}-{number2}: {number1-number2}')

    elif user_op == '*':
        print('                                   ')
        number1 = float(input('Enter Number1 ===> '))
        number2 = float(input('Enter Number2 ===> '))
        print('                                ')
        print(f'Answer ===> {number1}*{number2}: {number1*number2}')

    elif user_op == '/':
        print('                                   ')
        number1 = float(input('Enter Number1 ===> '))
        number2 = float(input('Enter Number2 ===> '))
        print('                                 ')
        print(f'Answer ===> {number1}/{number2}: {number1/number2}')

    elif user_op == 'out':
        print(colored('=============================================', color='blue'))
        print(colored(figlet_format('Good Luck'), color='cyan'))
        break
            
    else:
        print('                                     ')
        print(colored('Choose Again', color='red'))

# Create By Moein Heshmati
# Finish