from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

app = Flask(__name__)

# Remote WebDriver URL (replace with your server's IP if hosting remotely)
REMOTE_WEBDRIVER_URL = "http://localhost:4444/wd/hub"

@app.route('/open_browser', methods=['POST'])
def open_browser():
    try:
        # Parse user input from the request
        data = request.json
        url = data.get('url', 'https://www.google.com')  # Default to Google

        # Set up Remote WebDriver with Chrome capabilities
        options = webdriver.ChromeOptions()
        capabilities = DesiredCapabilities.CHROME
        driver = webdriver.Remote(
            command_executor=REMOTE_WEBDRIVER_URL,
            desired_capabilities=capabilities,
            options=options
        )

        # Perform automation task
        driver.get(url)
        title = driver.title
        driver.quit()

        # Return response
        return jsonify({'status': 'success', 'title': title})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
