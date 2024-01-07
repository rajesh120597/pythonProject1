from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Day1():
    a = 1

    def launch_browser(self, url):
        chr_options = webdriver.ChromeOptions()
        chr_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chr_options)
        driver.get(url)
        driver.maximize_window()
        return driver


# obj1 = Day1()
url = "https://app.vwo.com"


# driver = obj1.launch_browser(url)
# driver.close()

class Day2(Day1):

    def locators_test(self):
        obj1 = Day1()
        driver = obj1.launch_browser(url)
        driver.find_element(By.ID, "login-username").send_keys("test_test123@test123.com")
        # Test@123
        driver.find_element(By.NAME, "password").send_keys("Test@123")
        driver.find_element(By.ID, "js-login-btn").click()
        driver.implicitly_wait(10)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.title_is("Dashboard"))
        print(driver.title)
        assert driver.title == "Dashboard"
        driver.find_element(By.XPATH, "//div[@id='js-side-navigator']/ul/li[2]/button").click()


obj2 = Day2()
obj2.locators_test()
