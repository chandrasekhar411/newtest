from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
# chrome_options = Options()
# chrome_options.add_argument("--headless")

# driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:\Chandra Sekhar\Softwares\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome("C:\Chandra Sekhar\Softwares\chromedriver_win32\chromedriver.exe")

# driver.set_page_load_timeout(10)

driver.get("https://www.facebook.com/")

driver.maximize_window()

print(driver.title)

# driver.find_element_by_xpath("//input[@name='email']").send_keys("chandra@gmail.com")
# driver.find_element_by_xpath("//input[@name='pass']").send_keys("134657798765")
# driver.find_element_by_xpath("//input[@type='submit']").click()



driver.find_element_by_name("firstname").send_keys("Test")
driver.find_element_by_name("lastname").send_keys("Test")
driver.find_element_by_name("reg_email__").send_keys("Test@gmail.com")
driver.find_element_by_name("reg_email_confirmation__").send_keys("Test@gmail.com")

driver.find_element_by_name("reg_passwd__").send_keys("Test123")
driver.find_element_by_name("birthday_day").send_keys("10")
driver.find_element_by_name("birthday_month").send_keys("May")
driver.find_element_by_name("birthday_year").send_keys("1990")
driver.find_element_by_xpath("//input[@name='sex' and @value='1']").click()
driver.find_element_by_xpath("//input[@name='sex' and @value='2']").click()

# driver.find_element_by_xpath("//input[@name='sex' and @value='-1']").click()
#
# driver.find_element_by_name("preferred_pronoun").send_keys("She: 'Wish her a happy birthday!'")
#driver.find_element_by_name("custom_gender").send_keys("test")

# driver.find_element_by_name("websubmit").click()



#
# driver.close()
#
# driver.quit()

print("Test Completed")