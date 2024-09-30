import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

def wait_for_element(driver, by, value, timeout=20):
    try:
        element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, value)))
        return element
    except TimeoutException:
        print(f"Не удалось найти элемент по селектору {by} с значением {value}")
        return None

def click_elements(url):
    # Настройка драйвера для Chrome
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Открытие веб-интерфейса
        driver.get(url)
        print("Открыт URL:", url)

        time.sleep(1)

        link = wait_for_element(driver, By.ID, "navSection15")
        if link:
            print("Найден элемент ссылки с ID 'navSection15'")
            link.click()
            print("Ссылка нажата успешно")
        else:
            return

        time.sleep(1)

        button1 = wait_for_element(driver, By.ID, "start-task-btn")
        if button1:
            print("Найден элемент кнопки с ID 'start-task-btn'")
            button1.click()
            print("Кнопка 'Start Task' нажата успешно")
        else:
            return

        time.sleep(1)

        button2 = wait_for_element(driver, By.XPATH, "//button[contains(@class, 'btn') and contains(@class, 'btn-primary') and contains(@class, 'mb-4')]")
        if button2:
            print("Найден элемент кнопки с классом 'btn btn-primary mb-4'")
            button2.click()
            print("Кнопка 'Primary' нажата успешно")
        else:
            return

        time.sleep(1)

        # Имитируем CTRL+A
        body = driver.find_element(By.TAG_NAME, 'body')
        actions = ActionChains(driver)
        actions.click(body).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        print("Комбинация клавиш CTRL+A выполнена успешно")

        time.sleep(1)

        modal = wait_for_element(driver, By.CLASS_NAME, "modal-dialog.modal-dialog-scrollable.modal-dialog-full-width")
        if modal:
            print("Модальное окно найдено")

            modal_content = modal.find_element(By.CLASS_NAME, "modal-content.h-100")
            if modal_content:
                print("Контейнер внутри модального окна найден")

                print("HTML модального окна:", modal_content.get_attribute('outerHTML'))

                confirm_button = wait_for_element(driver, By.XPATH,
                                                  "//button[starts-with(@id, 'confirm-accounts-selection-btn-')]")
                if confirm_button:
                    confirm_button.click()
                    print("Кнопка 'Подтвердить выбор' нажата успешно")
                else:
                    print("Кнопка 'Подтвердить выбор' не найдена")

            else:
                print("Контейнер внутри модального окна не найден")
        else:
            print("Модальное окно не найдено")

        time.sleep(1)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:

        driver.quit()


url = input("Введите URL веб-интерфейса (например, http://localhost:55555): ")
click_elements(url)
