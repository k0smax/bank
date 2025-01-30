from typing import List, Union


def filter_by_state(operations: List[dict[str, Union[str, int]]], state : str = 'EXECUTED') -> List[dict[str, Union[str, int]]]:
    """Функция принимает список словарей и опциональный ключ,
    а возвращает только список словарей, значение ключа 'state' которых совпадает с опциональным ключом"""
    # formated_operations = []
    # for operation in operations:
    #     if operation['state'] == state:
    #         formated_operations.append(operation)
    # return formated_operations
    return [operation for operation in operations if operation['state'] == state]
