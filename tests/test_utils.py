import pytest

from unittest.mock import Mock, patch, mock_open

import src.utils
from src.utils import get_operations_list, get_amount_transaction


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
        (500, False, 100, False, "USD", {"result": 500.0}, 0.0), # server_error
        (200, {None}, None, None, None, None, 0.0),  # not operationAmount
        (200, False, "invalid", False, "USD", {"result": 0.0}, 0.0), # not amount
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
