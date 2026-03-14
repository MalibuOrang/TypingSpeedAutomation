# Использование

## Локальная практика печати

```powershell
.\.venv\Scripts\python.exe run_project.py
```

Опции:

- `--words N` — сколько слов брать из текста (по умолчанию 35)
- `--seed N` — фиксировать случайный выбор текста
- `--prompt "..."` — свой текст
- `--prompt-file path` — загрузить текст из файла (UTF‑8)
- `--show-diff` — показать отличия после ввода

Примеры:

```powershell
.\.venv\Scripts\python.exe run_project.py practice --words 25
.\.venv\Scripts\python.exe run_project.py practice --seed 42 --show-diff
```

## Проверка окружения

```powershell
.\.venv\Scripts\python.exe run_project.py doctor
```

