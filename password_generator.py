# Password Generator

# import secrets module to randomly choose characters.
# import password checker module from previous class.
# create a pool of different types of characters lower and upper may be the same, just with a method when used.
# Add an option so user can add a word to it's password. E.g. input == 'Cyber' therefore, password must have all conditions plus 'Cyber'
# Create an input variable to ask user if they want a random or a semi-random (enter a word and we will make it a password)
# the enter a word option should switch characters e.g. e for 3 and s for $ plus add more characters to it and switch upper and lower
# Make sure that random password satisfies the security requiremets (lab 6)
import secrets
import module_lab_6 as check

special_chars = ['!','@','#','$','%','^','&','*','(',')','_','-']
numbers = ['0','1','2','3','4','5','6','7','8','9']
letters = "abcdefghijklmnopqrstuvwxyz"
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
pass_length = 16 # moved away from first function so both can access this value

def create_password():
    """Function that generates a random password"""    
    def generator():
        password = ""
        character_count = 0
        while character_count <= pass_length:
            option = secrets.choice([1,2,3,4])
            if option == 1:
                random_choice = secrets.choice(special_chars)
                password = password + random_choice
                character_count += 1
            elif option == 2:
                random_choice = secrets.choice(numbers)
                password = password + random_choice
                character_count += 1
            elif option == 3:            
                random_choice = secrets.choice(alphabet)
                password = password + random_choice
                character_count += 1
            elif option == 4:            
                random_choice = secrets.choice(alphabet)
                password = password + random_choice.upper()
                character_count += 1
        return password
    password = generator()
    character_counter, digit_counter, uppercase_counter, lowercase_counter, special_counter = check.password_checker(password)
    if (character_counter >= 8 and digit_counter >= 1 and uppercase_counter >= 1 and lowercase_counter >= 1 and special_counter >= 1):
        return password
    else:
        generator()

def semi_random_password(word):
    """Takes a word and makes it a password"""
    word = word.capitalize()
    word = word.replace("a","@")
    word = word.replace("e","3")
    word = word.replace("i","1")
    word = word.replace("o","0")
    word = word.replace("u","U")
    password = word + '_'
    character_count = len(password)
    while character_count <= pass_length:
        option = secrets.choice([1,2])
        if option == 1:
            random_choice = secrets.choice(special_chars)
            password = password + random_choice
            character_count += 1
        elif option == 2:
            random_choice = secrets.choice(numbers)
            password = password + random_choice
            character_count += 1
    # Check if password fulfills the requirements. Imported password checker module.
    character_counter, digit_counter, uppercase_counter, lowercase_counter, special_counter = check.password_checker(password)
    if (character_counter >= 8 and digit_counter >= 1 and uppercase_counter >= 1 and lowercase_counter >= 1 and special_counter >= 1):
        print(password)
    else:
        print(f"Try again, the password, {password}, could not be generated.")
    
print("\nHi! What type of password would like? \n\n1. A fully random password.\n2. Semi-random with a word you enter.\n")
prompt = input("Enter the option 1 or 2: ")
if prompt == "1":
    print(create_password())
elif prompt == "2":
    word = input("\nEnter your word here: ")
    semi_random_password(word)
else:
    print(f"{prompt} is not a valid option. Enter either 1 or 2.")
    


