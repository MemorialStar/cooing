from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

def getQuery(query_raw):
    return query_raw.replace(' ', '%20')

def getVideofrom(url):
    # Specify the path to msedgedriver.exe
    edge_driver_path = "explorerdriver_linux/msedgedriver"  # Path to the Linux msedgedriver binary
    
    # Set up the Edge WebDriver
    service = Service(edge_driver_path)
    options = webdriver.EdgeOptions()
    options.add_argument('--headless')  # If you want to run Edge without opening the window
    options.add_argument('--disable-gpu')
    
    # Create the Edge WebDriver instance
    driver = webdriver.Edge(service=service, options=options)
    
    # Open the URL in the Edge browser
    driver.get(url)
    
    # Wait for a few seconds to ensure the page and all JavaScript files are fully loaded
    time.sleep(3)
    
    # Get the final HTML after JavaScript execution
    final_html = driver.page_source
    
    # # Save the final HTML to 'index.html'
    # with open('index.html', 'w', encoding='utf-8') as file:
    #     file.write(final_html)
    
    # Now find the div with id 'player_container'
    try:
        player_container = driver.find_element(By.ID, "player_container")
        iframe = player_container.find_element(By.TAG_NAME, "iframe")
        video_src = iframe.get_attribute('src')
        driver.quit()
        return video_src if video_src else "Video iframe not found or no source available."
    except:
        driver.quit()
        return "Player container not found."

# Example usage
query_raw = "hello world"
query = getQuery(query_raw)  # hello%20world
video_src = getVideofrom(url=f"https://youglish.com/pronounce/{query}/english")
print(video_src)
