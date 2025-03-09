import json
import logging
import os
import re
from collections import Counter
from typing import Any, Dict, List

import requests
from dotenv import load_dotenv

from config import PATH_TO_PROJECT

# Загрузка переменных из .env-файла
load_dotenv()


# Получение значения переменной API_KEY из .env-файла
API_KEY = os.getenv("API_KEY")


utils_logger = logging.getLogger("utils")
utils_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(os.path.join(PATH_TO_PROJECT, "logs/utils.log"), mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)


def get_operations_list(path_to_file: str) -> List[Dict[str, Any]]:
    """
    Возвращает список словарей с данными о финансовых транзакциях из json-файла.
    Если файл пустой, содержит не список или не найден - возвращает пустой список

      path_to_file
        путь до json-файла
    """
    utils_logger.info(f"Запущена функция {get_operations_list.__name__}")
    try:
        with open(path_to_file, encoding="utf-8") as file:
            data = json.load(file)
        if isinstance(data, list):
            utils_logger.info(f"json-файл {path_to_file} успешно прочитан!")
            # Преобразовываем список словарей (так, чтобы не было вложенных словарей)
            for operation in data:
                if operation.get("operationAmount"):
                    operation_amount = operation.pop("operationAmount")
                    operation["amount"] = operation_amount.get("amount", 0)
                    operation["currency_code"] = operation_amount.get("currency", {}).get("code")
                    operation["currency_name"] = operation_amount.get("currency", {}).get("name")
            return data
        else:
            utils_logger.info(f"Содержимое json-файла {path_to_file} не является списком!")
            return []
    except Exception as exc_info:
        utils_logger.error(f"Произошла ошибка! Информация об ошибке - {exc_info}")
        return []


def get_amount_transaction(transaction: Dict[str, Any]) -> float:
    """
    Принимает транзакцию и возвращает сумму транзакции в рублях

      transaction
        транзакция
    """
    utils_logger.info(f"Запущена функция {get_amount_transaction.__name__}")

    default_amount = 0.0
    try:
        amount = float(transaction["amount"])
        # Проверяем, является ли валюта RUB, и если не является - делаем запрос на сервер
        if transaction["currency_code"] == "RUB":
            return amount
        elif transaction["currency_code"] in ("USD", "EUR"):
            to_currency = "RUB"
            from_currency = transaction["currency_code"]
            url = (
                f"https://api.apilayer.com/exchangerates_data/convert?"
                f"to={to_currency}&from={from_currency}&amount={amount}"
            )
            headers = {"apikey": API_KEY}

            utils_logger.info(f"Выполняется запрос на сервер {url}")

            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                amount = response.json().get("result")
                utils_logger.info(f"Запрос на сервер {url} успешно выполнен!")
                return float(amount) if amount else default_amount
            utils_logger.warning(f"Не удалось подключиться к серверу {url}!")
        return default_amount
    except Exception as exp_info:
        utils_logger.error(f"Error!!! - {exp_info}")
        return default_amount


def search_operations_by_string_search(transactions: list[dict], string_search: str) -> list[dict]:
    """
    Функция принимает список транзакций и строку, по которой необходимо отфильтровать транзакции
    :param transactions: список транзакций
    :param string_search: строка поиска
    :return: отфильтрованный список транзакций по строке поиска
    """
    pattern = re.compile(string_search.lower())
    return [
        transaction for transaction in transactions if re.search(pattern, transaction.get("description", "").lower())
    ]


def counter_categories(transactions: list[dict], categories: list) -> dict:
    """
    Функция подсчитывает количество категорий, переданных списком, в списке транзакций
    :param transactions: список транзакций
    :param categories: категории, по которым необходимо получить статистику
    :return: словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории
    """
    counted = Counter(
        transaction.get("description") for transaction in transactions if transaction.get("description") in categories
    )
    return dict(counted)


if __name__ == "__main__":
    u = get_operations_list(os.path.join(PATH_TO_PROJECT, "data/operations.json"))
    # print(u[0])
    # print(search_operations_by_string_search(u, "Перевод организации"))
    print(counter_categories(u, []))
    # get_amount_transaction(u[1])
    # for tr in get_operations_list("../data/operations.json"):
    #     print(get_amount_transaction(tr))
