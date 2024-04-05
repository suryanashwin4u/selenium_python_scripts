from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#necessery for web driver setup on my device
driver_path = '../web_drivers/chromedriver'
options = webdriver.ChromeOptions()
options.binary_location = '../../Applications/Google Chrome.app'
options.add_argument(f'--chromedriver={driver_path}')
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://www.naukri.com/")
    driver.maximize_window()
    
    #loop for all gmail logins
    for i in range(3):
        # Find the username and password fields and enter your credentials
        driver.find_element("id","login_Layer").click()
        time.sleep(2)
        
        driver.find_element(By.XPATH,"//*[@id='root']/div[4]/div[2]/div/div/div[2]/div/div[3]").click()
        time.sleep(3)
        
        # automation script
        driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[4]/div").click()
        time.sleep(3)
        
        driver.find_elements(By.LINK_TEXT, "View all")[1].click()
        time.sleep(10)
        
        driver.find_element(By.XPATH, "//*[@id='root']/div[3]/div[2]/div[4]").click()
        time.sleep(3)
        
        driver.find_element(By.XPATH, "//*[@id='root']/div[3]/div[2]/div[4]/div[2]/div[2]/div/div[3]/div/div[1]/div[4]").click()
        time.sleep(3)
        
    list_emails = ['suryanashwin4u.mca@outlook.com','suryanashwin4u@yahoo.com']
    
    #loop for all list login
    for email_id in list_emails:
        
        driver.find_element("id","login_Layer").click()
        time.sleep(2)
    
        driver.find_element(By.XPATH, "//*[@id='root']/div[4]/div[2]/div/div/div[2]/div/form/div[2]/input").send_keys(email_id)
        driver.find_element(By.XPATH, "//*[@id='root']/div[4]/div[2]/div/div/div[2]/div/form/div[3]/input").send_keys("ASH07win!")
        driver.find_element(By.XPATH, "//*[@id='root']/div[4]/div[2]/div/div/div[2]/div/form/div[6]/button").click()

        time.sleep(3)
        
        driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[4]/div").click()
        time.sleep(3)
        
        driver.find_elements(By.LINK_TEXT, "View all")[1].click()
        time.sleep(10)
        
        driver.find_element(By.XPATH, "//*[@id='root']/div[3]/div[2]/div[4]").click()
        time.sleep(3)
        
        driver.find_element(By.XPATH, "//*[@id='root']/div[3]/div[2]/div[4]/div[2]/div[2]/div/div[3]/div/div[1]/div[4]").click()
        time.sleep(3)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()