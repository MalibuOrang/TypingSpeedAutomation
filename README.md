# Автоматизатор теста печати на сайте https://www.livechat.com/typing-speed-test/#/

Проект — скрипт автоматически через хром драйвер, проходит тест, можно настроить под любой нужный результат, скорость печати

## Требования

- Python 3.11+ (в проекте есть `.venv`)

## Установка

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```
Зависимости из `requirements.txt` нужны только для Selenium; 
## Запуск

```powershell
.\.venv\Scripts\python.exe run_project.py
```

Диагностика окружения:

```powershell
.\.venv\Scripts\python.exe run_project.py doctor
```
