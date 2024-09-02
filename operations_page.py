# operations_page.py
from selenium.common import StaleElementReferenceException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# Replace with actual values
max_alert_amount = "20000"
max_claim_alert_amount = "5000"
email_to_add = ""  # Replace with the actual email


def perform_operations(driver):
    try:
        # Wait for the hamburger button to be visible and clickable using its class
        hamburger_button = WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//*[@type='button' and contains(@class, 'mud-button-root mud-icon-button "
                                        "mud-inherit-text hover:mud-inherit-hover mud-ripple mud-ripple-icon "
                                        "mud-icon-button-edge-start')]"))
        )
        hamburger_button.click()

        # Wait for the navigation pane to be visible after clicking the hamburger button
        WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "mud-drawer"))
        )

        # Select the "Customer Alert Settings" menu item
        customer_alert_settings = WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Claim Alerts')]"))
        )
        customer_alert_settings.click()

        # Select the "Create New" button
        create_new_button = WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Create New']"))
        )
        create_new_button.click()

        # Selecting the dropdown that contains a list of countries
        dropdown_option = WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@type='text' and contains(@class, 'mud-input-slot')]"))
        )
        dropdown_option.click()

        # Wait for the countries' list to be visible
        WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "mud-list"))
        )

        # Get all dropdown options
        options = WebDriverWait(driver, 50).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'mud-list-item')]"))
        )

        # Use explicit wait before interacting with each option to avoid stale element issues
        for option in options:
            WebDriverWait(driver, 10).until(EC.visibility_of(option))
            if option.text == "KENYA":  # Replace "KENYA" with the desired option
                option.click()
                break

        # Handle the autocomplete input field by focusing on the parent div first
        for attempt in range(3):  # Retry up to 3 times
            try:
                # Locate the parent div for the autocomplete field
                parent_div = WebDriverWait(driver, 50).until(
                    EC.visibility_of_element_located(
                        (By.XPATH,
                         "//div[contains(@class, 'mud-input mud-input-outlined mud-input-adorned-end "
                         "mud-select-input')]")
                    )
                )

                # Then locate the specific input within that div
                autocomplete_input = parent_div.find_element(By.XPATH, "//input[@type='text']")
                autocomplete_input.send_keys("TEST CUSTOMER 100")

                # Wait for the autocomplete suggestions to appear
                suggestions = WebDriverWait(driver, 50).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'mud-list-item-text')]"))
                )

                # Select the desired suggestion
                for suggestion in suggestions:
                    if "TEST CUSTOMER 100" in suggestion.text:  # Replace with the desired suggestion
                        suggestion.click()
                        break

                break  # Break the loop if no exception occurs

            except StaleElementReferenceException as e:
                print(f"Retrying due to stale element reference: {e}")
                time.sleep(1)  # Wait a bit before retrying

        # After selecting the customer, locate the Maximum Alert Amount field
        try:
            print("Attempting to locate the Maximum Alert Amount field...")

            # Locate the input field for Maximum Alert Amount by indexing it directly
            max_alert_amount_field = WebDriverWait(driver, 50).until(
                EC.visibility_of_element_located((By.XPATH,
                                                  "(//input[@class='mud-input-slot mud-input-root "
                                                  "mud-input-root-outlined' and @type='text'])[1]"))
            )

            # Scroll to the element to make sure it's in view
            driver.execute_script("arguments[0].scrollIntoView(true);", max_alert_amount_field)
            time.sleep(2)  # Give some time for the scrolling

            # Ensure the element is clickable before interaction
            max_alert_amount_field = WebDriverWait(driver, 50).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "(//input[@class='mud-input-slot mud-input-root mud-input-root-outlined' "
                                            "and @type='text'])[1]"))
            )

            # Clear the field before entering the amount
            max_alert_amount_field.clear()
            max_alert_amount_field.send_keys(max_alert_amount)
            print("Successfully entered the Maximum Alert Amount.")

            # Locate the input field for Maximum Claim Amount by indexing it directly
            max_claim_alert_field = WebDriverWait(driver, 50).until(
                EC.visibility_of_element_located((By.XPATH,
                                                  "(//input[@class='mud-input-slot mud-input-root "
                                                  "mud-input-root-outlined' and @type='text'])[2]"))
            )

            # Scroll to the element to make sure it's in view
            driver.execute_script("arguments[0].scrollIntoView(true);", max_claim_alert_field)
            time.sleep(2)  # Give some time for the scrolling

            # Ensure the element is clickable before interaction
            max_claim_alert_field = WebDriverWait(driver, 50).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "(//input[@class='mud-input-slot mud-input-root mud-input-root-outlined' "
                                            "and @type='text'])[2]"))
            )

            # Clear the field before entering the amount
            max_claim_alert_field.clear()
            max_claim_alert_field.send_keys(max_claim_alert_amount)
            print("Successfully entered the Maximum Claim Amount.")

            # Locate the Enter Email field
            email_field = WebDriverWait(driver, 50).until(
                EC.visibility_of_element_located((By.XPATH,
                                                  "(//input[@class='mud-input-slot mud-input-root "
                                                  "mud-input-root-outlined' and @type='text'])[3]"))
            )

            email_field.send_keys(email_to_add)

            # Locate and click the Add button
            add_button = WebDriverWait(driver, 50).until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add Email']"))
            )
            add_button.click()
            print("Successfully added the email.")

            # Wait for 2 seconds before submitting the form
            time.sleep(2)

            # Locate and click the Submit button
            submit_button = WebDriverWait(driver, 50).until(
                EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Submit Form']"))
            )
            submit_button.click()
            print("Successfully clicked the Submit button.")

        except (TimeoutException, ElementNotInteractableException) as e:
            print(f"Failed to locate or interact with fields or buttons: {e}")

    except Exception as e:
        print(f"An error occurred during operations: {e}")
