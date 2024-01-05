from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chr_options)
driver.get("http://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
title = driver.title
print(title)
driver.implicitly_wait(20)
username = driver.find_element(By.XPATH, "//*[@name='username']")
username.send_keys("Admin")
password = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
password.send_keys("admin123")
submit = driver.find_element(By.XPATH, "//button[@type='submit']")
submit.click()
assert driver.title == 'OrangeHRM'
driver.find_element(By.LINK_TEXT, "My Info").click()
driver.find_element(By.NAME, "firstName").send_keys("test123")
driver.find_element(By.XPATH, "//form[@class='oxd-form']/div[5]/button[1]").click()
