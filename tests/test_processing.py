import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "state_executed",
            [
                {"id": 1, "state": "EXECUTED", "date": "2024-10-01T12:30:45.000"},
                {"id": 3, "state": "EXECUTED", "date": "2024-11-05T18:45:30.750"},
                {"id": 5, "state": "EXECUTED", "date": "2024-09-01T08:00:00.000"},
                {"id": 8, "state": "EXECUTED"},
            ],
        ),
        (
            "state_canceled",
            [
                {"id": 4, "state": "CANCELED", "date": "2024-09-01T14:00:00.000"},
                {"id": 7, "state": "CANCELED", "date": "2025-02-11T08:00:00.000"},
            ],
        ),
        ("state_pending", [{"id": 2, "state": "PENDING", "date": "2024-09-15T09:15:22.500"}]),
        ("state_no_state", []),
    ],
)
def test_filter_by_state(test_dict_operations, state, expected, request):
    assert filter_by_state(test_dict_operations, request.getfixturevalue(state)) == expected


@pytest.mark.parametrize(
    "expected",
    [
        [
            {"id": 1, "state": "EXECUTED", "date": "2024-10-01T12:30:45.000"},
            {"id": 3, "state": "EXECUTED", "date": "2024-11-05T18:45:30.750"},
            {"id": 5, "state": "EXECUTED", "date": "2024-09-01T08:00:00.000"},
            {"id": 8, "state": "EXECUTED"},
        ]
    ],
)
def test_filter_by_default_state(test_dict_operations, expected):
    assert filter_by_state(test_dict_operations) == expected


@pytest.mark.parametrize(
    "expected, flag",
    [
        (
            [
                {"id": 7, "state": "CANCELED", "date": "2025-02-11T08:00:00.000"},
                {"id": 3, "state": "EXECUTED", "date": "2024-11-05T18:45:30.750"},
                {"id": 1, "state": "EXECUTED", "date": "2024-10-01T12:30:45.000"},
                {"id": 2, "state": "PENDING", "date": "2024-09-15T09:15:22.500"},
                {"id": 4, "state": "CANCELED", "date": "2024-09-01T14:00:00.000"},
                {"id": 5, "state": "EXECUTED", "date": "2024-09-01T08:00:00.000"},
                {"id": 6, "date": "2023-12-01T08:00:00.000"},
                {"id": 8, "state": "EXECUTED"},
            ],
            True,
        ),
        (
            [
                {"id": 8, "state": "EXECUTED"},
                {"id": 6, "date": "2023-12-01T08:00:00.000"},
                {"id": 5, "state": "EXECUTED", "date": "2024-09-01T08:00:00.000"},
                {"id": 4, "state": "CANCELED", "date": "2024-09-01T14:00:00.000"},
                {"id": 2, "state": "PENDING", "date": "2024-09-15T09:15:22.500"},
                {"id": 1, "state": "EXECUTED", "date": "2024-10-01T12:30:45.000"},
                {"id": 3, "state": "EXECUTED", "date": "2024-11-05T18:45:30.750"},
                {"id": 7, "state": "CANCELED", "date": "2025-02-11T08:00:00.000"},
            ],
            False,
        ),
    ],
)
def test_sort_by_state(test_dict_operations, flag, expected):
    assert sort_by_date(test_dict_operations, flag) == expected


@pytest.mark.parametrize(
    "dict_operation_mistakes",
    [
        [
            {"id": 1, "state": "EXECUTED", "date": "2024-10-0112:30:45.000"},
        ],
        [
            {"id": 2, "state": "EXECUTED", "date": "2025-02-29T12:30:45.000"},
        ],
        [
            {"id": 3, "state": "EXECUTED", "date": "2024,10,01"},
        ],
    ],
)
def test_sort_by_state_mistakes(dict_operation_mistakes, uncorrected_format_date):
    with pytest.raises(ValueError) as exc_info:
        sort_by_date(dict_operation_mistakes)
    assert str(exc_info.value) == uncorrected_format_date
