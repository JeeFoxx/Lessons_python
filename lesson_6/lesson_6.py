input_pass = input("Введите пароль: ")
answer = len(input_pass)
if answer < 12:
    print("Короткий")
    for letter in input_pass:
        if letter.isdigit():
            print(letter,"- цифра")
        else:
            print(letter,"- буква")
else:
    print("Длинный")





# print('Длина пароля: ', len(input_pass))