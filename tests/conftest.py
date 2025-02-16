import pytest


@pytest.fixture
def sixteen_digit_number():
    return "3456896523099876"


@pytest.fixture
def sixteen_digit_string():
    return "gujhrgdoyrtijhdb"


@pytest.fixture
def twenty_digit_number():
    return "34568965230998761567"


@pytest.fixture
def twenty_digit_number_account():
    return "Счет 34568965230998761567"


@pytest.fixture
def sixteen_digit_number_card():
    return "Master Card 8965230998761567"


@pytest.fixture
def test_dict_operations():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-10-01T12:30:45.000"},
        {"id": 2, "state": "PENDING", "date": "2024-09-15T09:15:22.500"},
        {"id": 3, "state": "EXECUTED", "date": "2024-11-05T18:45:30.750"},
        {"id": 4, "state": "CANCELED", "date": "2024-09-01T14:00:00.000"},
        {"id": 5, "state": "EXECUTED", "date": "2024-09-01T08:00:00.000"},
        {"id": 6, "date": "2023-12-01T08:00:00.000"},
        {"id": 7, "state": "CANCELED", "date": "2025-02-11T08:00:00.000"},
        {"id": 8, "state": "EXECUTED"},
    ]


@pytest.fixture
def state_executed():
    return "EXECUTED"


@pytest.fixture
def state_canceled():
    return "CANCELED"


@pytest.fixture
def state_pending():
    return "PENDING"


@pytest.fixture
def state_no_state():
    return "NOSTATE"


@pytest.fixture
def uncorrected_format_date():
    return "Некорректный формат даты!"
