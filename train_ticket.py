# import requests
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Safari()
url = 'https://eticket.railway.gov.bd/booking/train/search/en' + '?fromcity=Rajshahi&tocity=Dhaka&doj=29-Aug-2023&class=SNIGDHA'

# payload = {'fromcity': 'Rajshahi', 'tocity': 'Dhaka', 'doj': '14-Jul-2023', 'class': 'SNIGDHA'}
# response = requests.get('https://eticket.railway.gov.bd/booking/train/search/en', params = payload)
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'lxml')
driver.quit()
# print(soup.prettify())

train_div = soup.find_all('div', class_='row single-trip-wrapper list_rows')
# particular_train_div = None
dhumketu_div, silkcity_div, padma_div = None, None, None

for div in train_div:
    if 'DHUMKETU EXPRESS' in div.text:
        dhumketu_div = div
    elif 'SILKCITY EXPRESS' in div.text:
        silkcity_div = div
    elif'PADMA EXPRESS' in div.text:
        padma_div = div
# else:
#     print('NOT FOUND')

for div in (dhumketu_div, silkcity_div, padma_div):
        for subdiv in div.find_all('div'):
            if 'SNIGDHA' in subdiv.text:
                print('FOUND')
                val = subdiv.find('div', class_='available-text open-for-all').text
                print(val)
                break
else:
    print('NOT FOUND')
