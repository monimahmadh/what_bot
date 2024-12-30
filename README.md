# WhatsApp Automation Bot

This project automates sending WhatsApp messages using Python, Selenium, and ChromeDriver. It supports dynamically loading contacts and messages, making it flexible for personal or small-scale automation purposes.

## Features
- **Automated Messaging**: Send messages to individual contacts via WhatsApp Web.
- **Chrome User Data Persistence**: Maintain session data to avoid re-scanning the QR code.
- **Customizable Messages**: Easily configure messages directly in the script.

---

## Installation and Setup

### Prerequisites
1. **Python**: Ensure Python 3.x is installed. Download it from [python.org](https://www.python.org/).
2. **Google Chrome**: Install the latest version of Google Chrome.
3. **ChromeDriver**: ChromeDriver will be automatically installed using `webdriver_manager`.

### Installation
1. Clone the repository:
   ```bash
   https://github.com/monimahmadh/what_bot.git
   cd whatsapp-automation-bot
   ```
2. Install required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory to store phone numbers:
   ```plaintext
   PHONE_NUMBERS=+8801878119442,+880164*****,+19758*****
   ```

4. Create a `config.py` file to store your Chrome user data settings. It will allow you to avoid re-scanning the QR code:
   ```python
   USER_DATA_DIR = r"C:\Users\YourUsername\AppData\Local\Google\Chrome\User Data"
   PROFILE_DIRECTORY = "Profile 1"
   ```

---

## Usage

1. Open the terminal and navigate to the project directory.
2. Run the script:
   ```bash
   python what_bot.py
   ```
3. On the first run, you will need to scan the QR code on WhatsApp Web to log in.
4. The script will:
   - Load the phone numbers from the `.env` file.
   - Send the specified message to each contact.

---

## File Structure
```plaintext
whatsapp-automation-bot/
│
├── what_bot.py         # Main script
├── config.py           # Configuration file for Chrome user data
├── .env                # Environment file for phone numbers
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
```

---

## Dependencies
The following libraries are used in this project:
- [selenium](https://pypi.org/project/selenium/): For browser automation.
- [webdriver_manager](https://pypi.org/project/webdriver-manager/): Automatically manages ChromeDriver.
- [python-dotenv](https://pypi.org/project/python-dotenv/): Load environment variables from a `.env` file.

Install dependencies using:
```bash
pip install -r requirements.txt
```

---

## Troubleshooting
1. **Error initializing WebDriver**: Ensure `Google Chrome` and `ChromeDriver` versions are compatible.
2. **QR Code not appearing**: Check the `USER_DATA_DIR` and `PROFILE_DIRECTORY` paths in `config.py`.
3. **No messages sent**: Verify the phone numbers in `.env` are in the correct format (e.g., `+8801234567890`).

---

## Contributing
Feel free to fork this repository and submit pull requests to improve functionality or add new features.

---

## License
This project is open-source and available under the [MIT License](LICENSE).

