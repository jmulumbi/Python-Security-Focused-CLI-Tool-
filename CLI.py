# Potential Add-ons 
# 1. Find a better way for decryption for caesar(optional)x
# 2. Decrypt a password x
# 3. Add input/output x
# 4. Add limit to how many times a user can input this into their system incorrectly (Further implementation when working with passwords and dictionaries)
#Have a choice asking you to enssentially login (JSON to access login credentials) (Have attempt limit)
#Dictionary could be available with the different cards 
# 5. Check to see whether any non numerical character is added x
# 6. Add choices for what you want your credit card options to do [1. Add card and pin (using dictionary key-value pairs), encrypting these in the dictionary before passing them, ]
# 7. Have a dictionary or list where the card number 
import json
import os
KEY = '!7*3(%'
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


def vigenereN(card_number,key, direciton = 1):
    numbers = '0123456789!@#$%^&*(}'
    key_index = 0 
    final_number = ''

    for digit in card_number:
            key_char = key[key_index % len(key)]
            key_index+=1 
            #If find does not find character in string it returns a negative number 
            index = numbers.find(digit)
            offset = numbers.find(key_char)
            new_index = (index + offset * direciton) % len(numbers)

            final_number += numbers[new_index]
    return final_number

def encryptV(card_number,key):
    return vigenereN(card_number,key)
def decryptV(card_number,key):
    return vigenereN(card_number,key,-1)

#Have user pick which card they want to access based off of which card they added, last 4 digits 
#Add password to access cards
# Work with JSON and file opening and closing 
#Have and option to print all the cards 
#Have an option to remove the cards 
#Have an option to view the last 4 letters of 

def main():
    print("Welcome To Your Credit Card Storage and Encryption System")
    while True:
        card_number = []
        print(f'Services\n \
        1.Add and encrypt card number\n \
        2.Print Credit Card Number \n \
        3.Remove Credit Card Number')
        choices = input('Please input the number of the choice you want to make: ')
        if choices == '1':
            file_name = 'cards.json'
            if os.path.exists(file_name):
                with open(file_name) as f:
                    all_data = json.load(f)
            else:
                all_data = []
            name = input('What is your first name?: ')
            sname = input('What is your second name?: ')
            #key = '!7*3(%'
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
                print('Credit Card Validated and Added')

                pin = input('What is your pin: ')
                if len(pin) != 4:
                    print(f'Your pin must be 4 digits')
                    continue
                all_data.append({
                'first_name': name,
                'last_name':sname, 
                'card_number':encryptV(card_translated,KEY),
                'card_pin':pin
            })
                with open(file_name,'w') as f:
                    json.dump(all_data,f,indent=2)
                print(f"Saved! Total entries: {len(all_data)}")
            else:
                print('Invalid!')
            # print(f"You're card encryption number is {encryptV(card_translated,key)}")
            # print(f"You're card decryptions number is {decryptV((encryptV(card_translated,key)),key)}")
            # print(f'Thank you for using our service')
        elif choices == '2':
            pass
        else:
            pass
            

            
main()
