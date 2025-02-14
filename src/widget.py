from dateutil import parser

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card_information: str) -> str:
    """Функция, принимающая тип и номер карты или счета, и возвращает замаскированный номер"""
    account_card_list = account_card_information.split()
    if len(account_card_list) < 2:
        if len(account_card_list) == 0:
            return ""
        raise ValueError("Ошибка! Отсутствует пробел между типом и номером карты или счета")

    if "счет" in account_card_information.lower() or "счёт" in account_card_information.lower():
        return "".join(account_card_list[:-1]) + " " + get_mask_account(account_card_list[-1])
    else:
        return "".join(account_card_list[:-1]) + " " + get_mask_card_number(account_card_list[-1])
    # if "счет" in account_card_information.lower() or "счёт" in account_card_information.lower():
    #     number = account_card_information.replace("счет", "").replace("счёт", "").strip()
    #     return "Счет " + get_mask_account(number)
    # else:
    #     number = account_card_information[-16:]
    #     print(number)
    #     return "".join(account_card_information.split()[:-1]) + " " + get_mask_card_number(number)


def get_date(current_date: str) -> str:
    """Функция принимает дату в любом формате и возвращает дату в формате 'ДД.ММ.ГГГГ'"""
    if current_date == "":
        return ""
    try:
        current_date_datetime = parser.parse(current_date)
    except (ValueError, TypeError):
        raise ValueError("Некорректный формат даты!")
    else:
        return current_date_datetime.strftime("%d.%m.%Y")
