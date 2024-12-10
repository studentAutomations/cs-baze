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
pageToScrape = webdriver.Chrome(service=browser_driver, options=chrome_options)

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

    pageToScrape.get("https://cs.elfak.ni.ac.rs/nastava/mod/forum/search.php?id=4&words=&phrase=&notwords=&fullwords=&timefromrestrict=1&fromday=1&frommonth=1&fromyear=2023&fromhour=0&fromminute=0&hfromday=0&hfrommonth=0&hfromyear=0&hfromhour=0&hfromminute=0&htoday=1&htomonth=1&htoyear=1&htohour=1&htominute=1&forumid=&subject=&user=")
    responseT = pageToScrape.find_element(By.XPATH, '//*[@id="region-main"]')

    novosti_markdown = responseT.text  

    with open("novosti.md", "w") as novosti_file:
        novosti_file.write(novosti_markdown)

finally:
    page_to_scrape.quit()
