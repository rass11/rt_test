import unittest
from selenium import webdriver


class rt(unittest.TestCase):

    def test_login(self):
        browser = webdriver.Chrome()
        browser.maximize_window()
        # открыть ссылку
        browser.get("https://www.mantisbt.org/bugs/my_view_page.php")
        browser.find_element_by_xpath('//*[@id="breadcrumbs"]/ul/div/a[1]').click()

        # логин
        browser.find_element_by_id("username").send_keys('test735')

        browser.find_element_by_xpath('//*[@id="login-form"]/fieldset/input[2]').click()
        # пароль
        browser.find_element_by_id("password").send_keys('qwer')

        browser.find_element_by_xpath('//*[@id="login-form"]/fieldset/input[3]').click()
        browser.quit()


    def test_create_task(self):
        
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get("https://www.mantisbt.org/bugs/my_view_page.php")
        browser.find_element_by_xpath('//*[@id="breadcrumbs"]/ul/div/a[1]').click()

        # логин
        browser.find_element_by_id("username").send_keys('test735')

        browser.find_element_by_xpath('//*[@id="login-form"]/fieldset/input[2]').click()
        # пароль
        browser.find_element_by_id("password").send_keys('qwer')

        browser.find_element_by_xpath('//*[@id="login-form"]/fieldset/input[3]').click()
        # задача
        browser.find_element_by_xpath('//*[@id="navbar-container"]/div[2]/ul/li[1]/div/a').click()

        # выпадающий список
        browser.find_element_by_xpath('//*[@id="select-project-id"]').click()
        browser.find_element_by_xpath('//*[@id="select-project-id"]/option[16]').click()

        # выбрать проект
        browser.find_element_by_xpath('//*[@id="select-project-form"]/div/div[2]/div[2]/input').click()

        # данные
        browser.find_element_by_xpath('//*[@id="summary"]').send_keys('Тестовая задача')  # тема
        browser.find_element_by_xpath('//*[@id="description"]').send_keys(
            'тест_тест_тест_тест_тест_тест_тест_тест_тест_тест_')  # описание
        # создать задачу
        browser.find_element_by_xpath('//*[@id="report_bug_form"]/div/div[2]/div[2]/input').click()
        browser.quit()


    def test_check_task(self):

        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get("https://www.mantisbt.org/bugs/my_view_page.php")
        browser.find_element_by_xpath('//*[@id="breadcrumbs"]/ul/div/a[1]').click()

        # логин
        browser.find_element_by_id("username").send_keys('test735')

        browser.find_element_by_xpath('//*[@id="login-form"]/fieldset/input[2]').click()
        # пароль
        browser.find_element_by_id("password").send_keys('qwer')

        browser.find_element_by_xpath('//*[@id="login-form"]/fieldset/input[3]').click()
        # задача
        browser.find_element_by_xpath('//*[@id="navbar-container"]/div[2]/ul/li[1]/div/a').click()

        # выпадающий список
        browser.find_element_by_xpath('//*[@id="select-project-id"]').click()
        browser.find_element_by_xpath('//*[@id="select-project-id"]/option[16]').click()

        # выбрать проект
        browser.find_element_by_xpath('//*[@id="select-project-form"]/div/div[2]/div[2]/input').click()

        # данные
        browser.find_element_by_xpath('//*[@id="summary"]').send_keys('Тестовая задача')  # тема
        browser.find_element_by_xpath('//*[@id="description"]').send_keys(
            'тест_тест_тест_тест_тест_тест_тест_тест_тест_тест_')  # описание
        # создать задачу
        browser.find_element_by_xpath('//*[@id="report_bug_form"]/div/div[2]/div[2]/input').click()


        browser.get("https://www.mantisbt.org/bugs/my_view_page.php")
        browser.find_element_by_xpath('//*[@id="timeline"]/div[2]/div[3]/div[2]/span[2]/a').click()
        browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
