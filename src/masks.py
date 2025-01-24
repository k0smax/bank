def split_string_blocks(string: str, char_in_block: int) -> str:
    """Функция разбивает строку на блоки по 'char_in_block' символов"""
    tmp_list = list()
    for i in range(char_in_block):
        tmp_list.append(string[i * char_in_block : (i + 1) * char_in_block])
    return " ".join(tmp_list)


def replace_char_stars(string: str, start_char: int, end_char: int) -> str:
    """Функция, заменяющая символы на звездочки"""
    tmp_list = list(string)
    for i in range(end_char - start_char + 1):
        tmp_list[start_char + i] = "*"
    return "".join(tmp_list)


def get_mask_card_number(card_number: int) -> str:
    """Функция маскирует номер карты в формате: XXXX XX** **** XXXX"""
    return split_string_blocks(replace_char_stars(str(card_number), 6, 10), 4)


def get_mask_account(account_number: int) -> str:
    """Функция маскирует номер счета в формате: **XXXX"""
    return replace_char_stars(str(account_number)[-6:], 0, 1)
