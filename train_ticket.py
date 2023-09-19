# import datetime
from bs4 import BeautifulSoup

with open('response', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html5lib')

train_div = {val.find('h2').string: val for val in soup.find_all('div', class_='row single-trip-wrapper list_rows')}


if not train_div:
    print('Sorry no train is available')
else:
    print('The following trains are available in that day:- ')
    train_list = list(train_div.keys())
    for serial, train in enumerate(train_list):
        print('{}| {}'.format(serial+1, train))

    choice = input('Do you want to board any specific train? <Type "Y" for YES and "N" for "NO> ')
    if choice == 'Y':
        particular_train = train_list[int(input('Enter the train: <Type the train number serial in the display> ')) - 1]
    else:
        particular_train = None

    print(particular_train)



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
