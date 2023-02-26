from selenium import webdriver # chromedriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# navigation options
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

# driver
driver_path = 'C:\\Users\\Maxi\\Desktop\\Computacion\\Python\\AUTOMATIZATION\\chromedriver.exe'
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)
# url of the website
website = 'https://www.eltiempo.es/'
# open the website
driver.get(website)
# button accept the cookies, wait for the cookies window to popup and accept when clickable
# five seconds to wait
# then we add a tuple with the css selector and the button identificator, replacing the ' ' for
# '.' so there is no interpretation errors and finally we click it
WebDriverWait(driver, 5)\
    .until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '''button.didomi-components-button didomi-button 
        didomi-dismiss-button didomi-components-button--color 
        didomi-button-highlight highlight-button'''.replace(' ', '.'))
    )).click()
# now we look for the time in Madrid in the search bar
WebDriverWait(driver, 5)\
    .until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'input#term')
    )).send_keys('Madrid')
# click search madrid
WebDriverWait(driver, 5)\
    .until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR,'i.icon icon-sm icon-city'.replace(' ', '.'))
    )).click()
# xpath:
WebDriverWait(driver, 5)\
    .until(
    EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[5]/div[1]/div[4]/div/main/section[3]/section/div/article/div[1]')
    ))
text = driver.find_element(by=By.XPATH,
                           value='/html/body/div[5]/div[1]/div[4]/div/main/section[3]/section/div/article/div[1]')
driver.close()

with open('text_weather.txt', 'w') as f:
    f.writelines(text.text)
