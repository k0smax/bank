from src.masks import get_mask_account, get_mask_card_number, split_string_blocks, replace_char_stars


def test_split_string_blocks(twelve_numbers_string, twelve_symbols_string):
    assert split_string_blocks(twelve_symbols_string, 4) == 'gujh rgdo yrti jhdb'
    assert split_string_blocks(twelve_symbols_string, 0) == twelve_symbols_string
    assert split_string_blocks(twelve_numbers_string, 4) == '3456 8965 2309 9876'
    assert split_string_blocks(twelve_numbers_string, -1) == twelve_numbers_string
    assert split_string_blocks('', 4) == ''
    assert split_string_blocks('   34  568965   230998   76  ', 4) == '3456 8965 2309 9876'


def test_replace_char_stars(twelve_numbers_string, twelve_symbols_string):
    assert replace_char_stars(twelve_symbols_string, 2, 4) == 'g***rgdoyrtijhdb'
    assert replace_char_stars(twelve_numbers_string, 4, 5) == '345**96523099876'
    assert replace_char_stars('', 4, 6) == ''
    assert replace_char_stars('   ' + twelve_symbols_string, 2, 4) == 'g***rgdoyrtijhdb'
    assert replace_char_stars(twelve_numbers_string + '   ', 4, 5) == '345**96523099876'
    assert replace_char_stars(twelve_numbers_string, -1, 4) == '****896523099876'
    assert replace_char_stars(twelve_numbers_string, 15, 19) == '34568965230998**'


def test_get_mask_card_number():
    pass


def test_get_mask_account():
    pass
