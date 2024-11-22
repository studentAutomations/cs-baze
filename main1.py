from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

# Set up Chrome options for headless operation
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.binary_location = "/usr/bin/chromium-browser"  # Set the path to the Chromium binary

# Path to the ChromeDriver executable
browser_driver = Service('/usr/bin/chromedriver')

# Initialize the WebDriver with options
page_to_scrape = webdriver.Chrome(service=browser_driver, options=chrome_options)

try:
    # Navigate to the page and perform login actions
    page_to_scrape.get("https://cs.elfak.ni.ac.rs/nastava/")
    page_to_scrape.find_element(By.LINK_TEXT, "Log in").click()
    time.sleep(5)

    page_to_scrape.find_element(By.LINK_TEXT, "OpenID Connect").click()
    time.sleep(5)

    mail = page_to_scrape.find_element(By.ID, "i0116")
    mail.send_keys(os.environ['MAIL'])  # Use environment variable for email
    page_to_scrape.find_element(By.ID, "idSIButton9").click()
    time.sleep(5)

    password = page_to_scrape.find_element(By.ID, "i0118")
    password.send_keys(os.environ['PASSWORD'])  # Use environment variable for password
    page_to_scrape.find_element(By.ID, "idSIButton9").click()
    time.sleep(5)

    page_to_scrape.find_element(By.ID, "idBtn_Back").click()
    time.sleep(5)

    page_to_scrape.find_element(By.LINK_TEXT, "Baze").click()
    time.sleep(5)

    link_element = page_to_scrape.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/section/div/div/ul/li[1]/div[3]/ul/li[2]/div/div/div[2]/div/a/span")
    link_element.click()
    time.sleep(5)


    responseT = page_to_scrape.find_element(By.XPATH, "//*[@id="region-main"]")

   
    
    novosti_markdown = responseT.text  # Extract text or format as needed

    # Write output to a markdown file
    with open("novosti1.md", "w") as novosti_file:
        novosti_file.write(novosti_markdown)

finally:
    # Clean up by quitting the driver
    page_to_scrape.quit()
