"""Импорт функций маскировки номеров"""

import datetime

from pycodestyle import continued_indentation

from src import masks


def mask_account_card(card_account_name: str) -> str:
    """функция маскиорвки номера счета либо номера карты"""
    splited_name = card_account_name.split()
    """Если имя карты одиночное"""
    if len(splited_name) == 2:
        card_name, card_number = splited_name
        if card_name not in ("Maestro", "MasterCard", "Visa Classic", "Visa Platinum", "Visa Gold", "Счет"):
            return "Неверное имя карты или счета"
        if not card_number.isdigit():
            return "Неверный формат данных"

        if "счет" in card_name.lower():
            hidden_num = masks.get_mask_account(card_number)
        elif card_name in ("Maestro", "MasterCard", "Visa Classic", "Visa Platinum", "Visa Gold"):
            hidden_num = masks.get_mask_card_number(card_number)

        """Вывод маскированных данных"""

        result = f"{card_name} {hidden_num}"
        return result

    """Если имя карты двойное"""
    if len(splited_name) == 3:
        card_name, card_name_2, card_number = splited_name
        if card_name not in ("Maestro", "MasterCard", "Visa", "Счет"):
            return "Неверное имя карты или счета"
        if not card_number.isdigit():
            return "Неверный формат данных"

        else:
            hidden_num = masks.get_mask_card_number(card_number)
        """Вывод маскированных данных"""
        result = f"{card_name} {card_name_2} {hidden_num}"
        return result

    else:
        return "Неверный формат данных"


def get_date(date_str: str) -> str:
    try:
        # Превращаем строку в объект datetime, игнорируя миллисекунды (после точки)
        dt_obj = datetime.datetime.strptime(date_str.split(".")[0], "%Y-%m-%dT%H:%M:%S")
        # Возвращаем дату в требуемом формате ДД.ММ.ГГГГ
        return dt_obj.strftime("%d.%m.%Y")
    except ValueError:
        return "Неверный формат данных"


if __name__ == "__main__":
    result = mask_account_card(input("Введите номер и название карты через пробел, или счет и номер счета через пробел: "))
    print(result)
    print(get_date(input("Введите дату:  ")))
