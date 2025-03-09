from typing import Any, Dict, Iterator, List

from src.masks import split_string_blocks


def filter_by_currency(list_dicts_operation: List[Dict[str, Any]], currency: str = "USD") -> Iterator[Dict[str, Any]]:
    """Функция принимает список словарей с транзакциями и возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    operations_currency = (
        operation
        for operation in filter(
            lambda x: x.get("currency_code") == currency,
            list_dicts_operation,
        )
    )
    for operation in operations_currency:
        yield operation


def transaction_descriptions(list_dicts_operation: List[Dict[str, Any]]) -> Iterator[str]:
    """Функция принимает список словарей с транзакциями и возвращает по очереди описание каждой операции"""
    for operation in list_dicts_operation:
        yield operation.get("description", "")


def card_number_generator(start_number: int, finish_number: int) -> Iterator[str | None]:
    """Функция поочередно генерирует номера карт в диапазоне (start_number - finish_number)
    в формате 'XXXX XXXX XXXX XXXX', где X - цифра номера карты"""
    for i in range(finish_number - start_number + 1):
        number_card = [char for char in str(start_number + i)]
        for i in range(16 - len(number_card)):
            number_card.insert(0, "0")
        number_card_str = "".join(number_card)
        yield split_string_blocks(number_card_str, 4)
        i += 1
        # number = random.randint(start_number, finish_number)
        # number_card = [char for char in str(number)]
        # for i in range(16 - len(number_card)):
        #     number_card.insert(0, '0')
        # yield split_string_blocks(''.join(number_card), 4)
