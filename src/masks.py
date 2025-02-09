import math


def split_string_blocks(string: str, char_in_block: int) -> str:
    """Функция разбивает строку на блоки по 'char_in_block' символов"""
    string = string.replace(' ', '')
    #Проверка на целочисленность char_in_block. Если меньше 1, то функция возвращает переданную строку без изменений
    if char_in_block < 1:
        return string
    tmp_list = list()
    for i in range(math.ceil(len(string)/char_in_block)):
        tmp_list.append(string[i * char_in_block : (i + 1) * char_in_block])
    return " ".join(tmp_list)


def replace_char_stars(string: str, start_char: int, end_char: int) -> str:
    """Функция, заменяющая символы на звездочки"""
    string = string.lstrip().rstrip()
    #Проверка на пустую строку (если передана пустая строка, возвращается также пустая строка)
    if len(string) == 0:
        return ''
    #Проверка на существование начального(start_char) и конченого(end_char) символа в строке
    if start_char <= 0:
        start_char = 1
    if end_char > len(string):
        end_char = len(string)

    tmp_list = list(string)
    for i in range(end_char - start_char + 1):
        tmp_list[start_char + i - 1] = "*"
    return "".join(tmp_list)


def get_mask_card_number(card_number: int) -> str:
    """Функция маскирует номер карты в формате: XXXX XX** **** XXXX"""
    return split_string_blocks(replace_char_stars(str(card_number), 7, 12), 4)


def get_mask_account(account_number: int) -> str:
    """Функция маскирует номер счета в формате: **XXXX"""
    return replace_char_stars(str(account_number)[-6:], 1, 2)
