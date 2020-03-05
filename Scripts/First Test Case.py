import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = webdriver.ChromeOptions()
# chrome_options = Options()
# chrome_options.add_argument("--headless")

# driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:\Chandra Sekhar\Softwares\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome("C:\Chandra Sekhar\Softwares\chromedriver_win32\chromedriver.exe")

# driver.set_page_load_timeout(10)

driver.get("https://google.com")

driver.maximize_window()

print(driver.title)

driver.find_element_by_name("q").send_keys("Automation step by step")
driver.add_cookie()


driver.find_element_by_name("btnK").click()

driver.close()

driver.quit()

print("Test Completed")

























