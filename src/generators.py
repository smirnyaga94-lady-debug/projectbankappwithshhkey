from typing import Any, Dict, Iterator, List


def filter_by_currency(transactions: List[Dict[str, Any]], currency_code: str) -> Iterator[Dict[str, Any]]:
    """
    Фильтрует транзакции по заданной валюте.

    :param transactions: Список словарей с транзакциями.
    :param currency_code: Строка с кодом валюты (например, 'USD').
    :return: Итератор, выдающий транзакции с нужной валютой.
    """
    for tx in transactions:
        current_code = tx.get("operationAmount", {}).get("currency", {}).get("code")
        if current_code == currency_code:
            yield tx


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """
    принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
    :param transactions: Список словарей с транзакциями.
    :return: возвращает описание каждой операции по очереди.
    """
    for tx in transactions:
        # Извлекаем значение по ключу 'description'
        yield tx.get("description", "Описание отсутствует")


def card_number_generator(start: int, end: int) -> Iterator[str]:
    for num in range(start, end + 1):
        # Форматируем число в строку из 16 цифр с ведущими нулями
        card_str = f"{num:016d}"

        # Разделяем строку на 4 блока по 4 цифры через пробел
        yield f"{card_str[0:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:16]}"


if __name__ == "__main__":
    # Пример использования:
    # Генерируем небольшой диапазон номеров карт
    cards = card_number_generator(1, 5)

    for card in cards:
        print(card)
