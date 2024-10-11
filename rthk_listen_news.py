from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Set up the WebDriver (make sure to specify the correct path to your chromedriver)
service = Service(executable_path='./chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL of the RTHK hourly news page
url = "https://news.rthk.hk/rthk/ch/news-bulletins.htm"

try:
    # Open the URL
    driver.get(url)
    
    # Wait for the page to load and the play button to be clickable
    play_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='listenbuttondiv'] a[class='listenbutton']"))
    )
    
    # Click the play button
    play_button.click()
    
    # Wait for a few seconds to let the news play (you can adjust the sleep time as needed)
    time.sleep(30)

finally:
    # Close the browser
    driver.quit()