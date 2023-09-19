# import datetime
from bs4 import BeautifulSoup
from get_the_html import coach, no_ticket

with open('response', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html5lib')


def has_seat_type_tag(tag):
    return tag.has_attr('data-seat-type')


train_div = {val.find('h2').string: {tag.find('span', class_='seat-class-name').string: int(tag.find('span', class_='all-seats').string) for tag in val.find_all(has_seat_type_tag)} for val in
             soup.find_all('div', class_='row single-trip-wrapper list_rows')}


if not train_div:
    print('Sorry no train is available')
else:
    print('The following trains are available in that day:- ')
    train_list = list(train_div.keys())
    for serial, train in enumerate(train_list):
        print('{}| {}'.format(serial + 1, train))

    choice = input('Do you want to board any specific train? <Type "Y" for YES and "N" for "NO> ')
    if choice == 'Y':
        particular_train = train_list[int(input('Enter the train: <Type the train number serial in the display> ')) - 1]
    else:
        particular_train = None

if particular_train:
    if not train_div[particular_train].get(coach):
        print('{} coach is not available for {} train'.format(coach, particular_train))
    elif train_div[particular_train].get(coach) >= no_ticket:
        print('TICKET AVAILABLE')
    else:
        print('NOT AVAILABLE')
else:
    for train in train_div.keys():
        if not train_div[train].get(coach):
            continue
        elif train_div[train].get(coach) >= no_ticket:
            print('You can purchase {} ticket/s of {} coach from {} train'.format(no_ticket, coach, train))

