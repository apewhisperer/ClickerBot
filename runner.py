from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time

i = 1000
while(i > 0) :
    #start firefox
    s = Service('./geckodriver-v0.31.0-win64/geckodriver.exe')
    driver = webdriver.Firefox(service=s)
    #get page
    driver.get("http://www.page.com")
    #get element by id
    button = driver.find_element_by_id('id')
    button.click()
    time.sleep(2)
    #get element by xpath
    elem = driver.find_element_by_xpath('/html/body/xpath')
    elem.click()
    time.sleep(2)
    driver.close()
    i -= 1