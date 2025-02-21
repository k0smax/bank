import pytest

from src.decorators import log_decorator


def test_log_decorator():
    @log_decorator()
    def add(x, y):
        return x + y

    result = add(2, 3)
    assert result == 5

    @log_decorator()
    def add(x, y):
        return x + y

    with pytest.raises(Exception, match="Ошибка!"):
        result = add("d", 3)


def test_log_decorator_capsys(capsys):
    @log_decorator()
    def add(x, y):
        return x + y

    add(2, 4)
    assert capsys.readouterr().out == "add ok\n"

    # with open(r"D:\Programming\Python\Projects\bank\tests\log.txt", "r") as file:
    #     d = file.read().strip().split("\n\n")[-1]
    #     print(d)
    #
    # assert d = ""
