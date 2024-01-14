print("Running linkedin.py...\n\n")

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
#options.add_argument('--headless')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

browser = webdriver.Chrome(r"C:\Windows\System32\chromedriver.exe", chrome_options = options)
browser.get(r"https://docs.google.com/forms/d/e/1FAIpQLSdhxqopQPUkUWsntlTyMolWr4Ab4NMuDiGHT4_gaGE4GIR1eg/viewform?pli=1")

all_elements = browser.find_elements(By.CSS_SELECTOR, "textarea")
questions = browser.find_elements(By.CSS_SELECTOR, "div[role = 'heading']")

# ignore title
for q in questions[1:]:
    print(q.text)

# Print the found elements
for element in all_elements:
    element.send_keys("HELLO")
    print(f"Successful for tag {element.tag_name} text {element.text}")

    

