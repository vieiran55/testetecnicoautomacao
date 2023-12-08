from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

def main():
    webdriver_path = r'C:\Users\antonio.leoncio\Downloads\chromedriver_win32\chromedriver.exe'


    service = ChromeService(executable_path=webdriver_path)
    driver = webdriver.Chrome(service=service)

    try:

        driver.get('https://www.saucedemo.com')

        driver.implicitly_wait(5)
   
        with open('informacoes_login.csv', 'r') as file:
          reader = csv.DictReader(file)
          for row in reader:
            username = row['username']
            password = row['password']
        
        time.sleep(2)
        username_input = driver.find_element(By.ID, "user-name")
        username_input.send_keys(username)
        
        time.sleep(2)
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys(password)
        
        time.sleep(2)
        login_input = driver.find_element(By.ID, "login-button")
        login_input.click()

        input("Pressione Enter para fechar o navegador...")

    finally:

        driver.quit()

if __name__ == "__main__":
    main()
