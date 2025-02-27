import os.path

from src.masks import get_mask_account, get_mask_card_number

# PATH = os.getcwd()
# PATH_LOG = os.path.join(PATH, r"src\log.txt")
# print(PATH)
# print(PATH_LOG)
card_number_input = input("Введите номер карты: ")
account_number_input = input("Введите номер счета: ")

print(f"Маска номера карты: {get_mask_card_number(card_number_input)}")
print(f"Маска номера счета: {get_mask_account(account_number_input)}")

# with open(r"D:\Programming\Python\Projects\bank\tests\log.txt", "r") as file:
#     d = file.read().split('\n\n')
#     for str in d:
#         print(str)
