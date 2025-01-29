from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from flask import Flask
import time
import tempfile

def setup_default_browser_driver():
    """
    Setup and return a WebDriver instance for the default browser.

    Returns:
        WebDriver: An instance of WebDriver for the default browser.
    """
    # Create a temporary directory for user data
    user_data_dir = tempfile.mkdtemp()

    options = webdriver.ChromeOptions()
    options.add_argument(f'--user-data-dir={user_data_dir}')

    # # Use headless mode for server environments (optional)
    # options.add_argument("--headless")  # Comment this line if you want to see the browser

    # Add argument to start maximized
    options.add_argument("--start-maximized")

    # Return the WebDriver instance (defaults to Chrome if no browser specified)
    return webdriver.Chrome(options=options)

app = Flask(__name__)

@app.route('/')
def open_browser():
    # Setup the WebDriver
    driver = setup_default_browser_driver()

    # Open a website to test
    driver.get('https://www.google.com')

    # Wait for a few seconds (for demonstration purposes)
    time.sleep(10)

    # Close the browser
    driver.quit()

    return "Default browser opened and closed successfully."

if __name__ == '__main__':
    app.run(debug=True)
