from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#necessery for web driver setup on my device
driver_path = '../web_drivers/chromedriver'
options = webdriver.ChromeOptions()
options.binary_location = '../../Applications/Google Chrome.app'
options.add_argument(f'--chromedriver={driver_path}')
driver = webdriver.Chrome(options=options)

try:
    # Open Facebook login page
    driver.get("https://www.facebook.com/")
    
    # Find the username and password fields and enter your credentials
    username_field = driver.find_element("id", "email")
    password_field = driver.find_element("id", "pass")

    username_field.send_keys("suryanashwin4u@gmail.com")
    password_field.send_keys("ASH07win!")

    # Submit the login form
    password_field.send_keys(Keys.RETURN)

    # Wait for the login to complete
    time.sleep(5)

    # You can add further automation steps here, for example, navigating to another page

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser window
    driver.quit()