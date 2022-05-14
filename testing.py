from random import random

from selenium import webdriver
import os
import time
from threading import Thread
from random import randint

driver = webdriver.Chrome("chromedriver.exe")
Thread(target=lambda: os.system('python manage.py runserver')).start()
time.sleep(10)
driver.get('http://127.0.0.1:8000/')


def login_page():
    driver.find_element_by_xpath('//input[@name="phone"]').send_keys('dhruvppatel2506@gmail.com')
    time.sleep(1)
    driver.find_element_by_xpath('//input[@name="otp"]').send_keys('2345')
    time.sleep(1)
    driver.find_element_by_xpath('//button[@name="Login"]').click()


def voting_page():
    driver.find_element_by_xpath('//button[@type="button home-button"]').click()
    elems = driver.find_elements_by_xpath('//label[@class="form-check-label pt-1"]')
    elems[randint(0, 3)].click()
    time.sleep(1)
    driver.find_element_by_xpath('//button[@type="submit"]').click()
    time.sleep(1)
    driver.back()
    driver.back()


def stats_page():
    driver.find_element_by_xpath('//button[@type="button contact-button"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//label[@for="GJ"]').click()
    time.sleep(1)
    elem = driver.find_elements_by_xpath('//button')
    elem[1].click()


login_page()
voting_page()
stats_page()

time.sleep(3)
driver.quit()