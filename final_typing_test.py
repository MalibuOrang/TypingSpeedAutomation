"""
Финальная версия скрипта для автоматического прохождения теста скорости печати
на сайте https://www.livechat.com/typing-speed-test/#/

Скрипт позволяет:
- Вводить текст с заданной скоростью (40-60 слов в минуту)
- Автоматически находить слова внутри div.tst-input-wrapper
- Эмулировать ввод с клавиатуры через ActionChains
"""
import time
import random
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException, StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

class TypingTestBot:
    def __init__(self, min_wpm=40, max_wpm=60, test_url="https://www.livechat.com/typing-speed-test/#/", headless=False):
        self.min_wpm = min_wpm
        self.max_wpm = max_wpm
        self.test_url = test_url
        self.headless = headless
        self.driver = None
        self.wait = None
        
    def calculate_delay_for_wpm(self, wpm):
        """
        Рассчитывает задержку между символами для достижения заданной скорости WPM
        Среднее слово = 5 символов
        """
        chars_per_minute = wpm * 5
        chars_per_second = chars_per_minute / 60
        delay_between_chars = 1 / chars_per_second
        return delay_between_chars

    def setup_driver(self):
        """
        Настраивает и возвращает экземпляр веб-драйвера
        """
        chrome_options = Options()
        if self.headless:
            chrome_options.add_argument("--headless")
        
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--window-size=1920,1080")
        
        # Оставляем браузер открытым после завершения скрипта
        chrome_options.add_experimental_option("detach", True)
        
        try:
            service = Service('chromedriver.exe')
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            self.wait = WebDriverWait(self.driver, 10)
            return True
        except WebDriverException as e:
            print(f"Ошибка при инициализации Chrome драйвера: {str(e)}")
            return False

    def type_word_with_delay(self, word):
        """
        Вводит слово с задержкой между символами, эмулируя клавиатуру
        """
        wpm = random.uniform(self.min_wpm, self.max_wpm)
        delay = self.calculate_delay_for_wpm(wpm)
        
        actions = ActionChains(self.driver)
        
        for char in word:
            # Эмулируем нажатие клавиши
            actions.send_keys(char).perform()
            
            # Добавляем небольшую вариацию задержки для более естественного ввода
            variation = random.uniform(-0.01, 0.01)
            time.sleep(max(0.01, delay + variation))
            
        # Обязательно нажимаем пробел после слова
        actions.send_keys(Keys.SPACE).perform()
        time.sleep(max(0.01, delay + random.uniform(-0.01, 0.01)))

    def run_test(self, duration=120):
        """
        Запускает тест скорости печати
        """
        print(f"Запуск теста скорости печати...")
        print(f"Скорость ввода: {self.min_wpm}-{self.max_wpm} WPM")
        print(f"URL: {self.test_url}")
        print(f"Фоновый режим: {'Да' if self.headless else 'Нет'}")
        
        if not self.setup_driver():
            return False
        
        try:
            print(f"Открытие страницы: {self.test_url}")
            self.driver.get(self.test_url)
            
            print("Ожидание загрузки страницы (5 сек)...")
            time.sleep(5)
            
            # Ждем появления враппера со словами
            try:
                wrapper_selector = "div.tst-input-wrapper"
                self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, wrapper_selector)))
            except Exception:
                print(f"Не удалось найти элемент по селектору '{wrapper_selector}'")
                return False
                
            print("Поле ввода (wrapper) найдено!")

            # Эмулируем клик по странице/врапперу для активации фокуса, если тест этого требует
            try:
                wrapper = self.driver.find_element(By.CSS_SELECTOR, wrapper_selector)
                ActionChains(self.driver).move_to_element(wrapper).click().perform()
            except:
                self.driver.find_element(By.TAG_NAME, "body").click()
                
            time.sleep(1)
            
            print("Поле ввода загружено. Начинаю эмуляцию печати...")
            
            start_time = time.time()
            words_typed = 0
            
            # Печатаем, пока не выйдет время
            while (time.time() - start_time) < duration:
                # Находим текущее активное слово по специальному классу u-pl-0
                try:
                    active_span = self.driver.find_element(By.CSS_SELECTOR, "div.tst-input-wrapper span.u-pl-0")
                    word_to_type = active_span.text.strip()
                except Exception:
                    # Ждем если класс временно исчез или подгружаются слова
                    time.sleep(0.1)
                    continue
                    
                if not word_to_type:
                    time.sleep(0.1)
                    continue
                
                # Печатаем текущее слово
                self.type_word_with_delay(word_to_type)
                words_typed += 1
                
                if words_typed % 10 == 0:
                    print(f"Напечатано {words_typed} слов... (осталось {max(0, int(duration - (time.time() - start_time)))} сек)")
                    
            print(f"Время тестирования ({duration} сек) вышло.")
            print(f"Тест завершен! Всего напечатано: {words_typed} слов.")
            
            return True
            
        except KeyboardInterrupt:
            print("\nПрограмма прервана пользователем")
            return False
        except Exception as e:
            print(f"Произошла ошибка во время теста: {str(e)}")
            return False

    def close(self):
        """
        Закрывает браузер
        """
        if self.driver:
            try:
                self.driver.quit()
                print("Браузер закрыт")
            except:
                print("Не удалось корректно закрыть браузер")

def main():
    parser = argparse.ArgumentParser(description='Автоматический тест скорости печати')
    parser.add_argument('--min-wpm', type=int, default=40, 
                       help='Минимальная скорость ввода (слов в минуту), по умолчанию 40')
    parser.add_argument('--max-wpm', type=int, default=60, 
                       help='Максимальная скорость ввода (слов в минуту), по умолчанию 60')
    parser.add_argument('--url', type=str, default='https://www.livechat.com/typing-speed-test/#/',
                       help='URL для теста скорости печати')
    parser.add_argument('--headless', action='store_true', 
                       help='Запуск в фоновом режиме (без GUI)')
    parser.add_argument('--duration', type=int, default=60, 
                       help='Время ввода текста (в секундах), по умолчанию 60')
    
    args = parser.parse_args()
    
    bot = TypingTestBot(
        min_wpm=args.min_wpm,
        max_wpm=args.max_wpm,
        test_url=args.url,
        headless=args.headless
    )
    
    try:
        success = bot.run_test(duration=args.duration)
        if success:
            print("Скрипт успешно отработал!")
        else:
            print("Во время выполнения произошли ошибки.")
            
        print("Браузер остается открытым. Вы можете закрыть его вручную.")
    except Exception as e:
        print(f"Критическая ошибка: {str(e)}")

if __name__ == "__main__":
    main()