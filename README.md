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

Также в проекте используется модули `datatime`, `typing` и `dateutil`.

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