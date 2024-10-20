from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

# Specify the path to msedgedriver (use the correct binary for Linux)
edge_driver_path = "explorerdriver_linux/msedgedriver"  # Path to the Linux msedgedriver binary

# Set up the Edge WebDriver
service = Service(edge_driver_path)
options = webdriver.EdgeOptions()
options.add_argument('--headless')  # Optional: Run Edge in headless mode
options.add_argument('--disable-gpu')

# Create the Edge WebDriver instance
driver = webdriver.Edge(service=service, options=options)

# Open a test URL
driver.get("https://www.google.com")

# Print the title of the page to verify the script is working
print(driver.title)

# Close the browser
driver.quit()
