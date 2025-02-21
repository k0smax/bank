# Виджет для ЛК клиента банка
## Цель проекта
*Создание виджета, который показывает несколько последних успешных банковский операций клиента*
## Инструкции по установке и использованию функций
Проект находится на стадии разработки и не имеет законченный вид. Однако вы можете склонировать себе проект и поработать с текущим функционалом.

1. Клонируйте репозиторий:
```
git clone https://github.com/k0smax/bank.git
```
2. Установите зависимости:

В этом проекте используется инструмент для управления зависимостями и сборкой пакетов в Python - `Poetry`
```
poetry install 
```

Установленные зависимости:

- flake8 (7.1.1)
- black (24.10.0)
- isort (5.13.2)
- mypy (1.14.1)
- pytest (8.3.4)
- pytest-cov (6.0.0)
- python-dateutil (>=2.9.0.post0,<3.0.0)

Для добавления зависимостей вручную с помощью poetry необходимо выполнить следующую команду для каждой зависимости

```poetry add <наименование_зависимости>```

Также в проекте используется модули `datatime`, `typing`, `dateutil`, `time`, `functools`.

Версия Python - 3.13
## Примеры работы функций
1. Функция `get_mask_card_number(card_number)` принимает на вход номер карты и маскирует её в формате `XXXX XX** **** XXXX`
    
    Пример работы функции:

   `get_mask_card_number(5647876534562156) -> '5647 87** ***6 2156'`
2. Функция `get_mask_account(account_number)` принимает на вход номер счета и маскирует её в формате `**XXXX`

   Пример работы функции:

   `get_mask_account(8765378516522536) -> '**2536'`
3. Функция `filter_by_state(operations, state="EXECUTED")` принимает на вход список словарей и опциональный ключ,
    а возвращает только список словарей, значение ключа `state` которых совпадает с опциональным ключом

   Пример работы функции:

    ```
   operations_example = [
   {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
   {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
   {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
   {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
   ]
   
    filter_by_state(operations_example) -> [
   {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
   {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
   ]
    ```
4. Функция `sort_by_date(operations, reverse_flag=True)` сортирует список банковских операций `operations` по дате 
в зависимости от флага сортировки `reverse_flag`

   Пример работы функции:

    ```
   operations_example = [
   {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
   {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, 
   {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
   {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
   ]
   
    sort_by_date(operations_example) -> [
   {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, 
   {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, 
   {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, 
   {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
   ]
    ```
5. Функция `mask_account_card(account_card_information)` возвращает замаскированный номер карты или счета.

   Пример работы функции:

    ```
   account_card_informaion = "Visa 7546653887466538"
   mask_account_card(account_card_information) -> "Visa 7546 65** **** 6538"
   
   account_card_informaion = "Счет 34568965230998761567"
   mask_account_card(account_card_information) -> "Счет **1567"
    ```
6. Функция `get_date(current_date)` принимает дату в любом формате и возвращает дату в формате 'ДД.ММ.ГГГГ'

   Пример работы функции:

    ```
   current_date = "2024-03-11T02:26:18.671407"
   get_date(current_date) -> "11.03.2024"
   
   current_date = "11 February 2025"
   get_date(current_date) -> "11.02.2025"
    ```
7. Функция `filter_by_currency(list_dicts_operation, currency="USD")` принимает список словарей с транзакциями и возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной.

   Пример работы функции:

    ```
   list_dicts_operation = [
   {"id" : 1, "operationAmount": {"currency" : {"code" : "USD"}}},
   {"id" : 2, "operationAmount": {"currency" : {"code" : "RUB"}}},
   {"id" : 3, "operationAmount": {"currency" : {"code" : "USD"}}}
   ]
   operations = filter_by_currency(list_dicts_operation, "USD")
   list(operations) = [
   {'id': 1, 'operationAmount': {'currency': {'code': 'USD'}}},
   {'id': 3, 'operationAmount': {'currency': {'code': 'USD'}}}
   ]
    ```
