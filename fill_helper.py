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
path = input("Please enter COMPLETE path to chromedriver (should be in the current folder)")
browser = webdriver.Chrome(r"{}".format(path), chrome_options = options)
def get(link):
    
    browser.get(link)
    questions = browser.find_elements(By.CSS_SELECTOR, "div[role = 'heading']")
    # ignore title
    q_text = []
    for q in questions[1:]:
        q_text.append(q.text)
    return q_text

def fill(link, answers):
    browser.get(link)
    all_elements = browser.find_elements(By.CSS_SELECTOR, "textarea")
    # Print the found elements
    for element, ans in zip(all_elements, answers):
        element.send_keys(ans)

    print("Done")

    

