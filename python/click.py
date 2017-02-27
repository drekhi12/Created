import time
from selenium import webdriver
from selenium.webdriver.common.by import By
user=raw_input("Enter the username : " )
passw=raw_input("Enter the password : ")
i=input("How many people you wanna follow: ")
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('https://www.instagram.com')
driver.find_element_by_link_text('Log in').click()
username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')
username.send_keys(user)
password.send_keys(passw)
password.submit()
driver.find_element_by_link_text('Find People').click()

while i>0:
    driver.find_element(By.XPATH, '//button[text()="Follow"]').click()
    time.sleep(2)
    i=i-1

time.sleep(5)
driver.close()
print "Run this script multiple times as Instagram has a certain limit to follow people "

