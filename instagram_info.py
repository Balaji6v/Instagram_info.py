from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


def login_instagram(driver, username, password):
    driver.get("https://www.instagram.com/accounts/login/")
    wait = WebDriverWait(driver, 15)

    # Wait for username field and enter login
    username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password_field = driver.find_element(By.NAME, "password")
    username_field.send_keys(username)
    password_field.send_keys(password + Keys.RETURN)

    # Wait for login to complete
    time.sleep(5)


def get_follow_info(driver):
    driver.get("https://www.instagram.com/guviofficial/")
    wait = WebDriverWait(driver, 15)

    # Wait for the followers/following elements to appear
    follow_elements = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, "//header//ul/li//span/span"))
    )

    if len(follow_elements) >= 2:
        followers = follow_elements[0].get_attribute("innerText")
        following = follow_elements[1].get_attribute("innerText")
        print("Followers:", followers)
        print("Following:", following)
    else:
        print("Could not locate follower/following counts.")


def main():
    username = "quiet_balaji"
    password = "balaji@13"

    # Initialize Chrome browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        login_instagram(driver, username, password)
        get_follow_info(driver)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()






