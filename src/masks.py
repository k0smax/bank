import math


def split_string_blocks(string: str, char_in_block: int) -> str:
    """Функция разбивает строку на блоки по 'char_in_block' символов"""
    string = string.replace(" ", "")
    # Проверка на целочисленность char_in_block. Если меньше 1, то функция возвращает переданную строку без изменений
    if char_in_block < 1:
        return string
    tmp_list = list()
    for i in range(math.ceil(len(string) / char_in_block)):
        tmp_list.append(string[i * char_in_block : (i + 1) * char_in_block])
    return " ".join(tmp_list)


def replace_char_stars(string: str, start_char: int, end_char: int) -> str:
    """Функция, заменяющая символы на звездочки"""
    string = string.lstrip().rstrip()
    # Проверка на пустую строку (если передана пустая строка, возвращается также пустая строка)
    if len(string) == 0:
        return ""
    # Проверка на существование начального(start_char) и конченого(end_char) символа в строке
    if start_char <= 0:
        start_char = 1
    if end_char > len(string):
        end_char = len(string)

    tmp_list = list(string)
    for i in range(end_char - start_char + 1):
        tmp_list[start_char + i - 1] = "*"
    return "".join(tmp_list)


def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует номер карты в формате: XXXX XX** **** XXXX"""
    # Проверка на правильное количество цифр в номере карты
    # (в данной программе количество цифр в номере карты предполагается в диапазоне от 13 до 19 включительно)
    if len(card_number) == 0:
        return ""
    if not card_number.isdigit():
        raise TypeError("Номер карты может содержать только цифры!")
    if len(card_number) > 19 or len(card_number) < 13:
        raise ValueError("Количество цифр в номере карты не соответствует реальному значению!")
    return split_string_blocks(replace_char_stars(card_number, len(card_number) - 9, len(card_number) - 4), 4)


# print(get_mask_card_number('23456657765437458'))
def get_mask_account(account_number: str) -> str:
    """Функция маскирует номер счета в формате: **XXXX"""
    # Предполагается, что номер счета может содержать только 20 цифр
    if not account_number.isdigit():
        raise TypeError("Номер счета может содержать только цифры!")
    if len(account_number) != 20:
        raise ValueError("Номер банковского счета должен состоять из 20 цифр!")
    return replace_char_stars(account_number[-6:], 1, 2)