8. Функция `transaction_descriptions(list_dicts_operation)` принимает список словарей с транзакциями и возвращает по очереди описание каждой операции.

   Пример работы функции:

    ```
   list_dicts_operation = [
   {"id" : 1, "description": "Перевод организации"},
   {"id" : 2, "description": "Перевод с карты на карту"},
   {"id" : 3, "description": "Перевод со счета на карту"},
   ]
   operations = transaction_descriptions(list_dicts_operation)
   list(operations) = [
   "Перевод организации",
   "Перевод с карты на карту",
   "Перевод со счета на карту"
   ]
    ```
9. Функция `card_number_generator(start_number, finish_number)` поочередно генерирует номера карт в диапазоне (start_number - finish_number)
    в формате 'XXXX XXXX XXXX XXXX', где X - цифра номера карты.

   Пример работы функции:

    ```
   cards_number = card_number_generator(1111111111111111, 1111111111111115)
   list(cards_number) = [
                "1111 1111 1111 1111",
                "1111 1111 1111 1112",
                "1111 1111 1111 1113",
                "1111 1111 1111 1114",
                "1111 1111 1111 1115"
   ]
    ```
9. Добавлен декоратор `log_decorator(filename="")`, который выполняет логирование выполнения функции. Если параметр filename не задан, то логи выводятся в консоль.

   Примеры логирования:

   При успешном выполнении функции:

   Вывод в консоль:
    ```
   add ok
    ```
   Запись в файл:
   ```commandline
   time_start : 02/22/2025, 01:04:20
   time_finish : 02/22/2025, 01:04:20
   time_lead : 2.5033950805664062e-05
   name_function : add
   status : True
   type_error : Not error
   input_data : (2, 4)
   result : 6
   console : add ok
   ```
   При неуспешном выполнении функции:

   Вывод в консоль:
    ```
   add error: can only concatenate str (not "int") to str. Inputs: ('d', 2)
    ```
   Запись в файл:
   ```commandline
   time_start : 02/22/2025, 01:05:25
   time_finish : 02/22/2025, 01:05:25
   time_lead : 2.6702880859375e-05
   name_function : add
   status : False
   type_error : error: can only concatenate str (not "int") to str
   input_data : ('d', 2)
   result : False
   console : add error: can only concatenate str (not "int") to str. Inputs: ('d', 2)
   ```
   
## Тестирование

Чтобы запустить все тесты, выполните: `pytest`.

Чтобы сгенерировать HTML-отчет о покрытии кода, выполните:
```pytest --cov=src --cov-report=html```
Отчет будет доступен в папке htmlcov/. Откройте файл index.html в браузере, чтобы просмотреть детали.

Пример тестов функции```mask_account_card(account_card_information)```:

```commandline
@pytest.mark.parametrize(
    "string, expected",
    [
        ("twenty_digit_number_account", "Счет **1567"),
        ("sixteen_digit_number_card", "MasterCard 8965 23** **** 1567"),
        ("Visa 7546653887466538", "Visa 7546 65** **** 6538"),
        ("МИР 4367539876409", "МИР 436* **** *640 9"),
        ("MasterCard 8746539876109846538", "MasterCard 8746 5398 7*** ***6 538"),
        ("счет   87465398761098465384", "счет **5384"),
        ("", ""),
    ],
)
def test_mask_account_card(string, expected, request):
    if string in ["twenty_digit_number_account", "sixteen_digit_number_card"]:
        string = request.getfixturevalue(string)
    assert mask_account_card(string) == expected


@pytest.mark.parametrize(
    "string, type_error, expected",
    [
        (
            "MasterCard8746539876109846538",
            ValueError,
            "Ошибка! Отсутствует пробел между типом и номером карты или счета",
        ),
        ("MasterCard 874653987sds6109", TypeError, "Номер карты может содержать только цифры!"),
        ("Счет 8746dgfd761098465384", TypeError, "Номер счета может содержать только цифры!"),
    ],
)
def test_mask_account_card_mistakes(string, type_error, expected):
    with pytest.raises(type_error) as exc_info:
        mask_account_card(string)
    assert str(exc_info.value) == expected
```