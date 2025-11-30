from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from time import sleep

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")


name_field = driver.find_element(By.ID, "name")
alert_btn = driver.find_element(By.ID, "alertbtn")
confirm_btn = driver.find_element(By.ID, "confirmbtn")

name_field.clear()
name_field.send_keys("Samar")
alert_btn.click()
sleep(1)
alert = Alert(driver)
actual_text = alert.text
expected_text = "Hello Samar, share this practice page and share your knowledge"
if expected_text == actual_text:
    print("ALERT AVEC NOM : PASS")
else:
    print("ALERT AVEC NOM : FAIL")
    print("Attendu :", expected_text)
    print("Obtenu  :", actual_text)
alert.accept()
driver.save_screenshot("alert_avec_nom.png")

name_field.clear()
name_field.send_keys("Samar")
confirm_btn.click()
sleep(1)
alert = Alert(driver)
actual_text = alert.text
expected_text = "Hello Samar, Are you sure you want to confirm?"
if expected_text == actual_text:
    print("CONFIRM AVEC NOM : PASS")
else:
    print("CONFIRM AVEC NOM : FAIL")
    print("Attendu :", expected_text)
    print("Obtenu  :", actual_text)
alert.accept()
driver.save_screenshot("confirm_avec_nom.png")

name_field.clear()
alert_btn.click()
sleep(1)
alert = Alert(driver)
actual_text = alert.text
expected_text = "Le champ est vide, veuillez saisir un nom"
if expected_text == actual_text:
    print("ALERT CHAMP VIDE : PASS")
else:
    print("ALERT CHAMP VIDE : FAIL")
    print("Attendu :", expected_text)
    print("Obtenu  :", actual_text)
alert.accept()
driver.save_screenshot("alert_champ_vide.png")

name_field.clear()
confirm_btn.click()
sleep(1)
alert = Alert(driver)
actual_text = alert.text
expected_text = "Le champ est vide, veuillez saisir un nom"
if expected_text == actual_text:
    print("CONFIRM CHAMP VIDE : PASS")
else:
    print("CONFIRM CHAMP VIDE : FAIL")
    print("Attendu :", expected_text)
    print("Obtenu  :", actual_text)
alert.accept()
driver.save_screenshot("confirm_champ_vide.png")

driver.quit()
