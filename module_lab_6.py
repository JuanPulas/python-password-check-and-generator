def password_checker(password):
    """Checks for password requirements"""
    character_counter = 0
    digit_counter = 0
    uppercase_counter = 0 
    lowercase_counter = 0
    special_counter = 0
    special_chars = ['@', '_', '!', '$', '#']
    for character in password:
        character_counter += 1
        if character.isdigit():
            digit_counter += 1
        elif character.isupper():
            uppercase_counter += 1
        elif character.islower():
            lowercase_counter += 1
        elif character in special_chars:
            special_counter += 1
    return character_counter, digit_counter, uppercase_counter, lowercase_counter, special_counter