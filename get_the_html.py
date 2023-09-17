from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Safari(options=chrome_options)
url = 'https://eticket.railway.gov.bd/booking/train/search/en?fromcity=Rajshahi&tocity=Dhaka&doj=13-Sep-2023&class=SNIGDHA'

driver.get(url)

with open('response', 'w') as f:
    f.write(driver.page_source)

driver.quit()
