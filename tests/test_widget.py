import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "string, expected",
    [
        ("twenty_digit_number_account", "Счет **1567"),
        ("sixteen_digit_number_card", "MasterCard 8965 23** **** 1567"),
        ("Visa 7546653887466538", "Visa 7546 65** **** 6538"),
        ("МИР 4367539876409", "МИР 436* **** *640 9"),
        ("MasterCard 8746539876109846538", "MasterCard 8746 5398 7*** ***6 538"),
        ("счет   87465398761098465384", "счет **5384"),
        ("", ""),
    ],
)
def test_mask_account_card(string, expected, request):
    if string in ["twenty_digit_number_account", "sixteen_digit_number_card"]:
        string = request.getfixturevalue(string)
    assert mask_account_card(string) == expected


@pytest.mark.parametrize(
    "string, type_error, expected",
    [
        (
            "MasterCard8746539876109846538",
            ValueError,
            "Ошибка! Отсутствует пробел между типом и номером карты или счета",
        ),
        ("MasterCard 874653987sds6109", TypeError, "Номер карты может содержать только цифры!"),
        ("Счет 8746dgfd761098465384", TypeError, "Номер счета может содержать только цифры!"),
    ],
)
def test_mask_account_card_mistakes(string, type_error, expected):
    with pytest.raises(type_error) as exc_info:
        mask_account_card(string)
    assert str(exc_info.value) == expected


@pytest.mark.parametrize(
    "date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("1999-12-31T23:59:59.999999", "31.12.1999"),
        ("2000-02-29T00:00:00.000000", "29.02.2000"),
        ("2024-03-11", "11.03.2024"),
        ("", ""),
        ("2025/02/11", "11.02.2025"),
        ("11 February 2025", "11.02.2025"),
        ("2026.1.1", "01.01.2026"),
    ],
)
def test_get_date(date, expected):
    assert get_date(date) == expected


@pytest.mark.parametrize(
    "date, type_error, expected",
    [
        ("2024-04-31", ValueError, "Некорректный формат даты!"),
        ("11 марта 2025", ValueError, "Некорректный формат даты!"),
        ("2024-13-11T02:26:18.671407", ValueError, "Некорректный формат даты!"),
        ("2025,12,31", ValueError, "Некорректный формат даты!"),
    ],
)
def test_get_date_mistakes(date, type_error, expected):
    with pytest.raises(ValueError) as exc_info:
        get_date(date)
    assert str(exc_info.value) == expected
