from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("detach", True)
delay = 5

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://console.cloud.google.com/apis/credentials/consent?project=crm-contact-rolling-machine")

email = driver.find_element(By.XPATH, "//input[@type='email']")
email.clear()
email.send_keys('CRMContactRollingMachine@gmail.com')
next_button = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span')
next_button.click()
password = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='password']")))
password.send_keys('crmisbest')
next_button = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button')
next_button.click()

try:
	check_box = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-mdc-checkbox-2-input"]')))
	check_box.click()
	agree = driver.find_element(By.XPATH, '//*[@id="mat-dialog-0"]/xap-deferred-loader-outlet/ng-component/mat-dialog-actions/cfc-progress-button/div[1]/button/span[2]/span')
	agree.click()
except:
	print("Already Agreed")

delete=0
while delete<1:
	try:
		deleteUsers = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="mdc-icon-button mat-mdc-icon-button mat-unthemed mat-mdc-button-base cm-button ng-star-inserted"]')))
		deleteUsers.click()
		confirm = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="_0rif_mat-dialog-0"]/xap-deferred-loader-outlet/ng-component/div[2]/cfc-progress-button/div[1]/button')))
		confirm.click()
	except:
		delete=1
		print("No More users to delete :)")



