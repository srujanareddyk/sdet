from behave import *
from selenium import webdriver
import time

# def selenium_browser_chrome():
driver = webdriver.Chrome('/Users/swetha/Downloads/chromedriver')
driver.get('https://www.dice.com/')
driver.maximize_window()
time.sleep(2)
# job_title_web_element = driver.find_element_by_xpath("//*[@data-cy='typeahead-input']").send_keys("SDET")
# job_location_web_element = driver.find_element_by_xpath("//*[@id='google-location-search']").clear()
# job_location_web_element = driver.find_element_by_xpath("//*[@id='google-location-search']").send_keys("Oregon")
# search_web_element = driver.find_element_by_xpath("//*[@data-cy='submit-search-button']").click()
# time.sleep(5)


@given('User enters "SDET" and "Oregon" in Jobs and location text boxes respectively')
def step_impl(context):
    job_title_web_element = driver.find_element_by_xpath("//*[@data-cy='typeahead-input']").send_keys("SDET")
    job_location_web_element = driver.find_element_by_xpath("//*[@id='google-location-search']").clear()
    job_location_web_element = driver.find_element_by_xpath("//*[@id='google-location-search']").send_keys("Oregon")
    pass

@when('the user clicks Search Jobs')
def step_impl(context):
    search_web_element = driver.find_element_by_xpath("//*[@data-cy='submit-search-button']").click()
    time.sleep(5)
    pass

@then('all the related jobs are displayed in the search results')
def step_impl(context):
    # selenium_browser_chrome()
    pass