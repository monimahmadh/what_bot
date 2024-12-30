import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import USER_DATA_DIR, PROFILE_DIRECTORY

from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Set ChromeOptions to specify the user data directory
options = Options()
options.add_argument(f"user-data-dir={USER_DATA_DIR}")
options.add_argument(f"profile-directory={PROFILE_DIRECTORY}")
# options.add_argument('--restore-last-session')

# Initialize the WebDriver with the specified options
try:
    driver = webdriver.Chrome(options=options)
except Exception as e:
    print(f"Error initializing WebDriver: {e}")

driver.get("https://web.whatsapp.com")
time.sleep(10)  # Wait for QR scan (for the first time)


def find_contact(phone_number):
    new_chat_btn = driver.find_element(By.XPATH, "//div[@role='button' and @aria-label='New chat']")
    new_chat_btn.click()
    time.sleep(2)
    driver.switch_to.active_element.send_keys(phone_number)
    time.sleep(2)
    driver.switch_to.active_element.send_keys(Keys.RETURN)


def send_message(message):
    driver.switch_to.active_element.send_keys(message)
    time.sleep(2)
    driver.switch_to.active_element.send_keys(Keys.RETURN)


def main():
    try:
            
        phone_numbers = os.getenv("PHONE_NUMBERS").split(',')
        message = "Trying to automate WhatsApp using Python! \n This is a test message."
        
        for number in phone_numbers:
            find_contact(number)
            send_message(message)
            time.sleep(5)

    except Exception as e:
        print(f"Error: {e}")
        driver.quit()

if __name__ == "__main__":
    main()

