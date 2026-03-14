# Автоматизатор теста печати на сайте https://www.livechat.com/typing-speed-test/#/

Проект — скрипт автоматически через хром драйвер, проходит тест, можно настроить под любой нужный результат, скорость печати

## Требования

- Python 3.11+ (в проекте есть `.venv`)

## Установка

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Зависимости из `requirements.txt` нужны только для старых Selenium-экспериментов; для локальной практики они не обязательны.

## Запуск

Локальная практика (по умолчанию):

```powershell
.\.venv\Scripts\python.exe run_project.py
```

Диагностика окружения:

```powershell
.\.venv\Scripts\python.exe run_project.py doctor
```

Параметры локальной практики:

```powershell
.\.venv\Scripts\python.exe run_project.py practice --words 35 --seed 1 --show-diff
.\.venv\Scripts\python.exe run_project.py practice --prompt "Hello world"
.\.venv\Scripts\python.exe run_project.py practice --prompt-file .\text.txt
```

