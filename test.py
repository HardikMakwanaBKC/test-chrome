from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from flask import Flask
import os
import platform

def get_chrome_user_data_path():
    """
    Gets the path to the last used Chrome profile.

    Returns:
        str: Path to the Chrome user data directory.
    """
    os_name = platform.system()
    if os_name == 'Windows':
        user_data_dir = os.path.join(os.getenv('LOCALAPPDATA'), 'Google', 'Chrome', 'User Data')
    elif os_name == 'Darwin':  # macOS
        user_data_dir = os.path.join(os.path.expanduser('~'), 'Library', 'Application Support', 'Google', 'Chrome')
    elif os_name == 'Linux':
        user_data_dir = os.path.join(os.path.expanduser('~'), '.config', 'google-chrome')
    else:
        raise ValueError(f"Unsupported operating system: {os_name}")

    # Find the most recently used profile (this might require more robust logic)
    profiles = os.listdir(user_data_dir)
    if profiles:
        # Assuming the most recently used profile is the last one in the list (may not always be accurate)
        last_profile = profiles[-1]
        return os.path.join(user_data_dir, last_profile)
    else:
        return user_data_dir  # Use the default profile directory

app = Flask(__name__)

@app.route('/')
def open_chrome():
    try:
        user_data_dir = get_chrome_user_data_path()

        options = Options()
        options.add_argument(f"--user-data-dir={user_data_dir}") 
        # options.add_argument("--no-sandbox")  # Uncomment if running in a container

        driver = webdriver.Chrome(options=options)
        driver.get("https://www.google.com") 
        driver.quit()

        return "Chrome opened and closed successfully."

    except Exception as e:
        return f"Error opening Chrome: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)