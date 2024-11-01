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

if has_digit(input_pass) == True:
    score += 2
else:
    score += 0

if is_very_long(input_pass) == True:
    score +=2
else:
    score +=0
    
if has_letters(input_pass) == True:
    score +=2
else:
    score +=0

if has_upper_letters(input_pass) == True:
    score +=2
else:
    score +=0

print(f"Рейтинг пароля: {score}")





# print('Длина пароля: ', len(input_pass))