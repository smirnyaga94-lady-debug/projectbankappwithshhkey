from src.widget import mask_account_card, get_date
import pytest

"""
Проверка распознавания карты и счета
"""
def test_mask_account_card(card_name):
    assert mask_account_card(card_name) == "Visa Classic 6831 98** **** 7658"

def test_mask_account_card_01(acc_name):
    assert mask_account_card(acc_name) == "Счет **9589"

"""
проверка различных данных ввода
"""
@pytest.mark.parametrize("name, excpected", [("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"), ("Счет 73654108430135874305", "Счет **4305"), ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"), ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353")])
def test_mask_account_card_param(name, excpected):
    assert mask_account_card(name) == excpected

"""
Проверка исключений, пустых вводов, неправильных названий карт, неверных номеров
"""
@pytest.mark.parametrize("name, excpected", [("  ", "Неверный формат данных"), ("__", "Неверный формат данных"), ("hello world 14578", "Неверное имя карты или счета"), ("123456789", "Неверный формат данных"), ("only visa classic 1789", "Неверный формат данных"), ("Visa Classic 1789154889655676766767676767", "Visa Classic Ошибка: введено не число или неверное количество знаков.")])
def test_mask_account_card_iskluch(name, excpected):
    assert mask_account_card(name) == excpected
