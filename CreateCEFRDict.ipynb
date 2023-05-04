# import all essential (according to CEFR) English words to excel file

# import essential libs + download Chrome WebDriver on your python folder
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select

# launch url
url = "https://www.englishprofile.org/wordlists/evp"

# create a new Chrome session
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get(url)

# wait until the page is loaded
timer=WebDriverWait(driver, 10).until(lambda driver: 
                                      driver.execute_script('return document.readyState') == 'complete')
def wait_until(timer, timeout, period=0.25, *args, **kwargs):
  mustend = time.time() + timeout
  while time.time() < mustend:
    if timer(*args, **kwargs): return True
    time.sleep(period)
  return False

# click on the "select all levels" button
driver.find_element_by_css_selector('#adminForm > div:nth-child(1) \
                                    > div.report-filters.pull-left > div > fieldset > div > label:nth-child(7) > span').click()
driver.find_element_by_css_selector('#adminForm > div:nth-child(1) \
                                    > div:nth-child(3) > button').click()

# wait until the page is reloaded
timer=WebDriverWait(driver, 10).until(lambda driver: 
                                      driver.execute_script('return document.readyState') == 'complete')
def wait_until(timer, timeout, period=0.25, *args, **kwargs):
  mustend = time.time() + timeout
  while time.time() < mustend:
    if timer(*args, **kwargs): return True
    time.sleep(period)
  return False

# click on the "show all" button to see all words on the one page
view_size=Select(driver.find_element_by_id("limit"))
view_size.select_by_visible_text('All')

# wait until the page is reloaded
timer=WebDriverWait(driver, 10).until(lambda driver: 
                                      driver.execute_script('return document.readyState') == 'complete')
def wait_until(timer, timeout, period=0.25, *args, **kwargs):
  mustend = time.time() + timeout
  while time.time() < mustend:
    if timer(*args, **kwargs): return True
    time.sleep(period)
  return False

# import essential libs to transfer data from web page to eccel file
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import shutil

# get data
page_source = driver.page_source
df=pd.read_html(page_source)
df = df[0]
# add new column with language type
df['EnglishType']='British English'
df.to_excel("output.xlsx",sheet_name='AllWords')

# move file to the selected folder
source = os.path.abspath("output.xlsx") 
destination = "*****.xlsx"
shutil.move(source,destination)

# the end
print("The End!")



