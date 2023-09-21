# import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import bdtrain

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


def get_html():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    global url, from_city, to_city, doj, coach
    url = get_url(from_city, to_city, doj, coach)
    print(url)
    driver.get(url)

    with open('response', 'w', encoding='utf-8') as f:
        f.write(driver.page_source)

    driver.quit()


def has_seat_type_tag(tag):
    return tag.has_attr('data-seat-type')


from_city = input('Enter the from-city: ')
to_city = input('Enter the to-city: ')
doj = input('Enter date of journey <YYYY/MM/DD>: ')
coach = input('Enter the coach type: ')
no_ticket = int(input('Enter how many tickets you want to purchase: '))
url = None
counter = 0
prev_station = None
flag = 0


def get_train_info():
    global counter
    counter += 1

    get_html()

    with open('response', 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html5lib')

    train_div = {val.find('h2').string: {
        tag.find('span', class_='seat-class-name').string: int(tag.find('span', class_='all-seats').string) for tag in
        val.find_all(has_seat_type_tag)} for val in
        soup.find_all('div', class_='row single-trip-wrapper list_rows')}

    return train_div

    # print(train_div)


train_info = get_train_info()

if not train_info:
    print('Sorry no train is available')

print('The following trains are available in that day:- ')
train_list = list(train_info.keys())
for serial, train in enumerate(train_list):
    print('{}| {}'.format(serial + 1, train))

choice = input('Do you want to board any specific train? <Type "Y" for YES and "N" for "NO> ')
if choice == 'Y':
    particular_train = train_list[int(input('Enter the train: <Type the train number serial in the display> ')) - 1]
else:
    particular_train = None

if particular_train:
    if coach not in train_info[particular_train]:
        print('{} coach is not available for {} train'.format(coach, particular_train))
        # break
    elif train_info[particular_train].get(coach) >= no_ticket:
        print('TICKET AVAILABLE')
        print('Click the flowing link to purchase: ')
        print(url)
        flag = 1
        # break
    else:
        train_name, code = particular_train.split('(')
        train_name = train_name.strip()
        code = int(''.join([digit for digit in code if digit.isnumeric()]))
        for trn in bdtrain.trains:
            if train_name == trn.name:
                train_class = trn

        if code % 2 == 1:
            stn = to_city
            remaining_stations = train_class.next_stations(code, stn)
        else:
            stn = from_city
            remaining_stations = train_class.previous_stations(code, stn)

        for station in remaining_stations:
            if code % 2 == 1:
                from_city = station
            train_info = get_train_info()
            print(train_info)
            if train_info[particular_train].get(coach) >= no_ticket:
                print('-' * 50)
                print('TICKET AVAILABLE')
                print('Click the following link to purchase: ')
                print(url)
                flag = 1
                break
if flag == 0:
    print('Sorry No Seat found!')

    # else:
    #     pass
    #     # for train in train_div.keys():
    #     #     if not train_div[train].get(coach):
    #     #         continue
    #     #     elif train_div[train].get(coach) >= no_ticket:
    #     #         print('You can purchase {} ticket/s of {} coach from {} train'.format(no_ticket, coach, train))
