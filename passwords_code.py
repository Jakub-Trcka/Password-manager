import random
import pyperclip


#password length
pass_len = 26
#character list
character_list = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 
'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '?', '/']
password_characters = ''
true_or_false = False
num1 = 0
menu_input = ''
enter_master_key = ''

while True:

    type_master_key = 1

    if enter_master_key == '':
        #ask for if he want to log in or he want to create an account
        acc_name_or_create = input('\n--------Do you have an existing account?--------\nIf yes, type account name\nIf no, type letter c, and create an account\n: ')

    #if he want to create an account aks him for email and new master key
    if acc_name_or_create == 'c':

        select_account_name = input('select the account name\n: ')

        new_file_name = select_account_name + '.txt'

        #checks if the account exist of no continue, if yes raise an error
        try:
            new_account_e = open(f'passwords/{new_file_name}', 'r')
            new_account_e.close()
            type_master_key = 0
            print('This account is already taken :/')

        except FileNotFoundError:
            while type_master_key == 1:

                your_master_key = input('Type your new master key\n: ')
                your_master_key2 = input('Type a master key confirmation\n: ')
                type_master_key = 0

                #of his master key is not equal to master key confirmation, aks him for another one
                if your_master_key != your_master_key2:

                    type_master_key = 1
                    print('Your master key is not equal to your master key confirmation.\nPlease type a new master key.')
                else:
                    #create a new file. And File's name is his email. And put into the file his master key
                    new_account_create = open(f'passwords/{new_file_name}', "w")
                    new_account_create.write(your_master_key + ' 1')
                    new_account_create.write('\n')
                    new_account_create.close()
                    print('Account created\n')

    else:
        acc_name_or_create1 = acc_name_or_create + '.txt'
        try:
            #check if the account does exist
            exist_acc = open(f'passwords/{acc_name_or_create1}', 'r')
            #ask for master key
            if enter_master_key != exist_acc.readlines()[0]:
                enter_master_key = input('Enter your master key: ') + ' 1\n'
            #if he type a correct master key ask him a questions
            exist_acc.close()
            exist_acc = open(f'passwords/{acc_name_or_create1}', 'r')
            if enter_master_key == exist_acc.readlines()[0]:
                print('\n-------------menu-------------')
                print('1. Generate new password')
                print('2. Copy a specific password')
                print('3. Show me a specific password')
                print('4. Show me all my passwords')
                print('5. Log out')
                print('------------------------------\n')
                menu_input = input(': ')

                #if he want to generate a password
                if menu_input == '1':
                    for _ in range(pass_len):
                        character = random.choice(character_list)
                        password_characters = password_characters + character
                    comment = input('Type name for this password (for example \'Gmail\')\n: ')
                    exist_acc = open(f'passwords/{acc_name_or_create1}', 'a')
                    exist_acc.write(comment + ' ' + password_characters)
                    exist_acc.write('\n')
                    exist_acc.close()
                    print('Saving ' + comment + ': ' + password_characters + '\n')
                    print('\nSuccessfully copied to the clipboard\n')
                    pyperclip.copy(password_characters)
                    spam = pyperclip.paste()

                #if he want to show specific password
                if menu_input == '2':
                    #ask him for comment of the password that he want
                    specific_password = input('Type the comment of the password that you want\n: ')
                    exist_acc.close()
                    exist_acc = open(f'passwords/{acc_name_or_create1}', 'r')

                    #checks if the comment with the password exist in the database
                    #for every string in database, checks is it's equal to typed comment
                    for password_and_comment in exist_acc.readlines():
                        #it splits the comment from the password and save it to list
                        password_and_comment_splitted = password_and_comment.split()
                        #checks if the comment is equal to typed comment
                        exist_acc.close()
                        exist_acc = open(f'passwords/{acc_name_or_create1}', 'r')
                        if password_and_comment_splitted[0] == specific_password and specific_password != exist_acc.readlines()[0]:
                            #print the password
                            print('\nSuccessfully copied to the clipboard\n')
                            pyperclip.copy(password_and_comment_splitted[1])
                            spam = pyperclip.paste()
                            true_or_false = True
                    if not(true_or_false):
                        print('This password does not exist :/\n')
                        
                if menu_input == '4':
                    exist_acc.close()
                    exist_acc = open(f'passwords/{acc_name_or_create1}', 'r')
                    for line in exist_acc.readlines():
                        num1 += 1
                        if num1 > 1:
                            print('\n' + line)
                #if he want to show specific password
                if menu_input == '3':
                    #ask him for comment of the password that he want
                    specific_password = input('Type the comment of the password that you want\n: ')
                    exist_acc.close()
                    exist_acc = open(f'passwords/{acc_name_or_create1}', 'r')

                    #checks if the comment with the password exist in the database
                    #for every string in database, checks is it's equal to typed comment
                    for password_and_comment in exist_acc.readlines():
                        #it splits the comment from the password and save it to list
                        password_and_comment_splitted = password_and_comment.split()
                        #checks if the comment is equal to typed comment
                        exist_acc.close()
                        exist_acc = open(f'passwords/{acc_name_or_create1}', 'r')
                        if password_and_comment_splitted[0] == specific_password and specific_password != exist_acc.readlines()[0]:
                            #print the password
                            print('\n' + password_and_comment_splitted[1] + '\n')
                            true_or_false = True
                    if not(true_or_false):
                        print('\nThis password does not exist :/\n')
                
                #if he wants to log out
                if menu_input == '5':
                    enter_master_key = ''
                    

            else:
                print('Invalid master key\n')
            exist_acc.close()

                    
        #if the account doesn't exist say this
        except FileNotFoundError:
            print('This account doesn\'t exist :/\n')

    
       
    
