input_pass = input("Введите пароль: ")
answer = len(input_pass)

def check_number_in_pass(password):
    for symbol in password:
        if symbol.isdigit():
            return True
    return False

if answer < 12:
    print("Короткий")
    if check_number_in_pass(input_pass):
        print("Есть цифры")
    else:
        print("Нет цифр")
else:
    print("Длинный")
    if check_number_in_pass(input_pass):
        print("Есть цифры")
    else:
        print("Нет цифр")





# print('Длина пароля: ', len(input_pass))