# Security CLI Program 
# Potential Add-ons 
# 1. Add limit to how many times a user can input this into their system incorrectly (Further implementation when working with passwords and dictionaries)
# 2.Have a choice asking you to enssentially login (JSON to access login credentials) (Have attempt limit)
# 3. Add choices for what you want your credit card options to do [1. Add card and pin (using dictionary key-value pairs), encrypting these in the dictionary before passing them,
# 4. Look for options for add on 
# 5. Create a GUI which deals with the front-end 
# 6. Database in the future 
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#Import json, os, cryptography, and base64
import json
import os
from cryptography.fernet import Fernet
import base64
#Function for Luhn algorithm to validate credit card numbers.
def verify_credit_card(card_translated):
    total = 0 
    reversed_card = card_translated[::-1]
    sum_of_even_digits = 0
    sum_of_odd_digits = 0
    even_digits = reversed_card[1::2]
    odd_digits = reversed_card[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)
    for digit in even_digits:
        number = int(digit)*2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits+=number
    total = sum_of_even_digits + sum_of_odd_digits
    print(total)
    return total % 10 == 0

#Main function to run CLI Tool 
def main():
    print("Welcome To Your Credit Card Storage and Encryption System")
    while True:
        card_number = []
        print(f'Services\n \
        1.Add and encrypt card number\n \
        2.View Card  \n \
        3.Remove Credit Card Number\n \
        4.View Cards')
        choices = input('Please input the choice you want to make: ')
        if choices == '1':
            file_name = 'cards.json'
            key_file_name = 'key.json'
            if os.path.exists(file_name):
                with open(file_name) as f:
                    all_data = json.load(f)
            else:
                all_data = []
            
            if os.path.exists(key_file_name):
                with open(key_file_name) as x:
                    key_data = json.load(x)
            else:
                key_data = []

            name = input('What is your first name?: ')
            sname = input('What is your second name?: ')
    
            card_number = input('Please put in your credit card number: ')
            translated = str.maketrans({' ':'','-':''})
            card_translated = card_number.translate(translated)

            if len(card_translated) != 16:
                print(f'Your card number input length was {len(card_translated)}. Card number must be 16 digits')
                continue
            if not card_translated.isdigit():
                print('Your card must only contain digits')
                continue
         
            if verify_credit_card(card_translated):
                print('Valid! Credit Card')

                pin = input('What is your pin: ')
                if len(pin) != 4:
                    print(f'Your pin must be 4 digits')
                    continue

                key = Fernet.generate_key()
                y = Fernet(key)
                token = y.encrypt(str(card_number).encode())  
                print(f'{card_translated} becomes {token}')

                all_data.append({
                'first_name': name,
                'last_name':sname, 
                'card_number': base64.b64encode(token).decode('utf-8'),
                'card_pin':pin
            })
                key_data.append({
                    'key':base64.b64encode(key).decode('utf-8')
                })
                with open(file_name,'w') as f:
                    json.dump(all_data,f,indent=2)
                print(f"Card Saved! Total Card Entries: {len(all_data)}")
                with open(key_file_name,'w') as x:
                    json.dump(key_data,x,indent=2)
                print(f'Key Saved')
            else:
                print('Invalid!')
        elif choices == '2':
            file_name = 'cards.json'
            key_file_name = 'key.json'
            if not os.path.exists(file_name) or not os.path.exists(key_file_name):
                print('No Cards Saved Yet')
                continue
            with open(file_name) as f:
                all_data = json.load(f)
            with open(key_file_name) as x:
                key_data = json.load(x)
            if not all_data:
                print('No Cards Found')
                continue
            print('Saved Cards \n')
            for i, card in enumerate(all_data):
                encrypted = base64.b64decode(card['card_number'])
                print(f'{i+1}. {card['first_name']} {card['last_name']}')
            try:
                pick = int(input('Select card number: ')) - 1
                if pick < 0 or pick >= len(all_data):
                    print('Invalid Section')
                    continue
            except ValueError:
                print('Enter a number: ')
                continue
            pin = input('Enter your pin: ')
            if pin != all_data[pick]['card_pin']:
                print('Incorrect Pin')
                continue

            key = base64.b64decode(key_data[pick]['key'])
            token = base64.b64decode(all_data[pick]['card_number'])
            f_key = Fernet(key)
            decrypted = f_key.decrypt(token).decode('utf-8')
            print(f'Decoded Card Number: {decrypted}' )
                
        elif choices == '3':
            file_name = 'cards.json'
            key_file_name = 'key.json'

            if not os.path.exists(file_name) or not os.path.exists(key_file_name):
                print(f'There are no available cards')
                continue
            with open(file_name) as f:
                all_data = json.load(f)
            with open(key_file_name) as x:
                key_data = json.load(x)

            for i, card in enumerate(all_data):
                print(f'{i+1}. {card['first_name']} {card['last_name']}')

            try: 
                pick = int(input('Which card number do you want to remove?: ')) - 1
                if pick < 0 or pick >= len(all_data):
                    print('Ivalid Selection')
            except:
                print('Enter a number: ')
                continue
            pin = input(f'Please enter your pin for the account :')
            #{card[pick]['first_name']} {card[pick]['last_name']}
            if pin != all_data[pick]['card_pin']:
                print('Ivalid Pin')
                continue

            remove = input('Are you sure you want to remove the card(y/n): ')
            if remove.lower() == 'y':
                all_data.pop(pick)
                key_data.pop(pick)

                with open(file_name,'w') as f:
                    json.dump(all_data,f,indent=2)

                with open(key_file_name,'w') as x:
                    json.dump(key_data,x,indent=2)
                    
                print('Card Number Removed')
                print(f'Card Number Removed. The total enttries are {len(all_data)}')
                print(all_data)
                print(key_data)




            else:
                break

        elif choices == '4':
            pass
        else:
            print('Invalid Choicce')
            continue
            
main()