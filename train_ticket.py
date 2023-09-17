# import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome()

day_name = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
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


def get_html(url):
    driver.get(url)
    with open('response', 'w', encoding='utf_8') as f:
        f.write(driver.page_source)

    driver.quit()


def get_url(from_station, to_station, journey_date, seat_type):
    if not from_station.isalpha():
        from_station = '%20'.join(from_station.split(' '))
    if not to_station.isalpha():
        to_station = '%20'.join(to_station.split(' '))

    year, month, date = journey_date.split('/')
    journey_date = date + '-' + month_name[month] + '-' + year

    return 'https://eticket.railway.gov.bd/booking/train/search/en?fromcity={}&tocity={}&doj={}3&class={}'.format(from_station, to_station, journey_date, seat_type)


# def get_available_train(starting_station, ending_station, date):
#     date_tup = tuple(map(int, date.split('/')))
#     date_obj = datetime.date(*date_tup)
#     day = day_name[date_obj.weekday()]


from_city = input('Enter the from-city: ')
to_city = input('Enter the to-city: ')
doj = input('Enter date of journey <YYYY/MM/DD>: ')
coach = input('Enter the coach type: ')
no_ticket = int(input('Enter how many tickets you want to purchase: '))

# train_name = input('Enter the ')  <- Provide user to enter a specific train. Have to improvise later.

url = get_url(from_city, to_city, doj, coach)

print(url)

get_html(url)

# with open('response.html', 'r') as f:
#     soup = BeautifulSoup(f, 'html5lib')
#
#
# def has_seat_type(tag):
#     if tag.has_attr('data-seat-type'):
#         if 'AC_S' in tag['data-seat-type']:
#             return True
#         else:
#             return False
#     else:
#         return False
#
#
# train_div = soup.find('h2', string='BANALATA EXPRESS (792)').parent.parent
#
# seat_category_div = train_div.find(has_seat_type)
#
# print('Available seats = ', seat_category_div.find('span', class_='all-seats').string)
