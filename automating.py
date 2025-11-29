from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# SETUP SINGLE BROWSER

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# Fonctionnalité 1 : Signup Button test

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

sign_up_btn = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//button[text()='Signup']"))
)
print("TC-S1 (Signup) :", "OK" if sign_up_btn.is_displayed() else "FAIL")

clickable_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Signup']"))
)
print("TC-S2 (Signup) :", "OK" if clickable_btn.is_enabled() else "FAIL")

# TC-S3 : Cliquer sur le bouton et vérifier redirection

clickable_btn.click()
time.sleep(1)

print(
    "TC-S3 (Signup Redirect) :",
    "OK" if "signup" in driver.current_url.lower()
    else f"FAIL (URL actuelle : {driver.current_url})"
)
driver.save_screenshot("signup_button_test.png")

# Fonctionnalité 2 : Suggestion Class Example

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(1)

input_field = wait.until(EC.visibility_of_element_located((By.ID, "autocomplete")))

# TC-S1 : Vérifier la visibilité du champ

print("TC-S1 (Visibilité) :", "OK" if input_field.is_displayed() else "FAIL")

# TC-S2 : Vérifier saisie + suggestions

input_field.clear()
input_field.send_keys("Ind")
time.sleep(1)

suggestions = driver.find_elements(By.CSS_SELECTOR, ".ui-menu-item div")
print("TC-S2 (Suggestions) :", "OK" if len(suggestions) > 0 else "FAIL")

# TC-S3 : Sélection avec la souris (India)

input_field.clear()
input_field.send_keys("Ind")
time.sleep(1)

# Refetch suggestions to avoid stale element issues

suggestions = driver.find_elements(By.CSS_SELECTOR, ".ui-menu-item div")
for item in suggestions:
    if item.text == "India":
        item.click()
        break

print("TC-S3 (Sélection souris) :","OK" if input_field.get_attribute("value") == "India" else "FAIL")

# TC-S4 : Sélection au clavier (Aus → Australia)

input_field.clear()
input_field.send_keys("Aus")
time.sleep(1)
input_field.send_keys("\ue015")
input_field.send_keys("\ue007")
time.sleep(1)
print("TC-S4 (Sélection clavier) :","OK" if input_field.get_attribute("value").lower().startswith("aus") else "FAIL")

# TC-S5 : Vérifier saisie non correspondante
input_field.clear()
input_field.send_keys("Xyzabc")
time.sleep(1)
no_suggestion = len(driver.find_elements(By.CSS_SELECTOR, ".ui-menu-item div")) == 0
print("TC-S5 (Aucune correspondance) :", "OK" if no_suggestion else "FAIL")
# the end and  screenshot
driver.save_screenshot("suggestion_class_test.png")
driver.quit()
