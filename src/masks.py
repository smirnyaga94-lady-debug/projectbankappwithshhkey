import textwrap


def get_mask_card_number(card_num: str) -> str:
    """Функция маскировки номера банковской карты"""

    # Проверяем длину и то, состоит ли ввод только из цифр
    if len(card_num) == 16 and card_num.isdigit():
        card_num = card_num
    else:
        return "Ошибка: введено не число или неверное количество знаков."
    formated_card_num = " ".join(textwrap.wrap(card_num, 4))
    hidden_num = f"{formated_card_num[0:7]}** **** {formated_card_num[-4:]}"
    return hidden_num


def get_mask_account(acc_num: str) -> str:
    """Функция маскировки номера банковского счета"""
    # Проверяем длину и то, состоит ли ввод только из цифр
    if len(acc_num) == 20 and acc_num.isdigit():
        acc_num = acc_num
    else:
        return "Ошибка: введено не число или неверное количество знаков."
    shown_acc_num = acc_num[-4:]
    hidden_num = f"**{shown_acc_num}"
    return hidden_num
