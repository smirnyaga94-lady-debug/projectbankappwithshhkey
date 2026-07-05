from datetime import datetime


def filter_by_state(transactions: list[dict], state_filter: str = "EXECUTED") -> list[dict]:
    """
    Фильтрует список словарей по ключу 'state'.

    :param transactions: Список словарей с данными.
    :param state_filter: Значение для фильтрации (по умолчанию 'EXECUTED').
    :return: Новый список отфильтрованных словарей.
    """
    return [item for item in transactions if item.get("state") == state_filter]


def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    """
    Сортирует список словарей по ключу 'date'.
    :param data: Список словарей
    :param reverse: Порядок сортировки (True — убывание, False — возрастание)
    :return: Новый отсортированный список
    """
    return sorted(data, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=reverse)


data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
# Фильтрация по умолчанию ('EXECUTED')
executed_only = filter_by_state(data)
print(executed_only)

# Фильтрация по другому статусу
canceled_only = filter_by_state(data, state_filter="CANCELED")
print(canceled_only)

# сортировка по дате
print(sort_by_date(data))
