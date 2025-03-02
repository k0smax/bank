import json
import os
from typing import Any, Dict, List

import requests
from dotenv import load_dotenv

# Загрузка переменных из .env-файла
load_dotenv()


# Получение значения переменной API_KEY из .env-файла
API_KEY = os.getenv("API_KEY")


def get_operations_list(path_to_file: str) -> List[Dict[str, Any]]:
    """
    Возвращает список словарей с данными о финансовых транзакциях из json-файла.
    Если файл пустой, содержит не список или не найден - возвращает пустой список

      path_to_file
        путь до json-файла
    """
    try:
        with open(path_to_file, encoding="utf-8") as file:
            data = json.load(file)
        if isinstance(data, list):
            return data
        else:
            return []
    except Exception:
        return []


def get_amount_transaction(transaction: Dict[str, Any]) -> float:
    """
    Принимает транзакцию и возвращает сумму транзакции в рублях

      transaction
        транзакция
    """
    default_amount = 0.0
    try:
        # Получаем информацию о валюте и сумме транзакции
        operation_amount = transaction.get("operationAmount", {})
        currency_info = operation_amount.get("currency", {})
        currency_code = currency_info.get("code")
        amount = float(operation_amount.get("amount", 0))

        # Проверяем, является ли валюта RUB, и если не является - делаем запрос на сервер
        if currency_code == "RUB":
            return amount
        elif currency_code in ("USD", "EUR"):
            to_currency = "RUB"
            from_currency = currency_code
            url = (
                f"https://api.apilayer.com/exchangerates_data/convert?"
                f"to={to_currency}&from={from_currency}&amount={amount}"
            )
            headers = {"apikey": API_KEY}
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                amount = response.json().get("result")
                return float(amount) if amount else default_amount

        return default_amount
    except Exception as exp_info:
        print(f"Error!!! - {exp_info}")
        return default_amount


# print(get_operations_list("../data/operations.json"))
# for tr in get_operations_list("../data/operations.json"):
#     print(get_amount_transaction(tr))
