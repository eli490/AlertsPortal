# main_script.py
from login_page import login_to_application
from operations_page import perform_operations

if __name__ == "__main__":
    try:
        driver = login_to_application()  # Call login and get the driver object
        perform_operations(driver)       # Pass the driver object to perform operations
    except Exception as e:
        print(f"An error occurred: {e}")
