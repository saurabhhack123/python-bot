from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
import time

def page_is_loaded(driver):
    return driver.find_element_by_tag_name("body") != None

game1 = [0, 25, 9, 14, 35, 19.5, 10.5, 2, 1]
game2 = [0, 23,7,13,35,19.00,12.50,2,1]
game3 = [0, 42, 11, 16, 40, 20, 11, 5,1]
game4 = [0, 40,10,14,36,19.50,11.00,4,1]
game5 = [0, 26, 9, 14, 36, 19.0, 11.0, 2 ,1]
game6 = [0, 47,12,16,36,17.5,10.50,5,2]
game7 = [0, 47, 13, 16, 40, 17.50, 10.50, 6 ,2]
game8 = [0, 47, 13,16,50,17.50,10.50,4,2]

games = [game1, game2, game3, game4, game5, game6, game7, game8]

dates = [11, 25, 9, 23, 6, 20, 4, 18]

# Create a new instance of the Firefox driver
driver = webdriver.Chrome('/Users/saurabhhack/Downloads/chromedriver')

driver.get("https://vbcourse2.knowledgematters.com/")
wait = ui.WebDriverWait(driver, 10)
wait.until(page_is_loaded)
email_field = driver.find_element_by_name("email")
email_field.send_keys("***")
password_field = driver.find_element_by_name("password")
password_field.send_keys("**")
password_field.send_keys(Keys.RETURN)

driver.get("https://vbcourse2.knowledgematters.com/course/view/208519")
wait = ui.WebDriverWait(driver, 10)
wait.until(page_is_loaded)

# this should open window

lesson_sim_link = driver.find_element_by_link_text("Continue Sim")
print lesson_sim_link
lesson_sim_link.click()

# driver.find_element_by_css_selector('.lesson_sim_link').click()
# driver.get("https://vbcourse2.knowledgematters.com/sim/load/686043")
driver.switch_to_window(driver.window_handles[-1])
title=driver.title

wait = ui.WebDriverWait(driver, 30)
wait.until(page_is_loaded)
print driver
# go to the google home page
# driver.get("https://vbcourse2.knowledgematters.com/sim/load/686043")
# the page is ajaxy so the title is originally this:

print driver.title
time.sleep(30)
wait = WebDriverWait(driver, 20)
print "loaded"
#button = wait.until(EC.element_to_be_clickable((By.ID,"menu-bar")))
"""
# beginning
element = driver.find_element_by_id("calendar2")
driver.execute_script("arguments[0].click();", element)
details = driver.find_element_by_class_name("btn btn-mini")
driver.execute_script("arguments[0].click();", details)
driver.execute_script("arguments[0].click();", details)
checkbox = driver.find_element_by_class_name("checkbox")
driver.execute_script("arguments[0].click();", checkbox)
close = driver.find_element_by_class_name("ui-icon ui-icon-closethick")
driver.execute_script("arguments[0].click();", close)
close = driver.find_element_by_class_name("ui-icon ui-icon-closethick")
driver.execute_script("arguments[0].click();", close)
"""

print driver

for i, game in enumerate(games):
   
    element = driver.find_element_by_id("staffing")
    button = driver.find_elements_by_class_name("caret")[2]
    driver.execute_script("arguments[0].click();", button)
    driver.execute_script("arguments[0].click();", element)

    staffing_fields = driver.find_elements_by_class_name("input-mini")
    for k, field in enumerate(staffing_fields):
        field.clear()
        field.send_keys(game[k])
    time.sleep(10)
    ok = driver.find_elements_by_tag_name("button")[5]
    ok.click();
    # ok.click();
    
    time.sleep(5)
    element = driver.find_element_by_id("parkingAction")
    button = driver.find_elements_by_class_name("caret")[2]
    driver.execute_script("arguments[0].click();", button)
    driver.execute_script("arguments[0].click();", element)
    
    time.sleep(5)
    parking_fields = driver.find_elements_by_class_name("input-mini")
    for j, field in enumerate(parking_fields):
        field.clear()
        field.send_keys(str(game[j + 5]))
    
    time.sleep(5)
    ok = driver.find_elements_by_tag_name("button")[5]
    ok.click()
    # ok.click()
    
    runToButton = driver.find_element_by_id("run-to-button-icon")
    runToButton.click()
    str_date = str(dates[i])
    print str_date
    date = driver.find_element_by_class_name("ui-state-active")
    # date = driver.find_element_by_link_text(str_date)
    date.click()
    time.sleep(5)
    print i
    if (i == 0):
        slider = driver.find_elements_by_class_name("ui-slider-handle")[0]
        print("slider")
        driver.execute_script("arguments[0].click();", slider)
        ActionChains(driver).click().perform()
        time.sleep(5)
        slider.send_keys(Keys.ARROW_RIGHT)
        time.sleep(5)
        print("slider2")
        slider.send_keys(Keys.ARROW_RIGHT)
        print("slider1")
        time.sleep(5)
        slider.send_keys(Keys.SPACE)

    time.sleep(22)
    close = driver.find_element_by_class_name("ui-icon-closethick")
    driver.execute_script("arguments[0].click();", close)



"""
try:
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))

    # You should see "cheese! - Google Search"
    print driver.title

finally:
    driver.quit()
"""