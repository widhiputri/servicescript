from selenium import webdriver
from time import sleep

#Add path to your chrome profile
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\USER\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(executable_path="C:\\Users\\USER\\Document\\Quadrant\\chromedriver.exe", chrome_options=options)

#Navigate to website
print('open url')
w.get(r'https://platform.quadrant.io/Services/locationQualityAnalysis.htm')
sleep(1)
w.find_element_by_xpath('//option[@value="Hydra"]').click()
sleep(1)
w.find_element_by_xpath('//option[@value="2019"]').click()
sleep(1)
w.find_element_by_xpath('//option[@value="8"]').click()
sleep(1)
w.find_element_by_xpath('//a[@id="loadBtn"]').click()

#Quit browser
driver.quit()