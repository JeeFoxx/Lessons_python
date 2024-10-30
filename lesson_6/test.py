input_pass = input("Введите пароль: ")
def check_number_in_pass(input_pass):
    number_found = False
    for letter in input_pass:
        if letter.has_human():
            number_found = True
    print(number_found)