from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# set up webdriver
driver = webdriver.Chrome()

#open google
driver.get("http://www.google.com")

#find the search box using its name attribute
search_box = driver.find_element("name","q")

#type a search query
search_box.send_keys("Selenium testing in Windows")

#Simulate pressing the enter key
search_box.send_keys(Keys.RETURN)

#close the browser
driver.quit()