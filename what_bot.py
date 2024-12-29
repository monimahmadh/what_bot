from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
user_data_dir = r"C:\Users\Workstation 2.0\AppData\Local\Google\Chrome\User Data\Profile 5"

# Set ChromeOptions to specify the user data directory
options = Options()
options.add_argument(f"user-data-dir={user_data_dir}")
# options.add_argument('--restore-last-session')

# Optional: specify a specific profile within the user data directory
options.add_argument("profile-directory=WhatsApp_Automate")  # WhatsApp_Automate

# Initialize the WebDriver with the specified options
try:
    driver = webdriver.Chrome(options=options)
except:
    print("Brewser already runnig..")
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
phone_numbers = ["+8801878119442", "+8801643872560", "+1975874690", "+8801935232394"]
message = "trying to automate WhatsApp using Python! \n This is a test message."


for number in phone_numbers:
    find_contact(number)
    send_message(message)
    time.sleep(5)

# close browser
# driver.quit()