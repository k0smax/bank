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


@pytest.fixture
def list_transaction():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2023-05-15T14:22:10.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "CANCELED",
            "date": "2023-08-22T09:45:33.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "PENDING",
            "date": "2024-01-10T18:30:45.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "RUB", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2023-11-30T07:12:25.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "CNY", "code": "CNY"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "EXECUTED",
            "date": "2024-02-14T12:15:20.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
        {
            "id": 615064591,
            "state": "CANCELED",
            "date": "2023-07-05T16:50:10.419441",
            "operationAmount": {"amount": "77751.04", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Maestro 3928549031574026",
            "to": "MasterCard 9175985085447523",
        },
        {
            "id": 147815167,
            "state": "EXECUTED",
            "date": "2023-09-18T20:05:55.413030",
            "operationAmount": {"amount": "50870.71", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод с карты на счет",
            "from": "Maestro 4598300720424501",
            "to": "Счет 7699855375169288",
        },
        {
            "id": 518707726,
            "state": "PENDING",
            "date": "2024-03-01T08:40:18.941293",
            "operationAmount": {"amount": "3348.98", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 10848359769870775355",
            "to": "Счет 21969751544412966366",
        },
        {
            "id": 649467725,
            "state": "EXECUTED",
            "date": "2023-12-25T23:55:44.978265",
            "operationAmount": {"amount": "96995.73", "currency": {"name": "CNY", "code": "CNY"}},
            "description": "Перевод организации",
            "from": "Счет 27248529432547658655",
            "to": "Счет 97584898735659638967",
        },
        {
            "id": 317987878,
            "state": "EXECUTED",
            "date": "2024-04-10T11:30:12.458625",
            "operationAmount": {"amount": "55985.82", "currency": {"name": "", "code": ""}},
            "description": "Перевод с карты на счет",
            "from": "Visa Classic 8906171742833215",
            "to": "Счет 6086997013848217",
        },
    ]

@pytest.fixture
def transaction_rub():
    return {
        "operationAmount": {
            "amount": 250,
            "currency": {
                "code": "RUB"
            }
        }
    }

@pytest.fixture
def transaction_usd():
    return {
        "operationAmount": {
            "amount": 250,
            "currency": {
                "code": "USD"
            }
        }
    }
