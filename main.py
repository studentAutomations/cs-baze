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
chrome_options.binary_location = "/usr/bin/google-chrome"  

browser_driver = Service('/usr/bin/chromedriver') 

page_to_scrape = webdriver.Chrome(service=browser_driver, options=chrome_options)

try:
    wait = WebDriverWait(page_to_scrape, 5)  
    
    page_to_scrape.get("https://cs.elfak.ni.ac.rs/nastava/")
    
    log_in_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Log in")))
    log_in_link.click()

    
    openid_connect_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "OpenID Connect")))
    openid_connect_link.click()

    mail = wait.until(EC.presence_of_element_located((By.ID, "i0116")))
    mail.send_keys(os.environ['MAIL'])

    next_button = wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
    next_button.click()

    password = wait.until(EC.presence_of_element_located((By.ID, "i0118")))
    password.send_keys(os.environ['PASSWORD'])

    sign_in_button = wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
    sign_in_button.click()

    
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
