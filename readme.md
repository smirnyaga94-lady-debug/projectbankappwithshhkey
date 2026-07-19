# Учебный проект "Маски для банков"
## Описание:

Проект "Маски для банков" - это приложение для создания масок счетов или карт

## Установка:

1. Клонируйте репозиторий:
```
git@github.com:smirnyaga94-lady-debug/projectbankappwithshhkey.git
```

2. Установите зависимости:
```
pip install -r requirements.txt
```

## Использование:

1. Запустите программу:
```
python widget.py
```


## Тесты:

### Структура проекта

* `tests/` — папка со всеми тестами.
* `tests/conftest.py` — общие фикстуры и настройки.
* `src/` — исходный код вашего приложения.

### Как запустить тесты

Запуск всех тестов в проекте:
```bash
python -m pytest
```

Запуск конкретного файла с тестами:
```bash
python -m pytest tests/test_masks.py
python -m pytest tests/test_processing.py
python -m pytest tests/test_widget.py
```

Просмотр покрытия кода с помощью [pytest-cov](https://pytest-cov.readthedocs.io/):
```bash
python -m pytest --cov=название_модуля
```


