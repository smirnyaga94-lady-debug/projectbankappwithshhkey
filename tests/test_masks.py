import pytest

from src.masks import get_mask_account, get_mask_card_number

"""
Тест маскировки номера карты через параметризацию, т.е. используем несколько данных для одной функции,
здесь также обработаны исключения
"""


@pytest.mark.parametrize(
    "card_num, excpected",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("6831982476737658", "6831 98** **** 7658"),
        (" ", "Ошибка: введено не число или неверное количество знаков."),
        ("123456789", "Ошибка: введено не число или неверное количество знаков."),
        ("text", "Ошибка: введено не число или неверное количество знаков."),
        ("", "Ошибка: введено не число или неверное количество знаков."),
        ("visa567891123456", "Ошибка: введено не число или неверное количество знаков."),
    ],
)
def test_mask_card_number(card_num, excpected):
    assert get_mask_card_number(card_num) == excpected


"""
отдельно проверяем маскировку номера карты при вводе пробела
"""


def test_empty_mask_card_number():
    assert get_mask_card_number(card_num=" ") == "Ошибка: введено не число или неверное количество знаков."


"""
проверка маскировки номера счета, номера счетов взяты из файла conftest
"""


def test_mask_account(account_num):
    assert get_mask_account(acc_num=account_num) == "**9589"


def test_mask_account_1(account_num_1):
    assert get_mask_account(acc_num=account_num_1) == "**5560"


def test_mask_account_2(account_num_2):
    assert get_mask_account(acc_num=account_num_2) == "**4305"


"""
проверка исключений при маскировки номера счета
"""


def test_mask_account_empty():
    assert get_mask_account("") == "Ошибка: введено не число или неверное количество знаков."


def test_mask_account_space():
    assert get_mask_account(" ") == "Ошибка: введено не число или неверное количество знаков."


def test_mask_account_not_digit():
    assert get_mask_account("hello, world") == "Ошибка: введено не число или неверное количество знаков."


def test_mask_account_wrong_len():
    assert get_mask_account("12345678") == "Ошибка: введено не число или неверное количество знаков."
