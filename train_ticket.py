from bs4 import BeautifulSoup

with open('response.html', 'r') as f:
    soup = BeautifulSoup(f, 'html5lib')


def has_seat_type(tag):
    if tag.has_attr('data-seat-type'):
        if 'AC_S' in tag['data-seat-type']:
            return True
        else:
            return False
    else:
        return False


train_div = soup.find('h2', string='BANALATA EXPRESS (792)').parent.parent

seat_category_div = train_div.find(has_seat_type)

print('Available seats = ', seat_category_div.find('span', class_='all-seats').string)

