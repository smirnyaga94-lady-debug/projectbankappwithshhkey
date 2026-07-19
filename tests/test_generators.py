import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


class TestTransactionFunctions:

    @pytest.fixture
    def sample_transactions(self):
        """Фикстура с реальным примером входных данных."""
        return [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            },
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188",
            },
            {
                "id": 873106923,
                "state": "EXECUTED",
                "date": "2019-03-23T01:09:46.296404",
                "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 44812258784861134719",
                "to": "Счет 74489636417521191160",
            },
            {
                "id": 895315941,
                "state": "EXECUTED",
                "date": "2018-08-19T04:27:37.904916",
                "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод с карты на карту",
                "from": "Visa Classic 6831982476737658",
                "to": "Visa Platinum 8990922113665229",
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
                "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Visa Platinum 1246377376343588",
                "to": "Счет 14211924144426031657",
            },
        ]

    # --- ТЕСТЫ ДЛЯ filter_by_currency ---

    def test_filter_by_currency_usd(self, sample_transactions):
        """Проверка успешной фильтрации транзакций в USD (должно быть 3 штуки)."""
        result = list(filter_by_currency(sample_transactions, "USD"))
        assert len(result) == 3
        assert result[0]["id"] == 939719570
        assert result[1]["id"] == 142264268
        assert result[2]["id"] == 895315941

    def test_filter_by_currency_rub(self, sample_transactions):
        """Проверка успешной фильтрации транзакций в рублях (должно быть 2 штуки)."""
        result = list(filter_by_currency(sample_transactions, "RUB"))
        assert len(result) == 2
        assert result[0]["id"] == 873106923
        assert result[1]["id"] == 594226727

    def test_filter_by_currency_missing(self, sample_transactions):
        """Проверка случая, когда транзакции в заданной валюте (EUR) отсутствуют."""
        result = list(filter_by_currency(sample_transactions, "EUR"))
        assert len(result) == 0

    def test_filter_by_currency_empty_list(self):
        """Проверка, что генератор стабильно работает с пустым списком на входе."""
        result = list(filter_by_currency([], "USD"))
        assert result == []

    def test_filter_by_currency_no_currency_key(self):
        """Проверка, что генератор не падает, если в структуре данных нет нужных ключей."""
        corrupted_data = [{"id": 111, "description": "Сломанная транзакция"}, {"id": 222, "operationAmount": {}}]
        result = list(filter_by_currency(corrupted_data, "USD"))
        assert result == []

    # --- ТЕСТЫ ДЛЯ transaction_descriptions ---

    def test_transaction_descriptions_correct(self, sample_transactions):
        """Проверка, что функция возвращает точные текстовые описания по порядку."""
        expected_descriptions = ["Перевод организации", "Перевод со счета на счет", "Перевод со счета на счет", "Перевод с карты на карту", "Перевод организации"]
        result = list(transaction_descriptions(sample_transactions))
        assert result == expected_descriptions

    def test_transaction_descriptions_empty_list(self):
        """Проверка работы функции обработки описаний с пустым списком."""
        result = list(transaction_descriptions([]))
        assert result == []

    def test_transaction_descriptions_fallback(self):
        """Проверка устойчивости: возврат заглушки, если ключ 'description' потерян."""
        mixed_data = [{"id": 999, "description": "Всё ок"}, {"id": 888}]  # Тут ключа нет
        result = list(transaction_descriptions(mixed_data))
        assert result == ["Всё ок", "Описание отсутствует"]


# --- НАБОР ТЕСТОВ С ПАРАМЕТРИЗАЦИЕЙ ---


class TestCardNumberGenerator:

    @pytest.mark.parametrize(
        "start, end, expected_count, first_card, last_card",
        [
            # Проверка стандартного небольшого диапазона с ведущими нулями
            (1, 3, 3, "0000 0000 0000 0001", "0000 0000 0000 0003"),
            # Граничное условие: диапазон из одного элемента
            (55, 55, 1, "0000 0000 0000 0055", "0000 0000 0000 0055"),
            # Нижняя граница (нули)
            (0, 1, 2, "0000 0000 0000 0000", "0000 0000 0000 0001"),
            # Верхняя граница диапазона (максимальные значения номеров карт)
            (9999999999999998, 9999999999999999, 2, "9999 9999 9999 9998", "9999 9999 9999 9999"),
        ],
    )
    def test_generator_range_and_boundaries(self, start, end, expected_count, first_card, last_card):
        """Проверяет правильность количества карт, крайние значения диапазона и их значения."""
        generator = card_number_generator(start, end)
        cards = list(generator)

        assert len(cards) == expected_count
        assert cards[0] == first_card
        assert cards[-1] == last_card

    @pytest.mark.parametrize("start, end", [(1, 5), (100000, 100005), (9999999999999990, 9999999999999995)])
    def test_card_number_formatting(self, start, end):
        """Проверяет корректность строкового формата карт (Длина 19, блоки по 4 цифры через пробелы)."""
        generator = card_number_generator(start, end)

        for card in generator:
            # Общая длина строки "XXXX XXXX XXXX XXXX" должна быть ровно 19 символов
            assert len(card) == 19

            # Проверяем, что на нужных позициях стоят пробелы
            assert card[4] == " "
            assert card[9] == " "
            assert card[14] == " "

            # Проверяем, что блоки состоят только из цифр
            blocks = card.split(" ")
            assert len(blocks) == 4
            for block in blocks:
                assert len(block) == 4
                assert block.isdigit()

    def test_generator_termination(self):
        """Проверяет, что генератор корректно завершает работу после выдачи последнего элемента."""
        generator = card_number_generator(1, 2)

        # Забираем доступные элементы
        next(generator)
        next(generator)

        # Следующий вызов должен вызывать исключение StopIteration, сигнализируя о конце генерации
        with pytest.raises(StopIteration):
            next(generator)

    def test_invalid_range_empty_result(self):
        """Проверяет поведение, если начальное значение больше конечного (должен вернуть пустой результат)."""
        generator = card_number_generator(10, 5)
        cards = list(generator)
        assert len(cards) == 0
