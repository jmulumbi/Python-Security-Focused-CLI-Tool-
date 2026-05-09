# Security CLI Program 
# Potential Add-ons 
# 1. Add limit to how many times a user can input this into their system incorrectly (Further implementation when working with passwords and dictionaries)
# 2.Have a choice asking you to enssentially login (JSON to access login credentials) (Have attempt limit)
# 3. Add choices for what you want your credit card options to do [1. Add card and pin (using dictionary key-value pairs), encrypting these in the dictionary before passing them,
# 4. Look for options for add on 
# 5. Create a GUI which deals with the front-end 
# 6. Database in the future 
# 
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#Import json, os, cryptography, and base64
import json
import os
from cryptography.fernet import Fernet
import base64
import bcrypt
PIN_LENGTH = 4 
CARD_LENGTH = 16 
CARDS_FILE = 'cards.json'
MAX_PIN_ATTEMPTS = 3
#Function for Luhn algorithm to validate credit card numbers.
def verify_credit_card(card_translated):
    """
    Validate credit card number using the Luhn algorithm

    Args:
        card_translated (str): 16 digit card
    
    Returns:
        bool: True if valid, False otherwise 

    Example:
         >>>> verify_credit_card("1234123412361236")
        True
    """
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
    return total % 10 == 0
#Function to hash pin
def hash_pin(pin):
    """
    Hash pin using bcrypt library

    Args:
        pin (str): 4 digit pin number
    
    Returns:
        str: hashed pin

    Example:
        >>>> hash_pin("1234")
        -> "$2b$12$1I/WYsVsEPbMBEoD2jiZ.e1J7AQQKNkKnn2gk8F30gmDMr1ezoo6e"
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pin.encode(),salt)
    return hashed.decode('utf-8')
#Function to verify hashed pin
def verify_pin(input_pin, stored_hash):
    """
    Verify input pin is identical to the hashed pin

    Args: 
        input_pin (str) : 4 digit pin number
        stored_hash (str) : 50 digit, symbol and letter long hash

    Returns:
        bool: True if Valid, False otherwise 
    
    Example:
        >>>> verify_pin('1234',"$2b$12$1I/WYsVsEPbMBEoD2jiZ.e1J7AQQKNkKnn2gk8F30gmDMr1ezoo6e")
        True
    """
    return bcrypt.checkpw(input_pin.encode(), stored_hash.encode())
#Function to load data from the json file 
def load_data(file_name):
    """
    Load data from the cards.json file

    Args:
        file_name (.json file): JSON file with credentials

    Returns:
        Loaded JSON file

    Example:
        >>>> load_data('cards.json')
          {
    "first_name": "Jeremiah Mulumbi ",
    "last_name": "2",
    "card_number": "Z0FBQUFBQnAtbThIcEtoQ2dlb3NxZDRKa01hVXQza244VmFISXJVYnlvSnZKU2tLa2RsQnBEY0tCajVkbHQ2NV9iUkUwU3NrTGV6VDdiS0dKTEtIY19UR3o2aDIzMWZja1htYUwxYjg3SlpqY2tJQThmYWtYZlU9",
    "card_pin": "$2b$12$1I/WYsVsEPbMBEoD2jiZ.e1J7AQQKNkKnn2gk8F30gmDMr1ezoo6e",
    "key": "MmhDYzFLcGpSQVFRdDctS2Mtb1hXZUhmWEZsT0I5bTRpNmxDVmtNdGlITT0="
  }
    """
    if not os.path.exists(file_name):
        print('No Cards Saved Yet')
        return None
    with open(file_name) as f:
        all_data = json.load(f)
    return all_data
def show_cards(all_data):
    for i, card in enumerate(all_data):
        print(f'{i+1}. {card['first_name']} {card['last_name']}')

#Main function to run CLI Tool 
def main():
    """
    Runs the main functionality of the CLI tool 
    """
    print("Welcome To Your Credit Card Storage and Encryption System")
    while True:
        print(f'Services\n \
        1.Add and encrypt card number\n \
        2.View Card  \n \
        3.Remove Credit Card Number\n \
        4.View Cards \n \
        5.Change Pin')
        choices = input('Please input the choice you want to make: ')
        if choices == '1':
            file_name = 'cards.json'

            if os.path.exists(file_name):
                with open(file_name) as f:
                    all_data = json.load(f)
            else:
                all_data = []
            
            name = input('What is your first name?: ')
            sname = input('What is your second name?: ')
    
            card_number = input('Please put in your credit card number: ')
            translated = str.maketrans({' ':'','-':''})
            card_translated = card_number.translate(translated)

            if len(card_translated) != CARD_LENGTH:
                print(f'❌Your card number input length was {len(card_translated)}. Card number must be 16 digits')
                continue
            if not card_translated.isdigit():
                print('❌Your card must only contain digits')
                continue
         
            if verify_credit_card(card_translated):
                print('✅Valid! Credit Card')

                pin = input('What is your pin: ')
                if len(pin) != PIN_LENGTH:
                    print(f'❌Your PIN must be exactly 4 digits')
                    continue
                if not pin.isdigit():
                    print('❌PIN must be a digit')
                    continue

                key = Fernet.generate_key()
                y = Fernet(key)
                token = y.encrypt(str(card_translated).encode()) 
 
                print(f'**** **** **** {card_translated[-4:]} has been saved')

                all_data.append({
                'first_name': name,
                'last_name':sname, 
                'card_number': base64.b64encode(token).decode('utf-8'),
                'card_pin':hash_pin(pin),
                'key':base64.b64encode(key).decode('utf-8')
            })

                with open(file_name,'w') as f:
                    json.dump(all_data,f,indent=2)
                print(f"✅Card Saved! Total Card Entries: {len(all_data)}")
                print(f'✅Key Saved')

            else:
                print('❌Invalid!')
        elif choices == '2':
            all_data = load_data('cards.json')
            if not all_data:
                print('No Cards Found')
                continue
            print('Saved Cards \n')
            show_cards(all_data)
            try:
                pick = int(input('Select card number: ')) - 1
                if pick < 0 or pick >= len(all_data):
                    print('❌Invalid Section')
                    continue
            except ValueError:
                print('Enter a number: ')
                continue
            pin = input('Enter your PIN: ')
            if not verify_pin(pin, all_data[pick]['card_pin']):
                print('Incorrect PIN')
                continue

            key = base64.b64decode(all_data[pick]['key'])
            token = base64.b64decode(all_data[pick]['card_number'])
            f_key = Fernet(key)
            decrypted = f_key.decrypt(token).decode('utf-8')
            print(f'Decoded Card Number: {decrypted}' )
                
        elif choices == '3':
            file_name = 'cards.json'
            all_data = load_data('cards.json')
            show_cards(all_data)
            try: 
                pick = int(input('Which card number do you want to remove?: ')) - 1
                if pick < 0 or pick >= len(all_data):
                    print('❌Invalid Selection')
            except:
                print('Enter a number: ')
                continue
            pin = input(f'Please enter your PIN for {all_data[pick]["first_name"]} {all_data[pick]["last_name"]}: ')
            
            if not verify_pin(pin,all_data[pick]['card_pin']):
                print('❌Invalid PIN')
                continue

            remove = input('Are you sure you want to remove the card(y/n): ')
            if remove.lower() == 'y':
                all_data.pop(pick)

                with open(file_name,'w') as f:
                    json.dump(all_data,f,indent=2)


                print('✅Card Number Removed')
                print(f'✅Card Number Removed. The total enttries are {len(all_data)}')
            else:
                print('Removal Cancelled')
                continue
        elif choices == '4':
            file_name = 'cards.json'

            if not os.path.exists(file_name):
                print('No available files')
                continue

            all_data = load_data('cards.json')

            show_cards(all_data)
        elif choices == '5':
            #ADD CHECK TO SEE IF PIN IS 4 DIGITS
            file_name = 'cards.json'
            all_data = load_data('cards.json')
            show_cards(all_data)
            pick = int(input('Choose which card you want to change the PIN of')) - 1 
            if pick < 0 or pick > len(all_data):
                print('Invalid Selection')
                continue
            pin = input(f'Please enter your current PIN for {all_data[pick]['first_name']} {all_data[pick]['last_name']}: ')
            if not verify_pin(pin,all_data[pick]['card_pin']):
                print('❌Invalid PIN')
                continue
            else: 
                new_pin = input(f'Please input your new PIN for {all_data[pick]['first_name']} {all_data[pick]['last_name']}: ')
                check_pin = input(f'Please enter the pin again to confirm change: ')
                if new_pin != check_pin:
                    print('❌PINs do not match. Try again')
                    continue
                else:
                    all_data[pick]['card_pin'] = hash_pin(check_pin)
                    with open(file_name,'w') as f:
                        json.dump(all_data,f,indent=2)
                        print('✅New PIN Saved')
        else:
            print('❌Invalid Choice')
            continue
            
if __name__ == "__main__": main()

#Valid Credit Cards:
#Card Number: 1234123412361236 - Pin: 4566
#Card Number: 4829173648291736 - Pin: 3201
#Card Number: 6738492017463824 - Pin: 3532
