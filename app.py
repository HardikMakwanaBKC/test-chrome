from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

app = Flask(__name__)

@app.route('/')
def index():
    # Set up Chrome options
    options = Options()
    options.headless = False  # This will ensure the browser opens normally
    options.add_argument("--start-maximized")  # Start Chrome maximized
    
    # Provide the path to ChromeDriver
    chrome_driver_path = './chromedriver'  # Modify with your actual path if needed
    
    # Set up the Chrome WebDriver
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    
    # Open a website
    driver.get("https://www.example.com")
    
    # Wait for the page to load and then capture the title
    time.sleep(3)  # Sleep for 3 seconds to allow the page to load
    page_title = driver.title
    
    # Close the browser
    driver.quit()

    return f"Page Title: {page_title}"

if __name__ == '__main__':
    app.run(debug=True)
