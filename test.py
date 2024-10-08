from selenium import webdriver as dr
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wt
from selenium.webdriver.support import expected_conditions as EC
from chromedriver_py import binary_path as bin

svc = dr.ChromeService(executable_path=bin)
wd = dr.Chrome(service=svc)

# Replace with your desired URL
url = "https://www.google.com/"

# Navigate to the URL
wd.get(url)

# Find the search bar element using its name attr
search_bar = wt(wd, 10).until(
    EC.visibility_of_element_located((By.NAME, "q"))
)

# Type "Selenium test" into the search bar
search_bar.send_keys("Selenium test")

# Find the search button using its name attribute
search_btn = wt(wd, 10).until(
    EC.element_to_be_clickable((By.NAME, "btnK"))
)

# Click the search button
search_btn.click()

# Optional: Wait for a specific element on the next page if needed
# For example, wait for the search results to load
# wt(wd, 10).until(EC.presence_of_element_located((By.ID, "search-results")))

# Print the page title
title = wd.title
print(f"Page title: {title}")

# Close the browser window
wd.quit()