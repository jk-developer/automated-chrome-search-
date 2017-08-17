from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
# create a new Firefox session
path = "C:\\Selenium drivers\\chromedriver.exe"

driver = webdriver.Chrome(path)
driver.implicitly_wait(30)
driver.maximize_window()
 
# navigate to the application home page
driver.get("http://www.google.com")
 
# get the search textbox
search_field = driver.find_element_by_id("lst-ib")
search_field.clear()
 
# enter search keyword and submit
search_field.send_keys("how to use the xpath in selenium web automation")
search_field.submit()
 
# closing the web chrome webdriver
driver.quit()
 


