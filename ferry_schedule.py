from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Set up the WebDriver (make sure to specify the correct path to your chromedriver)
service = Service(executable_path='./chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

# Get the current date and time
now = datetime.now()

# Format the date as "YYYY-MM-DD"
formatted_date = now.strftime("%Y-%m-%d")

# URL of the Sun Ferry schedule page
url = "https://www.sunferry.com.hk/en/route-and-fare?origin=CE&destination=MW&departure_date=" + formatted_date + "&departure_time=04%3A17&vessel_type=any"

try:
    # Open the URL
    driver.get(url)
    
    # Wait for the schedule table to load
    time.sleep(10)  # Increase the sleep time to give the page more time to load
    
    # Locate the schedule table (assuming it is in a table element)
    schedule_table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "table[id='schedule-table']"))
    )
    
    # Locate the rows of the schedule table
    schedule_rows = schedule_table.find_elements(By.TAG_NAME, "tr")
    
    # Print the schedule information
    for row in schedule_rows:
        columns = row.find_elements(By.TAG_NAME, "td")
        if columns:
            print([column.text for column in columns])

except TimeoutException:
    print("Schedule table not found within the timeout period.")

finally:
    # Close the browser
    driver.quit()