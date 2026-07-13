from src.processing import filter_by_state, sort_by_date

# --- Тесты для функции filter_by_state ---


def test_filter_by_state_default(sample_data):
    """Проверка фильтрации по умолчанию (EXECUTED)."""
    result = filter_by_state(sample_data)
    assert len(result) == 2
    assert all(item["state"] == "EXECUTED" for item in result)
    assert result[0]["id"] == 41428829


def test_filter_by_state_canceled(sample_data):
    """Проверка фильтрации по конкретному статусу (CANCELED)."""
    result = filter_by_state(sample_data, state_filter="CANCELED")
    assert len(result) == 2
    assert all(item["state"] == "CANCELED" for item in result)


def test_filter_by_state_empty_result(sample_data):
    """Проверка фильтрации, если совпадений нет."""
    result = filter_by_state(sample_data, state_filter="PENDING")
    assert result == []


def test_filter_by_state_missing_key():
    """Проверка работы, если у элемента вообще нет ключа 'state'."""
    invalid_data = [{"id": 1, "date": "2023-01-01T00:00:00.0"}]
    result = filter_by_state(invalid_data)
    assert result == []


# --- Тесты для функции sort_by_date ---


def test_sort_by_date_descending(sample_data):
    """Проверка сортировки по убыванию даты (по умолчанию)."""
    result = sort_by_date(sample_data)

    # Самая свежая дата должна быть первой (2019 год)
    assert result[0]["id"] == 41428829
    # Самая старая дата должна быть последней (июнь 2018)
    assert result[-1]["id"] == 939719570


def test_sort_by_date_ascending(sample_data):
    """Проверка сортировки по возрастанию даты (reverse=False)."""
    result = sort_by_date(sample_data, reverse=False)

    # Самая старая дата должна быть первой (июнь 2018)
    assert result[0]["id"] == 939719570
    # Самая свежая дата должна быть последней (2019 год)
    assert result[-1]["id"] == 41428829


def test_sort_by_date_empty():
    """Проверка сортировки пустого списка."""
    assert sort_by_date([]) == []
