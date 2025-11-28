from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# =========================
# FONCTIONNALITÉ : RADIO BUTTONS
# URL : https://rahulshettyacademy.com/AutomationPractice/
# =========================

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
wait = WebDriverWait(driver, 10)

# Localisation des boutons radio
radio1 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="radio-btn-example"]/fieldset/label[1]/input')))
radio2 = driver.find_element(By.XPATH, '//*[@id="radio-btn-example"]/fieldset/label[2]/input')
radio3 = driver.find_element(By.XPATH, '//*[@id="radio-btn-example"]/fieldset/label[3]/input')

# TC-01 : sélectionner radio1
radio1.click()
print("TC-01 :", "OK" if radio1.is_selected() else "FAIL")

# TC-02 : sélectionner radio2
radio2.click()
print("TC-02 :", "OK" if radio2.is_selected() and not radio1.is_selected() else "FAIL")

# TC-03 : sélectionner radio3
radio3.click()
print("TC-03 :", "OK" if radio3.is_selected() else "FAIL")

# Screenshot final
driver.save_screenshot("radiobuttons_functionality.png")

driver.quit()

# =========================
# FONCTIONNALITÉ : BOUTON PRACTICE
# URL : https://rahulshettyacademy.com/
# =========================

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)  # timeout un peu plus long pour le Practice

driver.get("https://rahulshettyacademy.com/")

# TC-R1 : Vérifier la présence du lien Practice
try:
    practice_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Practice")))
    print("TC-R1 (Practice) : OK")
except (TimeoutException, NoSuchElementException):
    print("TC-R1 (Practice) : FAIL")

# TC-R2 : Cliquer et vérifier redirection
practice_btn.click()
try:
    wait.until(lambda d: "automationpractice" in d.current_url.lower())
    print("TC-R2 (Practice) : OK")
except TimeoutException:
    print("TC-R2 (Practice) : FAIL")

# TC-R3 : Vérifier URL exacte
expected_url = "https://rahulshettyacademy.com/automationpractice/"
print("TC-R3 (Practice) :", "OK" if expected_url.lower() == driver.current_url.lower() else "FAIL")

# TC-R4 : Cliquer plusieurs fois (force FAIL print)
multi_ok = True
for i in range(3):
    try:
        btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Practice")))
        btn.click()
        wait.until(lambda d: "automationpractice" in d.current_url.lower())
    except:
        multi_ok = False
print("TC-R4 (Practice) : FAIL")
# Screenshot final
driver.save_screenshot("practice_functionality.png")

driver.quit()
