input_pass = input("Введите пароль: ")
# answer = len(input_pass)

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






# print('Длина пароля: ', len(input_pass))