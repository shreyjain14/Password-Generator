import random
from strengthChecker import checkStrength

uppercase_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']
symbol_list = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?',
               '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def generate_password(length, uppercase, lowercase, symbol, number):
    if uppercase == None and lowercase == None and symbol == None and number == None:
        return "Please check at least one box.", "", ""
    if length < 9:
        length = 9
    if length > 100:
        length = 100
    score = 0
    i = 0
    strength = ''
    password = ""
    while i < 3 and score < 3:
        i += 1
        available_chars = []
        password = ""
        if uppercase == "on":
            for letter in uppercase_list:
                available_chars.append(letter)
        if lowercase == 'on':
            for letter in lowercase_list:
                available_chars.append(letter)
        if symbol == 'on':
            for symb in symbol_list:
                available_chars.append(symb)
        if number == 'on':
            for num in numbers:
                available_chars.append(num)

        for i in range(length):
            password += random.choice(available_chars)

        score, strength = checkStrength(password)
    password = password

    return "Password: ", password, strength
