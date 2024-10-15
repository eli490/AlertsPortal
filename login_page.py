# login_page.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Replace with actual login credentials
username = "TEST"
password = ""

# Specify the path to the ChromeDriver executable
chrome_driver_path = "C:/Users/elvin.opak/SeleniumProject/Driver/chromedriver.exe"
service_obj = Service(chrome_driver_path)


def login_to_application():
    # Initialize the Chrome WebDriver with the specified Service
    driver = webdriver.Chrome(service=service_obj)

    try:
        # Open the web application
        driver.get("")

        # Maximize the browser window
        driver.maximize_window()

        # Wait for the username field to be present and visible
        username_field = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='text']"))
        )
        password_field = driver.find_element(By.XPATH, "//input[@type='password']")

        # Enter credentials
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Wait for the login button to be clickable and then click it
        login_button = WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))
        )
        login_button.click()

        # Wait for the welcome message to appear
        WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located(
                (By.XPATH,
                 "//*[contains(text(), 'Welcome to the Alerts Portal, Please proceed to the different pages')]")
            )
        )

        return driver  # Return the driver object after successful login

    except Exception as e:
        print(f"An error occurred during login: {e}")
        driver.quit()
        raise
