from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

# Initialize Chrome driver
driver = webdriver.Chrome()  # Make sure chromedriver is in your PATH


# Open the target page
driver.get("https://rahulshettyacademy.com/AutomationPractice/")  # Replace with your page URL
sleep(2)  # wait for page to load

# Your original dropdown code
dropdown_element = driver.find_element(By.ID, "dropdown-class-example")
dropdown = Select(dropdown_element)

dropdown.select_by_visible_text("Option1")
sleep(1)
selected_option = dropdown.first_selected_option.text
if selected_option == "Option1":
    print("TC-R1 : PASS")
else:
    print("TC-R1 : FAIL")
    print("Attendu :", "Option1")
    print("Obtenu  :", selected_option)
driver.save_screenshot("dropdown_option1.png")

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

# Close the browser
driver.quit()
