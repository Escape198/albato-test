from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import zipfile
import time
import os
import auth


filename = "zip.zip"


try:
    browser = webdriver.Chrome()
    browser.get('https://mail.yandex.ru/')
    browser.maximize_window()
    browser.implicitly_wait(10)

    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="index-page-container"]/div/div[2]/div/div/div[4]/a[2]'))).click()
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, "passp-field-login"))).send_keys(auth.email)
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "passp:sign-in"))).click()
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.ID, 'passp-field-passwd'))).send_keys(auth.password)
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, 'passp:sign-in'))).click()
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="js-apps-container"]/div[2]/div[7]/div/div[3]/div[2]/div[1]/div/div/div/a/span'))).click()

    textbox = WebDriverWait(browser, 7).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                        "#cke_1_contents > div"))).send_keys('OK')

    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME,
                                        'composeYabbles'))).send_keys('recursion198@gmail.com')

    file = browser.find_element(
        By.XPATH, '/html/body/div[2]/div[2]/div[10]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/div[5]/span/span/div/input')

    zip_obj = zipfile.ZipFile(filename, "w")
    zip_obj.write("new.py")
    zip_obj.write("mod.py")
    zip_obj.write("first_test.py")
    zip_obj.close()

    _dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(_dir, 'zip.zip')
    file.send_keys(file_path)

    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div[10]/div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/button'))).click()


finally:
    time.sleep(15)
    # quit
