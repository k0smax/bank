from unittest.mock import Mock, mock_open, patch

import pytest

import src.utils
from src.utils import (get_amount_transaction, get_operations_list, counter_categories,
                       search_operations_by_string_search)


def test_get_operations_list_valid():
    mock_data = '[{"key": "value"}]'
    with patch("src.utils.open", mock_open(read_data=mock_data)):
        result = get_operations_list("data/operations.json")
        assert result == [{"key": "value"}]


def test_get_operations_list_empty():
    with patch("src.utils.open", mock_open(read_data="")):
        result = get_operations_list("data/operations.json")
        assert result == []


def test_get_operations_list_not_json():
    with patch("src.utils.open", mock_open(read_data="not json")):
        result = get_operations_list("data/operations.json")
        assert result == []


def test_get_amount_transaction_rub(transaction_rub):
    assert get_amount_transaction(transaction_rub) == 250.0


def test_get_amount_transaction_usd(transaction_usd):
    mock_requests_get = Mock()
    mock_requests_get.return_value.json.return_value = {"result": 500.0}
    mock_requests_get.return_value.status_code = 200
    src.utils.requests.get = mock_requests_get
    assert get_amount_transaction(transaction_usd) == 500.0


@pytest.mark.parametrize(
    "status_code, operation_amount, amount, currency, code, return_value, result", [
        (500, False, 100, False, "USD", {"result": 500.0}, 0.0),  # server_error
        (200, {None}, None, None, None, None, 0.0),  # not operationAmount
        (200, False, "invalid", False, "USD", {"result": 0.0}, 0.0),  # not amount
        (200, False, 100, False, None, None, 0.0),  # not code
        (200, False, 100, False, "GBP", None, 0.0),  # currency invalid
    ]
)
@patch("requests.get")
def test_get_amount_transaction_except(mock_requests_get, status_code, operation_amount, amount,
                                       currency, code, return_value, result):
    transaction = {
        "operationAmount": operation_amount or {
            "amount": amount,
            "currency": currency or {
                "code": code
            }
        }
    }
    mock_requests_get.return_value.status_code = status_code
    mock_requests_get.return_value.json.return_value = return_value
    assert get_amount_transaction(transaction) == result


@pytest.mark.parametrize(
    "string_search, expected", [
        ("Выплата", []),
        ("Перевод с карты на счет", [
            {
                "id": 147815167,
                "state": "EXECUTED",
                "date": "2023-09-18T20:05:55.413030",
                "amount": "50870.71",
                "currency_name": "EUR",
                "currency_code": "EUR",
                "description": "Перевод с карты на счет",
                "from": "Maestro 4598300720424501",
                "to": "Счет 7699855375169288",
            },
            {
                "id": 317987878,
                "state": "EXECUTED",
                "date": "2024-04-10T11:30:12.458625",
                "amount": "55985.82",
                "currency_name": "",
                "currency_code": "",
                "description": "Перевод с карты на счет",
                "from": "Visa Classic 8906171742833215",
                "to": "Счет 6086997013848217",
            }
        ])
    ]
)
def test_search_operations_by_string_search(list_transaction, string_search, expected):
    assert search_operations_by_string_search(list_transaction, string_search) == expected


@pytest.mark.parametrize(
    "categories, expected", [
        ([], {}),
        (["Перевод со счета на счет"], {"Перевод со счета на счет": 2}),
        (["Перевод с карты на карту", "Перевод организации"], {
            "Перевод с карты на карту": 2,
            "Перевод организации": 3
        })
    ]
)
def test_counter_categories(list_transaction, categories, expected):
    assert counter_categories(list_transaction, categories) == expected
