from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from time import sleep

# Lancer le navigateur et ouvrir la page
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Récupérer les éléments nécessaires : champ nom et boutons Alert et Confirm
name_field = driver.find_element(By.ID, "name")
alert_btn = driver.find_element(By.ID, "alertbtn")
confirm_btn = driver.find_element(By.ID, "confirmbtn")

# Test avec le champ rempli : bouton Alert
name_field.clear()
name_field.send_keys("Samar")
alert_btn.click()
sleep(1)
alert = Alert(driver)
actual_text = alert.text
expected_text = "Hello Samar, share this practice page and share your knowledge"
# Vérifier si le message correspond exactement à ce qui est attendu
if expected_text == actual_text:
    print("ALERT AVEC NOM : PASS")
else:
    print("ALERT AVEC NOM : FAIL")
    print("Attendu :", expected_text)
    print("Obtenu  :", actual_text)
alert.accept()
driver.save_screenshot("alert_avec_nom.png")

# Test avec le champ rempli : bouton Confirm
name_field.clear()
name_field.send_keys("Samar")
confirm_btn.click()
sleep(1)
alert = Alert(driver)
actual_text = alert.text
expected_text = "Hello Samar, Are you sure you want to confirm?"
# Vérifier si le message correspond exactement à ce qui est attendu
if expected_text == actual_text:
    print("CONFIRM AVEC NOM : PASS")
else:
    print("CONFIRM AVEC NOM : FAIL")
    print("Attendu :", expected_text)
    print("Obtenu  :", actual_text)
alert.accept()
driver.save_screenshot("confirm_avec_nom.png")

# Test avec le champ vide : bouton Alert
name_field.clear()
alert_btn.click()
sleep(1)
try:
    alert = Alert(driver)
    actual_text = alert.text
    # Vérifier si le site génère un message avec champ vide
    # Si le message contient "Hello ," alors c'est un bug car le champ devrait être obligatoire
    if "Hello ," in actual_text:
        print("ALERT CHAMP VIDE : BUG détecté")
        print("Texte obtenu :", actual_text)
    else:
        # Si aucune alerte ou message correct, le comportement est conforme
        print("ALERT CHAMP VIDE : comportement correct")
    alert.accept()
except:
    # Si aucune alerte n'apparaît, le comportement est correct
    print("ALERT CHAMP VIDE : aucune alerte affichée, comportement correct")
driver.save_screenshot("alert_champ_vide.png")

# Test avec le champ vide : bouton Confirm
name_field.clear()
confirm_btn.click()
sleep(1)
try:
    alert = Alert(driver)
    actual_text = alert.text
    # Vérifier si le site génère un message avec champ vide
    # Si le message contient "Hello ," alors c'est un bug car le champ devrait être obligatoire
    if "Hello ," in actual_text:
        print("CONFIRM CHAMP VIDE : BUG détecté")
        print("Texte obtenu :", actual_text)
    else:
        print("CONFIRM CHAMP VIDE : comportement correct")
    alert.accept()
except:
    # Si aucune alerte n'apparaît, le comportement est correct
    print("CONFIRM CHAMP VIDE : aucune alerte affichée, comportement correct")
driver.save_screenshot("confirm_champ_vide.png")

# Test du dropdown
ddropdown_element = driver.find_element(By.ID, "dropdown-class-example")
dropdown = Select(ddropdown_element)

# Sélection Option1
dropdown.deselect_all()
dropdown.select_by_visible_text("Option1")
sleep(1)
selected_option = dropdown.first_selected_option.text
# Vérifier si l'option sélectionnée correspond à l'attendu
if selected_option == "Option1":
    print("TC-R1 : PASS")
else:
    print("TC-R1 : FAIL")
    print("Attendu :", "Option1")
    print("Obtenu  :", selected_option)
driver.save_screenshot("dropdown_option1.png")

# Sélection Option2
dropdown.deselect_all()
dropdown.select_by_visible_text("Option2")
sleep(1)
selected_option = dropdown.first_selected_option.text
if selected_option == "Option2":
    print("TC-R2 : PASS")
else:
    print("TC-R2 : FAIL")
    print("Attendu :", "Option2")
    print("Obtenu  :", selected_option)
driver.save_screenshot("dropdown_option2.png")

# Sélection Option3
dropdown.deselect_all()
dropdown.select_by_visible_text("Option3")
sleep(1)
selected_option = dropdown.first_selected_option.text
if selected_option == "Option3":
    print("TC-R3 : PASS")
else:
    print("TC-R3 : FAIL")
    print("Attendu :", "Option3")
    print("Obtenu  :", selected_option)
driver.save_screenshot("dropdown_option3.png")

# Fermer le navigateur à la fin des tests
driver.quit()
