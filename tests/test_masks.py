import pytest

from src.masks import get_mask_account, get_mask_card_number, replace_char_stars, split_string_blocks


def test_split_string_blocks(sixteen_digit_number, sixteen_digit_string):
    assert split_string_blocks(sixteen_digit_string, 4) == "gujh rgdo yrti jhdb"
    assert split_string_blocks(sixteen_digit_string, 0) == sixteen_digit_string
    assert split_string_blocks(sixteen_digit_number, 4) == "3456 8965 2309 9876"
    assert split_string_blocks(sixteen_digit_number, -1) == sixteen_digit_number
    assert split_string_blocks("", 4) == ""
    assert split_string_blocks("   34  568965   230998   76  ", 4) == "3456 8965 2309 9876"


def test_replace_char_stars(sixteen_digit_number, sixteen_digit_string):
    assert replace_char_stars(sixteen_digit_string, 2, 4) == "g***rgdoyrtijhdb"
    assert replace_char_stars(sixteen_digit_number, 4, 5) == "345**96523099876"
    assert replace_char_stars("", 4, 6) == ""
    assert replace_char_stars("   " + sixteen_digit_string, 2, 4) == "g***rgdoyrtijhdb"
    assert replace_char_stars(sixteen_digit_number + "   ", 4, 5) == "345**96523099876"
    assert replace_char_stars(sixteen_digit_number, -1, 4) == "****896523099876"
    assert replace_char_stars(sixteen_digit_number, 15, 19) == "34568965230998**"


def test_get_mask_card_number(sixteen_digit_number):
    assert get_mask_card_number(sixteen_digit_number) == "3456 89** **** 9876"
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("2345")
    assert str(exc_info.value) == "Количество цифр в номере карты не соответствует реальному значению!"
    with pytest.raises(TypeError) as exc_info:
        get_mask_card_number("sdf234")
    assert str(exc_info.value) == "Номер карты может содержать только цифры!"
    assert get_mask_card_number("") == ""


def test_get_mask_account(twenty_digit_number):
    assert get_mask_account(twenty_digit_number) == "**1567"
    with pytest.raises(TypeError) as exc_info:
        get_mask_account("34566ikuhde34587")
    assert str(exc_info.value) == "Номер счета может содержать только цифры!"
    with pytest.raises(ValueError) as exc_info:
        get_mask_account("342342309589080")
    assert str(exc_info.value) == "Номер банковского счета должен состоять из 20 цифр!"
