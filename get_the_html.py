from selenium import webdriver
from selenium.webdriver.chrome.options import Options

month_name = {
    '01': 'Jan',
    '02': 'Feb',
    '03': 'Mar',
    '04': 'Apr',
    '05': 'May',
    '06': 'Jun',
    '07': 'Jul',
    '08': 'Aug',
    '09': 'Sep',
    '10': 'Oct',
    '11': 'Nov',
    '12': 'Dec'
}


def get_url(from_station, to_station, journey_date, seat_type):
    if not from_station.isalpha():
        from_station = '%20'.join(from_station.split(' '))
    if not to_station.isalpha():
        to_station = '%20'.join(to_station.split(' '))

    year, month, date = journey_date.split('/')
    journey_date = date + '-' + month_name[month] + '-' + year

    return 'https://eticket.railway.gov.bd/booking/train/search/en?fromcity={}&tocity={}&doj={}&class={}'.format(
        from_station, to_station, journey_date, seat_type)


def get_html(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    with open('response', 'w', encoding='utf-8') as f:
        f.write(driver.page_source)

    driver.quit()


from_city = input('Enter the from-city: ')
to_city = input('Enter the to-city: ')
doj = input('Enter date of journey <YYYY/MM/DD>: ')
coach = input('Enter the coach type: ')
no_ticket = int(input('Enter how many tickets you want to purchase: '))

url = get_url(from_city, to_city, doj, coach)
print(url)
get_html(url)
