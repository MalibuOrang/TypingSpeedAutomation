from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://www.livechat.com/typing-speed-test/#/')
time.sleep(5)

try:
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.common.keys import Keys
    
    wrapper = driver.find_element(By.CSS_SELECTOR, 'div.tst-input-wrapper')
    ActionChains(driver).move_to_element(wrapper).click().perform()

    for i in range(25):
        # find the currently active word
        active_span = driver.find_element(By.CSS_SELECTOR, '.tst-input-wrapper span.u-pl-0')
        word = active_span.text.strip()
        print(f'Typing word {i}: {word}')
        
        actions = ActionChains(driver)
        for c in word:
            actions.send_keys(c).perform()
            time.sleep(0.01)
        actions.send_keys(Keys.SPACE).perform()
        time.sleep(0.05)
        
except Exception as e:
    print('ERROR:', e)
finally:
    driver.quit()
