import logging
import math

masks_logger = logging.getLogger("masks")
masks_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/masks.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)


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
    masks_logger.info(f"Запущена функция маскировки номера карты {get_mask_card_number.__name__}")

    if len(card_number) == 0:
        return ""
    if not card_number.isdigit():
        masks_logger.error(f"Номер карты {card_number} содержит не только цифры!")

        raise TypeError("Номер карты может содержать только цифры!")
    if len(card_number) > 19 or len(card_number) < 13:
        masks_logger.error(f"Количество цифр в номере карты {card_number} не соответствует реальному значению!")

        raise ValueError("Количество цифр в номере карты не соответствует реальному значению!")
    mask_card = split_string_blocks(replace_char_stars(card_number, len(card_number) - 9, len(card_number) - 4), 4)

    masks_logger.info(f"Маскировка номера карты выполнена успешно! Результат: {mask_card}")

    return mask_card


def get_mask_account(account_number: str) -> str:
    """Функция маскирует номер счета в формате: **XXXX"""
    # Предполагается, что номер счета может содержать только 20 цифр
    masks_logger.info(f"Запущена функция маскировки номера счета {get_mask_account.__name__}")

    if not account_number.isdigit():
        masks_logger.error(f"Номер счета {account_number} содержит не только цифры!")

        raise TypeError("Номер счета может содержать только цифры!")
    if len(account_number) != 20:
        masks_logger.error(f"Количество цифр в номере счета {account_number} = {len(account_number)}! НЕ равно 20!")

        raise ValueError("Номер банковского счета должен состоять из 20 цифр!")
    mask_account = replace_char_stars(account_number[-6:], 1, 2)

    masks_logger.info(f"Маскировка номера счета выполнена успешно! Результат: {mask_account}")

    return mask_account


# get_mask_account("64788928876445в678490")
# get_mask_card_number("6578849883в766514")
# get_mask_account("6473")
# get_mask_card_number("475898738987")
