from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver service
service = Service('./chromedriver')  # Update the path to your WebDriver

# Initialize the WebDriver
driver = webdriver.Chrome(service=service)

# Open the YouTube website
driver.get("https://www.youtube.com/")

# Wait for the page to load
time.sleep(2)

# Find the search box and enter the search query
search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("Nepal Hiking Trails")

# Submit the search query
search_box.send_keys(Keys.RETURN)

# Wait for the search results to load
time.sleep(3)

# Optionally, you can print the titles of the search results
try:
    results = driver.find_elements(By.CSS_SELECTOR, "#video-title")
    for result in results:
        print(result.text)
except Exception as e:
    print(f"An error occurred: {e}")

# Click on the second video in the search results
try:
    second_video = results[1]  # The second video is at index 1
    second_video.click()
except Exception as e:
    print(f"An error occurred while clicking the second video: {e}")

# Wait for the video to load
time.sleep(5)

# Play the video for 10 seconds
time.sleep(10)

# Close the browser
driver.quit()