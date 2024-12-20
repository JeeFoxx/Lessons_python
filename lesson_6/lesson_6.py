input_pass = input("Введите пароль: ")

score = 0

def has_digit(password):
    for symbol in password:
        if symbol.isdigit():
            return True
    return False

def is_very_long(password):
    length = len(password)
    if length < 12:
        return False
    return True

def has_letters(password):
    for symbol in password:
        if symbol.isalpha():
            return True
    return False

def has_upper_letters(password):
    for symbol in password:
        if symbol.isupper():
            return True
    return False

def has_lower_letters(password):
    for symbol in password:
        if symbol.islower():
            return True
    return False

def has_symbols(password):
    spec_symbol = ["%", "#"]
    for symbol in password:
        if symbol in spec_symbol:
            return True
    return False
        

def calculate_rating(password):
    score = 0   
    if has_digit(password):
        score += 2
    if is_very_long(password):
        score += 2
    if has_letters(password):
        score += 2
    if has_upper_letters(password):
        score += 2
    if has_lower_letters(password):
        score += 2
    if has_symbols(password):
        score += 2
    
    return score

print(f"Рейтинг пароля: {calculate_rating(input_pass)}")





# print('Длина пароля: ', len(input_pass))