from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
url = 'https://eticket.railway.gov.bd/booking/train/search/en?fromcity=Rajshahi&tocity=Dhaka&doj=30-Aug-2023&class=SNIGDHA'

driver.get(url)
soup = BeautifulSoup(driver.page_source, 'lxml')
driver.quit()


train_div = soup.find_all('div', class_='row single-trip-wrapper list_rows')

# particular_train_div = None

# dhumketu_div, silkcity_div, padma_div = None, None, None


for div in train_div:
    if 'SILKCITY EXPRESS' in div.text:
        silkcity_div = div
        break

else:
    raise Exception('NO TRAIN FOUND')

silkcity_seat_category = silkcity_div.find_all('div', class_='single-seat-class seat-available-wrap  seat-available-wrap')

if silkcity_seat_category:
    print(silkcity_seat_category.prettify())
else:
    raise Exception('Seat Class div not found')

for div in silkcity_seat_category:
    if 'SNIGDHA' in div.text:
        print('FOUND')
        print(div.prettify())
        val = div.find('span', class_='all-seats').text
        print(val)
        break
else:
    print('NOT FOUND')
