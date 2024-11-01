# def check_number_in_pass(password):
#     for symbol in password:
#         if symbol.isdigit():
#             return True
#     return False
# print(check_number_in_pass("лы12овис"))

# def is_very_long(password):
#     length = len(password)
#     if length < 12:
#         return False
#     return True
# print(is_very_long("kjgfhsgd"))

def has_letters(password):
    for symbol in password:
        if symbol.isalpha():
            return True
    return False

print(has_letters("h456"))