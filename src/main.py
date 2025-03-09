import os

from config import PATH_TO_PROJECT
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.readers import reader_csv_file, reader_excel_file
from src.utils import get_operations_list, search_operations_by_string_search
from src.widget import get_date, mask_account_card

if __name__ == "__main__":
    print(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n" "Выберите необходимый пункт меню:",
        end="",
    )
    while True:
        print(
            "1. Получить информацию о транзакциях из JSON-файла\n"
            "2. Получить информацию о транзакциях из CSV-файла\n"
            "3. Получить информацию о транзакциях из XLSX-файла"
        )

        user_input = input("Ваш вариант: ")

        if user_input == "1":
            transactions_data = get_operations_list(os.path.join(PATH_TO_PROJECT, "data/operations.json"))
            print("Для обработки выбран JSON-файл.")
        elif user_input == "2":
            transactions_data = reader_csv_file(os.path.join(PATH_TO_PROJECT, "data/transactions.csv"))
            print("Для обработки выбран CSV-файл.")
        elif user_input == "3":
            transactions_data = reader_excel_file(os.path.join(PATH_TO_PROJECT, "data/transactions_excel.xlsx"))
            print("Для обработки выбран XLSX-файл.")
        else:
            continue
        break

    while True:
        print(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
        )

        user_input = input("Введите статус: ").lower().strip()

        if user_input == "executed":
            print(f'Операции отфильтрованы по статусу "EXECUTED"')
        elif user_input == "canceled":
            print(f'Операции отфильтрованы по статусу "CANCELED"')
        elif user_input == "pending":
            print(f'Операции отфильтрованы по статусу "PENDING"')
        else:
            print(f"Статус операции {user_input} недоступен.")
            continue
        sorted_transactions = filter_by_state(transactions_data, user_input.upper())
        break

    # print(sorted_transactions)

    while True:
        print("Отсортировать операции по дате?")

        user_input = input("Да/Нет: ").lower().strip()

        if user_input == "да":
            while True:
                print("Отсортировать по возрастанию или по убыванию?")

                user_input = input("по возрастанию/по убыванию: ").lower().strip()

                if user_input == "по возрастанию":
                    sorted_transactions = sort_by_date(sorted_transactions, False)
                elif user_input == "по убыванию":
                    sorted_transactions = sort_by_date(sorted_transactions)
                else:
                    continue
                break
        elif user_input == "нет":
            break
        else:
            continue
        break
    # print(sorted_transactions)
    while True:
        print("Выводить только рублевые транзакции?")

        user_input = input("Да/Нет: ").lower().strip()

        if user_input == "да":
            sorted_transactions_by_rub = []
            trans = filter_by_currency(sorted_transactions, "RUB")
            while True:
                try:
                    sorted_transactions_by_rub.append(next(trans))
                except StopIteration:
                    break
            print(sorted_transactions_by_rub)
            sorted_transactions = sorted_transactions_by_rub
        elif user_input == "нет":
            break
        else:
            continue
        break
    # print(sorted_transactions)
    while True:
        print("Отфильтровать список транзакций по определенному слову в описании?")

        user_input = input("Да/Нет: ").lower().strip()

        if user_input == "да":
            print("По какому слову отфильтровать операции?")

            user_input = input("Слово: ").lower().strip()

            sorted_transactions = search_operations_by_string_search(sorted_transactions, user_input)
        elif user_input == "нет":
            break
        else:
            continue
        break
    # print(sorted_transactions)
    print("Распечатываю итоговый список транзакций...")
    count_transactions = len(sorted_transactions)
    if count_transactions == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {count_transactions}")
        for transaction in sorted_transactions:
            if not transaction.get("from"):
                print(
                    f"{get_date(str(transaction.get('date')))} {transaction.get('description')}\n"
                    f"{mask_account_card(str(transaction.get('to')))}\n"
                    f"Сумма: {transaction.get('amount')} {transaction.get('currency_code')}\n"
                )
            else:
                print(
                    f"{get_date(str(transaction.get('date')))} {transaction.get('description')}\n"
                    f"{mask_account_card(str(transaction.get('from')))} -> {mask_account_card(str(transaction.get('to')))}\n"
                    f"Сумма: {transaction.get('amount')} {transaction.get('currency_code')}\n"
                )
