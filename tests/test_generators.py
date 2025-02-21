import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize("currency, expected", [("USD", [0, 5, 7]), ("RUB", [2, 4])])
def test_filter_by_currency(list_transaction, currency, expected):
    operations = filter_by_currency(list_transaction, currency)
    for index in expected:
        assert next(operations) == list_transaction[index]


@pytest.mark.parametrize("currency, expected", [("THR", StopIteration), ("RUB", StopIteration)])
def test_filter_by_currency_empty(list_transaction, currency, expected):
    if currency == "THR":
        operations = filter_by_currency(list_transaction, currency)
    elif currency == "RUB":
        operations = filter_by_currency([], currency)
    with pytest.raises(expected):
        next(operations)


@pytest.mark.parametrize(
    "expected",
    [
        [
            "",
            "Перевод со счета на счет",
            "Перевод со счета на счет",
            "Перевод с карты на карту",
            "Перевод организации",
            "Перевод с карты на карту",
            "Перевод с карты на счет",
            "Перевод организации",
            "Перевод организации",
            "Перевод с карты на счет",
        ]
    ],
)
def test_transaction_descriptions(list_transaction, expected):
    transaction_descriptions_test = transaction_descriptions(list_transaction)
    assert list(transaction_descriptions_test) == expected


def test_transaction_descriptions_empty():
    transaction_descriptions_empty_test = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(transaction_descriptions_empty_test)


@pytest.mark.parametrize(
    "star_number, finish_number, expected",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (
            1111111111111111,
            1111111111111121,
            [
                "1111 1111 1111 1111",
                "1111 1111 1111 1112",
                "1111 1111 1111 1113",
                "1111 1111 1111 1114",
                "1111 1111 1111 1115",
                "1111 1111 1111 1116",
                "1111 1111 1111 1117",
                "1111 1111 1111 1118",
                "1111 1111 1111 1119",
                "1111 1111 1111 1120",
            ],
        ),
    ],
)
def test_card_number_generator(star_number, finish_number, expected):
    card_number_generator_test = card_number_generator(star_number, finish_number)
    for number_card in expected:
        assert next(card_number_generator_test) == number_card
