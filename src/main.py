# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')
UPPER_CASE = list('ABCDHJKRSTXYZ')
LOWER_CASE = list('abcdhjkrstxyz')
NUMBERS = list('1234567890')


def generate_password():
    
    # Start coding here
    full_string = SYMBOLS + UPPER_CASE + LOWER_CASE + NUMBERS
    
    passwd = ''
    while validate(passwd) == False: 
        passwd_gen = []
        i = random.randint(8,16)
        while i > 0:
            rand_char = random.choice(full_string)
            passwd_gen.append(rand_char) 
            i-=1
            
        passwd = ''.join(passwd_gen)
            
    return passwd
    
   
def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
