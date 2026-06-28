"""Импорт функций маскировки номеров"""
from masks import get_mask_card_number, get_mask_account
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

result = mask_account_card(input("Введите номер и название карты через пробел, или счет и номер счета через пробел:  "))
print(result)