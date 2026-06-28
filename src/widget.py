"""Импорт функций маскировки номеров"""
from masks import get_mask_card_number, get_mask_account
from datetime import datetime

def mask_account_card(card_account_name: str) ->str:
    """функция маскиорвки номера счета либо номера карты"""
    card_name, card_number = card_account_name.split()
    if "счет" in card_name.lower():
        hidden_num = get_mask_account(card_number)
    else:
        hidden_num = get_mask_card_number(card_number)
    """Вывод маскированных данных"""
    result = f"{card_name} {hidden_num}"
    return result

def get_date(date_str: str) -> str:
        # Превращаем строку в объект datetime, игнорируя миллисекунды (после точки)
        dt_obj = datetime.strptime(date_str.split('.')[0], "%Y-%m-%dT%H:%M:%S")
        # Возвращаем дату в требуемом формате ДД.ММ.ГГГГ
        return dt_obj.strftime("%d.%m.%Y")
result = mask_account_card(input("Введите номер и название карты через пробел, или счет и номер счета через пробел:  "))
print(result)
print(get_date(input("Введите дату:  ")))