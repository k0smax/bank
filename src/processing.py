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
    return [operation for operation in operations if operation["state"] == state]


def sort_by_date(
    operations: List[dict[str, Union[str, int]]], reverse_flag: bool = True
) -> List[dict[str, Union[str, int]]]:
    """Функция сортирует список операций 'operations' по дате в зависимости от флага сортировки 'reverse_flag'"""
    return sorted(operations, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=reverse_flag)


# print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#                     {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
#                     {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#                     {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
