from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Set up the WebDriver (make sure to specify the correct path to your chromedriver)
service = Service(executable_path='./chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL of the HKSAR Government Press Releases page
url = "https://www.news.gov.hk/chi/index.html"

try:
    # Open the URL
    driver.get(url)
    
    # Wait for the page to load (you can adjust the sleep time as needed)
    time.sleep(5)
    
    # Locate the headlines (assuming they are in <a> tags within a <div> or <li>)
    headlines = driver.find_elements(By.CSS_SELECTOR, "div[id='mainTicker'] a")
    
    # Print the headlines
    for headline in headlines:
        print(headline.text)

finally:
    # Close the browser
    driver.quit()