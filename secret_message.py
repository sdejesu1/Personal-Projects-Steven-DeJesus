# author: Steven De Jesus


# this program is designed to both encrypt and decrypt messages that the user inputs
# global variables
A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
B = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
C = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
D = ['.', ',', '?', '!', '\'', '"', '-', '(', ')', '[', ']', '{', '}', '@', '#', '$', '%', '^', '&', '*', '/', '\\', '|', '<', '>', ':', ';', ' ']

# define main function
def main():
    loop = True
    while loop == True:
        # call get_menu_option
        option = get_menu_option()
    # use that value to call the function associated with the user's choice
        try:
            if option == 1:
                encode()
            elif option == 2:
                decode()
            elif option == 3:
                # return back to this menu after each task has been completed to allow the user to select another option (since fxn calls main if true it should run again)
                loop = program_exit()
    
        except ValueError:
            print('Please choose a value between 1 and 3.')

# define get_menu_option function
def get_menu_option():
    # call display_title
    display_title()
    # present user with 3 options: encrypt, decrpyt, exit
    print('Please select from the following options: ' + '\n')
    print('1. Encrypt')
    print('2. Decrypt')
    print('3. Quit' + '\n')
    # include user validation
    choice = int(input('>>>: '))
    if choice != 1:
        if choice != 2:
            if choice != 3:
                print('Please choose an option only between 1 and 3.')
                choice = int(input('>>>: '))
    # return user's choice as an integer
    return choice

# define display_title function
def display_title():
    print('--------------')
    print('Secret Message')
    print('--------------')

# define encode function
def encode():
    # prompt user with Enter a message to encrypt:
    plain_message = input('Enter a message to encrypt: ')
    encrypted_message = ""
    length_of_message = len(plain_message)
    # process each character by determining which list contains the character and then concatenate the letter of the list with a colon and the index of where that character is stored in the list
    for letter in plain_message:
        # check for list A
        if letter.islower():
            if letter in A and plain_message.index(letter) == length_of_message - 1:
                encrypted_message += "A:" + str(A.index(letter))
            elif letter in A:
                encrypted_message += "A:" + str(A.index(letter)) + "-"

        # check for list B
        elif letter.isupper():
            if letter in B and plain_message.index(letter) == length_of_message - 1:
                encrypted_message += "B:" + str(B.index(letter))
            elif letter in B:
                encrypted_message += "B:" + str(B.index(letter)) + "-"

        # check for list C
        elif letter.isdigit():
            if letter in C and plain_message.index(letter) == length_of_message - 1:
                encrypted_message += "C:" + str(C.index(letter))
            elif letter in C:
                encrypted_message += "C:" + str(C.index(letter)) + "-"

        # check for list D
        elif letter in D and plain_message.index(letter) == length_of_message - 1:
            encrypted_message += "D:" + str(D.index(letter))
        else:
            encrypted_message += "D:" + str(D.index(letter)) + "-"

    print("Encrypted message: ", encrypted_message)

# define decode function:

def decode():
    # prompt the user with Enter a message to decrypt:
    # convert encoded_text into list
    # the encoded characters are delimited with a "-", look into the string split() method to see if you can separate each encoded character into its own element stored in a list
    encrypted_message = [x for x in input("Enter a message to decrypt: \n>>> ").split("-")]
    decrypted_message = ''
    # proceed with processing each list item by identifying the original character based on the appropriate constant list (i.e. A, B, C, or D) and index representing the element (e.g. translate A:7 → h)
    for i in encrypted_message:
        element = i.split(":")
        if element[0] == 'A':
            if A[int(element[1])] in A:
                decrypted_message += A[int(element[1])]

        elif element[0] == 'B':
            if B[int(element[1])] in B:
                decrypted_message += B[int(element[1])]

        elif element[0] == 'C':
            if C[int(element[1])] in C:
                decrypted_message += C[int(element[1])]
        elif element[0] == 'D':
            if D[int(element[1])] in D:
                decrypted_message += D[int(element[1])]

    
    # Concatenate each decoded character to a string, then output the original plaintext message (the string) once all encoded elements have been processed

    # display the plaintext message as follows: Message: She can't read this :)
    print("Message: ", decrypted_message, "(They can't read this :)\n")



# define program_exit function
def program_exit():
    exit_choice = input('Are you sure you want to exit? (y/n): ')
    if exit_choice == 'n':
        main()
    elif exit_choice == 'y':
        print('Thank you for using My Secret Message!')
        return False
    else:
        print('Invalid response. (y or n)')
        program_exit()


main()
