def check_number_in_pass(password):
    for symbol in password:
        if symbol.isdigit():
            return True
    return False
input_pass = input("Введите пароль: ")
if check_number_in_pass(input_pass):
    print("Есть цифры")
else:
    print("Нет цифр")