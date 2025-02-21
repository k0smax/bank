import time
from functools import wraps
from typing import Any, Callable, Dict, Tuple


def log_decorator(filename: str = "") -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Декоратор с параметрами для логирования выполнения функции.
    'filename' - имя файла для записи логов. Если не указано, логи выводятся в консоль.
    """

    def wrapper(function: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(function)
        def inner(*args: Tuple[Any, ...], **kwargs: Dict[str, Any]) -> Any:
            type_error = "Not error"
            status = True
            result = False
            console_message = f"{function.__name__} ok"
            time_start_local = time.time()
            time_start = time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime())
            try:
                result = function(*args, **kwargs)
                return result
            except Exception as exp:
                exp_error = str(exp)
                type_error = f"error: {exp_error}"
                status = False
                console_message = f"{function.__name__} error: {exp_error}. Inputs: {(*args, *kwargs)}"
            finally:
                time_finish_local = time.time()
                time_finish = time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime())
                log = {
                    "time_start": time_start,
                    "time_finish": time_finish,
                    "time_lead": time_finish_local - time_start_local,
                    "name_function": function.__name__,
                    "status": status,
                    "type_error": type_error,
                    "input_data": (*args, *kwargs),
                    "result": result,
                    "console": console_message,
                }
                if not filename:
                    # for key, value in log.items():
                    #     print(f"{key} : {value}")
                    print(log["console"])
                else:
                    with open("log.txt", "a", encoding="UTF-8") as file:
                        for key, value in log.items():
                            file.writelines(f"{key} : {value}\n")
                        file.writelines("\n")
            raise Exception("Ошибка!")

        return inner

    return wrapper
# @log_decorator()
# def add(x, y):
#     return x + y
#
# add("d", 2)
# add(2, 4)
