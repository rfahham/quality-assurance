from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 

driver = webdriver.Chrome() 
driver.get("https://seusite.com/login") 

username = driver.find_element_by_id("username") 
password = driver.find_element_by_id("password") 

username.send_keys("usuario") 
password.send_keys("senha") 

driver.find_element_by_tag_name("button").click() 

assert "Dashboard" in driver.title 
driver.quit()