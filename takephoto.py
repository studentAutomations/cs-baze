from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.binary_location = "/usr/bin/google-chrome"  # Updated for GitHub runner

browser_driver = Service('/usr/bin/chromedriver')  # Updated for GitHub runner

page_to_scrape = webdriver.Chrome(service=browser_driver, options=chrome_options)

try:
    page_to_scrape.get("https://cs.elfak.ni.ac.rs/nastava/")
    page_to_scrape.find_element(By.LINK_TEXT, "Log in").click()
    time.sleep(2)

    page_to_scrape.find_element(By.LINK_TEXT, "OpenID Connect").click()
    time.sleep(2)

    mail = page_to_scrape.find_element(By.ID, "i0116")
    mail.send_keys(os.environ['MAIL'])  
    page_to_scrape.find_element(By.ID, "idSIButton9").click()
    time.sleep(2)

    password = page_to_scrape.find_element(By.ID, "i0118")
    password.send_keys(os.environ['PASSWORD'])  
    page_to_scrape.find_element(By.ID, "idSIButton9").click()
    time.sleep(2)

    page_to_scrape.find_element(By.ID, "idBtn_Back").click()
    time.sleep(2)

    page_to_scrape.find_element(By.LINK_TEXT, "Baze").click()
    time.sleep(2)

    link_element = page_to_scrape.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/section/div/div/ul/li[1]/div[3]/ul/li[1]/div/div/div[2]/div/a")
    link_element.click()
    time.sleep(2)

    responseT = page_to_scrape.find_element(By.XPATH, '//*[@id="region-main"]')

    height = responseT.size['height']
    width = responseT.size['width']     
    desired_width = max(width, 1200)  
    desired_height = min(height, 1000)
    page_to_scrape.set_window_size(desired_width, desired_height)     
    page_to_scrape.execute_script("arguments[0].scrollIntoView(true);", responseT)  
    responseT.screenshot('cs-baze-nova-obavestenja.png')

finally:
    page_to_scrape.quit()
