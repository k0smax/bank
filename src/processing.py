from datetime import datetime
from typing import List, Union


def filter_by_state(
    operations: List[dict[str, Union[str, int]]], state: str = "EXECUTED"
) -> List[dict[str, Union[str, int]]]:
    """Функция принимает список словарей и опциональный ключ,
    а возвращает только список словарей, значение ключа 'state' которых совпадает с опциональным ключом"""
    # formated_operations = []
    # for operation in operations:
    #     if operation['state'] == state:
    #         formated_operations.append(operation)
    # return formated_operations
    return [operation for operation in operations if operation.get("state") == state]


def sort_by_date(
    operations: List[dict[str, Union[str, int]]], reverse_flag: bool = True
) -> List[dict[str, Union[str, int]]]:
    """Функция сортирует список операций 'operations' по дате в зависимости от флага сортировки 'reverse_flag'"""

    def try_get_date(operation: dict[str, Union[str, int]]) -> datetime:
        """
        Функция пытается получить дату из банковской операции.
        Если дата отсутствует или некорректна, то выбрасывает ошибку ValueError
        """
        date_str = operation.get("date")

        try:
            if date_str:
                return datetime.strptime(str(date_str), "%Y-%m-%dT%H:%M:%S.%f")
            else:
                return datetime.strptime("1000-10-10T00:00:00.000", "%Y-%m-%dT%H:%M:%S.%f")
        except ValueError:
            raise ValueError("Некорректный формат даты!")

    return sorted(operations, key=try_get_date, reverse=reverse_flag)
