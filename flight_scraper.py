from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart

# origin_loc = input("Where are you leaving from?")
# origin_date = input("When do you want to leave?")
# destination_loc = input("Where do you want to go?")
isOneway = False


DRIVER_PATH = '/Users/ezduanmu/Downloads/chromedriver'

driver = webdriver.Chrome(executable_path=DRIVER_PATH)

driver.get('https://www.expedia.com/')

# 
primary_options = driver.find_element_by_id("uitk-tabs-button-container")
primary_options_list = primary_options.find_elements_by_tag_name("li")
for option in primary_options_list:
    if option.text is not None and "flights" in option.text.lower():
        flight_button = option
flight_button.click()

if !isOneway:
    travel_options = driver.find_element_by_id("uitk-tabs-button-container")
    travel_options_div = travel_options.find_elements_by_tag_name("div")
    travel_options_list = travel_options_div[0].find_elements_by_tag_name("li")
    for option in travel_options_list:
        if option.text is not None and "one-way" in option.text.lower():
            oneway_button = option
            oneway_button.click()

# Quit chromedriver at end of program
time.sleep(10)
driver.quit()