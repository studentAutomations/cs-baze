from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.binary_location = "/usr/bin/google-chrome"  # Adjusted for GitHub runner

browser_driver = Service('/usr/bin/chromedriver')  # Adjusted for GitHub runner

page_to_scrape = webdriver.Chrome(service=browser_driver, options=chrome_options)

try:
    wait = WebDriverWait(page_to_scrape, 10)  # Set an explicit wait timeout of 10 seconds
    
    page_to_scrape.get("https://cs.elfak.ni.ac.rs/nastava/")
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Log in"))).click()
    
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "OpenID Connect"))).click()
    
    mail = wait.until(EC.presence_of_element_located((By.ID, "i0116")))
    mail.send_keys(os.environ['MAIL'])  
    page_to_scrape.find_element(By.ID, "idSIButton9").click()
    
    password = wait.until(EC.presence_of_element_located((By.ID, "i0118")))
    password.send_keys(os.environ['PASSWORD'])  
    page_to_scrape.find_element(By.ID, "idSIButton9").click()
    
    wait.until(EC.element_to_be_clickable((By.ID, "idBtn_Back"))).click()
    
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Baze"))).click()
    
    link_element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/section/div/div/ul/li[1]/div[3]/ul/li[1]/div/div/div[2]/div/a")))
    link_element.click()
    
    responseT = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="region-main"]')))
    novosti_markdown = responseT.text  

    with open("novosti.md", "w") as novosti_file:
        novosti_file.write(novosti_markdown)

finally:
    page_to_scrape.quit()
