"""Импорт функций маскировки номеров"""
from masks import get_mask_card_number, get_mask_account
from datetime import datetime

def mask_account_card(card_account_name: str) ->str:
    """функция маскиорвки номера счета либо номера карты"""
    splited_name = card_account_name.split()
    """Если имя карты одиночное"""
    if len(splited_name) == 2:
        card_name, card_number = splited_name
        if card_number.isdigit() == False:
            return "Неверный формат данных"

        if "счет" in card_name.lower():
            hidden_num = get_mask_account(card_number)
        elif "Maestro" or "MasterCard" or "Visa Classic" or "Visa Platinum" or "Visa Gold" in card_name:
            hidden_num = get_mask_card_number(card_number)

        """Вывод маскированных данных"""
        result = f"{card_name} {hidden_num}"
        return result

    """Если имя карты двойное"""
    if len(splited_name) == 3:
        card_name, card_name_2, card_number = splited_name
        if card_number.isdigit() == False:
            return "Неверный формат данных"

        else:
            hidden_num = get_mask_card_number(card_number)
        """Вывод маскированных данных"""
        result = f"{card_name} {card_name_2} {hidden_num}"
        return result

    else:
        return "Неверный формат"


def get_date(date_str: str) -> str:
        try:
            # Превращаем строку в объект datetime, игнорируя миллисекунды (после точки)
            dt_obj = datetime.strptime(date_str.split('.')[0], "%Y-%m-%dT%H:%M:%S")
            # Возвращаем дату в требуемом формате ДД.ММ.ГГГГ
            return dt_obj.strftime("%d.%m.%Y")
        except ValueError:
            return "Неверный формат данных"
result = mask_account_card(input("Введите номер и название карты через пробел, или счет и номер счета через пробел:  "))
print(result)
print(get_date(input("Введите дату:  ")))
#изменения
print("Добрый день, уважаемый клиент")