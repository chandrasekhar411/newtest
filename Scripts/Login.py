from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
# chrome_options = Options()
# chrome_options.add_argument("--headless")

# driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:\Chandra Sekhar\Softwares\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome("C:\Chandra Sekhar\Softwares\chromedriver_win32\chromedriver.exe")

# driver.set_page_load_timeout(10)

driver.get("https://google.com")

driver.maximize_window()

print(driver.title)

search_box =driver.find_element_by_name("q")

search_box.send_keys("Automation step by step")

search_box.send_keys(Keys.ESCAPE)
search_box.find_element_by_css_selector()
search_box.find_element_by_xpath()
# webdriver.ActionChains(driver).send_keys(Keys.ESCAPE)

driver.find_element_by_name("btnK").click()

driver.close()

driver.quit()

print("Test Completed")
