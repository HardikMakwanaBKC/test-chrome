from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from flask import Flask
import os, time

def get_chrome_user_data_path():
    try:
        app_data_path = os.getenv('LOCALAPPDATA')
        chrome_user_data_path = os.path.join(app_data_path, 'Google', 'Chrome', 'User Data')
        return chrome_user_data_path
    except Exception as e:
        print(f"Error occurred while getting Chrome user data path: {e}")
        return None
    
def setup_chrome_driver():
    """
    Setup and return a Chrome WebDriver instance.

    Returns:
        WebDriver: An instance of Chrome WebDriver.
    """
    # Create an instance of ChromeOptions
    options = Options()

    # Get the last chrome profile data path that was opened
    strChromeUserDataPath = get_chrome_user_data_path()

    # If the user data path is valid, add the argument to the options
    if strChromeUserDataPath:
        options.add_argument(f"user-data-dir={strChromeUserDataPath}")  # Path to the user data directory

    # Add the argument to maximize the window at startup
    options.add_argument("--start-maximized")  # Maximize the window at startup
    options.add_experimental_option("detach", True)

    # Return the Chrome WebDriver instance
    return webdriver.Chrome(options=options)

app = Flask(__name__)

@app.route('/')
def open_chrome():
    
    driver = setup_chrome_driver()

    # Open a website to test
    driver.get('https://www.google.com')

    time.sleep(10)
    # Close the browser
    driver.quit()

    return "Chrome opened and closed successfully."

if __name__ == '__main__':
    app.run(debug=True)