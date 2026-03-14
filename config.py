"""
Конфигурационный файл для скрипта автоматического ввода текста
"""

# Параметры скорости ввода (в словах в минуту)
MIN_WPM = 40  # Минимальная скорость (слов в минуту)
MAX_WPM = 60  # Максимальная скорость (слов в минуту)

# URL сайта для тестирования
TEST_URL = "https://www.livechat.com/typing-speed-test/#/"

# Параметры ожидания
PAGE_LOAD_TIMEOUT = 10  # Время ожидания загрузки страницы (в секундах)
ELEMENT_FIND_TIMEOUT = 10  # Время ожидания поиска элемента (в секундах)

# Параметры браузера
HEADLESS_MODE = False  # Запускать ли браузер в фоновом режиме (True/False)
CHROME_OPTIONS = [
    "--no-sandbox",
    "--disable-dev-shm-usage",
    "--disable-blink-features=AutomationControlled",
    "--disable-extensions",
    "--window-size=1920,1080"
]

# Селекторы для поиска элементов на странице
TEXT_SELECTORS = [
    ".words",
    ".sentence", 
    "[data-testid='words']",
    "[data-testid='sentence']",
    ".challenge-text",
    "#challenge-text",
    ".text-container",
    ".typing-area"
]

INPUT_SELECTORS = [
    "input[type='text']",
    "textarea",
    "[data-testid='input']",
    "[data-testid='typing-input']",
    "#typing-input",
    ".typing-input",
    "[contenteditable='true']",
    ".input-field"
]

# Текст для использования в случае, если не удается получить его с сайта
FALLBACK_TEXT = (
    "The quick brown fox jumps over the lazy dog. "
    "This is a sample text for typing practice. "
    "Programming is fun and challenging. "
    "Python is a versatile language used for various applications. "
    "Automation can save time and reduce repetitive tasks. "
    "Testing typing speed is important for productivity. "
    "Accuracy and speed both matter in typing tests. "
    "Regular practice improves typing skills significantly."
)