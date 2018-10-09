# Created by Sabbir Ahmed @ 08 October, 2018
# This program will scrape wikipidia to obtain information about country name, capital name, land area, water area, population, gdp, hdi, timezone, tld and calling code of every independent states
from bs4 import BeautifulSoup
import requests
import csv
import re
import pprint

#Here are the patterns to extract formatted information from the soup
pattern_area = re.compile(r'^\d+\.?\d*')
pattern_pouplation = re.compile(r'^\d+\.?\d*')
pattern_gdp = re.compile(r'\$\s*(\d+\.?\d*)')
pattern_hdi = re.compile(r'^\d+\.?\d*')
pattern_time = re.compile(r'UTC\s*(.?\s*\d+:?\.?\d*)')
pattern_water = re.compile(r'^\d+\.?\d*')
pattern_density = re.compile(r'^\d+\.?\d*')
pattern_gini = re.compile(r'^\d+\.?\d*')
pattern_drive = re.compile(r'(right|left)')
pattern_capita = re.compile(r'\$\s*(\d+\.?\d*)')


def formatting(info):
    '''This function will format the extracted contents from html soup'''
    
    info['area'] = info['area'].replace(',', '')
    area_mo = pattern_area.search(info['area'])
    if area_mo:
        info['area'] = area_mo.group(0)
    
    water_mo = pattern_water.search(info['water'])
    if water_mo:
        info['water'] = water_mo.group(0)
    
    info['population'] = info['population'].replace(',', '')
    population_mo = pattern_pouplation.search(info['population'])
    if population_mo:
        info['population'] = population_mo.group(0)

    info['density'] = info['density'].replace(',', '')
    density_mo = pattern_density.search(info['density'])
    if density_mo:
        info['density'] = density_mo.group(0)

    info['gdp'] = info['gdp'].replace(',', '')
    gdp_mo = pattern_gdp.search(info['gdp'])
    if gdp_mo:
        val = pattern_gdp.search(info['gdp']).group(1)
        if 'trillion' in info['gdp'].lower():
            info['gdp'] = str(float(val) * 1000)
        else:
            info['gdp'] = val
    
    info['capita'] = info['capita'].replace(',', '')
    capita_mo = pattern_capita.search(info['capita'])
    if capita_mo:
        info['capita'] = capita_mo.group(1)
    
    gini_mo = pattern_gini.search(info['gini'])
    if gini_mo:
        info['gini'] = gini_mo.group(0)

    hdi_mo = pattern_hdi.search(info['hdi'])        
    if hdi_mo:
        info['hdi'] = hdi_mo.group(0)

    time_mo = pattern_time.search(info['time_zone'])
    if time_mo:
        info['time_zone'] = time_mo.group(1)

    drive_mo = pattern_drive.search(info['driving'])
    if drive_mo:
        info['driving'] = drive_mo.group(0)

    return info

def get_info(country):
    '''Get contents from the Wikipedia page and extract information for each country'''

    #Initially each information is set as string "N/A"
    info = {'capital': 'N/A', 'area': 'N/A', 'water': 'N/A', 'population': 'N/A', 'density': 'N/A', 'gdp': 'N/A', 'capita': 'N/A', 'gini': 'N/A', 'hdi': 'N/A', 'currency': 'N/A', 'time_zone': 'N/A', 'driving': 'N/A', 'calling_code': 'N/A', 'iso': 'N/A', 'tld': 'N/A'}

    page_url = "https://en.wikipedia.org" + country

    response = requests.get(page_url)

    #Checking whether there was any problem to download that particular page
    try:
        response.raise_for_status()
    except:
        print("Problem occured while getting response from website: " + page_url)
        return []

    soup = BeautifulSoup(response.text, 'html.parser').select_one('.infobox.geography.vcard')

    #Looping through all the rows in the Infobox Geography Vcard Table of wikipidia page
    for ind, row in enumerate(soup.findAll('tr')):
        # Skip the first row which contains the country official name. (Reason Gini conflicts)
        if ind == 0:
            continue

        #Not all rows contain table header (th). We will skip those.
        if not row.th:
            continue

        header_content = row.th.text.strip().lower()

        if "capital" in header_content:
            info['capital'] = row.td.a.text.strip()

        elif "area" in header_content:
            area_row = row.next_sibling
            if info['area'] == 'N/A':
                info['area'] = area_row.td.text.strip()

        elif "water" in header_content:
            if info['water'] == 'N/A':
                info['water'] = row.td.text.strip()
        
        elif "population" in header_content:
            population_row = row.next_sibling
            if info['population'] == 'N/A':
                info['population'] = population_row.td.text.strip()

        elif "density" in header_content:
            if info['density'] == 'N/A':
                info['density'] = row.td.text.strip()
        
        elif "gdp" in header_content:
            gdp_row = row.next_sibling
            if info['gdp'] == 'N/A':
                info['gdp'] = gdp_row.td.text.strip()

        elif "per capita" in header_content:
            if info['capita'] == 'N/A':
                info['capita'] = row.td.text.strip()
        
        elif 'gini' in header_content:
            info['gini'] = row.td.text.strip()

        elif "hdi" in header_content:
            info['hdi'] = row.td.text.strip()
        
        elif "currency" in header_content:
            info['currency'] = row.td.a.text.strip()

        elif "time" in header_content:
            info['time_zone'] = row.td.text.strip()
        
        elif "driving" in header_content:
            info['driving'] = row.td.text.strip()
        
        elif "calling" in header_content:
            if row.td.a:
                info['calling_code'] = row.td.a.text.strip()
            else:
                info['calling_code'] = row.td.text.strip()
        
        elif "iso" in header_content:
            info['iso'] = row.td.text.strip()

        elif "tld" in header_content:
            info['tld'] = row.td.a.text.strip()
        
        

    return info

#We will get the country list and their wiki links from the below url
country_list_page_url = 'https://en.wikipedia.org/wiki/Member_states_of_the_United_Nations'

response = requests.get(country_list_page_url)
soup = BeautifulSoup(response.text, 'html.parser').select_one('.sortable.wikitable')

# Writing the data to csv file
with open('country_data.csv', 'a', newline= '', encoding= 'utf-16') as f:
    writer = csv.writer(f)

    # Header Contents are written first
    writer.writerow(['Country', 'Capital', 'Land Area (sqkm)', 'Water(%)', 'Population', 'Density (/sqkm)', 'GDP(Billion $)', 'GDP Per Capita', 'Gini', 'HDI', 'Currency', 'Time Zone', 'Driving', 'Calling Code', 'ISO', 'Domain Name'])

    # Each contry information are written as looping through the table rows of wikitable
    # First row [0] is skipped since that was header in the wikitable
    for row in soup.select('tbody > tr')[1:]:

        # Each row contains 4 table data. Only the second one (index 1) contains country information
        country_soup = row.findAll('td')[1]

        # Extract country name from title attribute of <a> tag
        country_name = country_soup.a['title']
        print('Getting information - {} ...'.format(country_name))

        # Passing the href attribute value to the get_info function to obtain all the raw information about that country
        info = get_info(country_soup.a['href'])

        # Call formatting function to get nice presentable formatted data
        formatted_info = formatting(info)

        # Getting values from info dictionary
        data = list(formatted_info.values())

        # Inserting country name as a first cell in each row
        data.insert(0, country_name)

        # Writing data to csv file
        writer.writerow(data)
        print('DONE!')

f.close()

print('---Task Finished---')
