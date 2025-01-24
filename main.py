from src.masks import get_mask_account, get_mask_card_number

card_number_input = int(input("Введите номер карты: "))
account_number_input = int(input("Введите номер счета: "))

print(f"Маска номера карты: {get_mask_card_number(card_number_input)}")
print(f"Маска номера счета: {get_mask_account(account_number_input)}")
