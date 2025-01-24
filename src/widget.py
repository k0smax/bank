from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(account_card_information: str) -> str:
    """ Функция, принимающая тип и номер карты или счета, и возвращает замаскированный номер """
    account_card_list = account_card_information.split()
    if 'Счет' in account_card_list:
        return ' '.join(account_card_list[:-1]) + ' ' + get_mask_account(int(account_card_list[-1]))
    else:
        return ' '.join(account_card_list[:-1]) + ' ' + get_mask_card_number(int(account_card_list[-1]))
