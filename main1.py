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
chrome_options.binary_location = "/usr/bin/chromium-browser"  


browser_driver = Service('/usr/bin/chromedriver')


page_to_scrape = webdriver.Chrome(service=browser_driver, options=chrome_options)

try:
    
    page_to_scrape.get("https://cs.elfak.ni.ac.rs/nastava/")
    page_to_scrape.find_element(By.LINK_TEXT, "Log in").click()
    time.sleep(5)

    page_to_scrape.find_element(By.LINK_TEXT, "OpenID Connect").click()
    time.sleep(5)

    mail = page_to_scrape.find_element(By.ID, "i0116")
    mail.send_keys(os.environ['MAIL'])  
    page_to_scrape.find_element(By.ID, "idSIButton9").click()
    time.sleep(5)

    password = page_to_scrape.find_element(By.ID, "i0118")
    password.send_keys(os.environ['PASSWORD'])  
    page_to_scrape.find_element(By.ID, "idSIButton9").click()
    time.sleep(5)

    page_to_scrape.find_element(By.ID, "idBtn_Back").click()
    time.sleep(5)

    page_to_scrape.find_element(By.LINK_TEXT, "Baze").click()
    time.sleep(5)

    link_element = page_to_scrape.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/section/div/div/ul/li[1]/div[3]/ul/li[2]/div/div/div[2]/div/a/span")
    link_element.click()
    time.sleep(5)


    responseT = page_to_scrape.find_element(By.XPATH, '//*[@id="region-main"]')

   
    
    novosti_markdown = responseT.text  

    
    with open("novosti1.md", "w") as novosti1_file:
        novosti1_file.write(novosti_markdown)

finally:
    
    page_to_scrape.quit()
