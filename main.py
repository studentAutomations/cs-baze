from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

browser_driver = Service('/usr/lib/chromium-browser/chromedriver')

page_to_scrape = webdriver.Chrome(service=browser_driver)
page_to_scrape.get("https://cs.elfak.ni.ac.rs/nastava/")

page_to_scrape.find_element(By.LINK_TEXT, "Log in").click()

time.sleep(5)

page_to_scrape.find_element(By.LINK_TEXT, "OpenID Connect").click()

time.sleep(5)

mail = page_to_scrape.find_element(By.ID, "i0116")
mail.send_keys("MAIL")
page_to_scrape.find_element(By.ID, "idSIButton9").click()
time.sleep(5)


password = page_to_scrape.find_element(By.ID, "i0118")
password.send_keys("PASSWORD")
page_to_scrape.find_element(By.ID, "idSIButton9").click()
time.sleep(5)

page_to_scrape.find_element(By.ID, "idBtn_Back").click()
time.sleep(5)

page_to_scrape.find_element(By.ID, "random673f8f2a516cf12_label_3_19").click()
time.sleep(5)

page_to_scrape.find_element(By.CLASS_NAME, "instancename").click()
time.sleep(5)

responseT = page_to_scrape.find_element(By.ID, "discussion-list-673f8fb631cf3673f8fb606ae088")



html = BeautifulSoup(responseT.text, 'html.parser')


novosti_markdown = newText.text

with open("novosti.md", "w") as novosti_file:
    novosti_file.write(novosti_markdown)