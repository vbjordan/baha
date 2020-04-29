import sys
from bs4 import BeautifulSoup
import geocoder
# import googlemaps
import requests
import re

file = sys.argv[1]

# gmaps = googlemaps.Client(key='AIzaSyCSSgQmDRC6ZpTU1EJkfWndsd2TEC0Jih0')

# session = requests.Session()
# html = session.get('http://berkeleyheritage.com/berkeley_landmarks/landmarks1-100.html')
# print(html.content)
# soup = BeautifulSoup(html.content, 'html.parser')

with open(file, 'r', encoding='latin-1') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
    # print(soup.prettify())

# print(soup.get_text())

# table = soup.find_all('table')[0]
# print(table)
# exit()
"""
number
name & link
city lm #
address
architect & date
initiated
designated
notes
"""

for tr in soup.find_all('tr')[1:]:
    # print(tr)
    row = []
    i = 0
    for td in tr.find_all('td'):
        # print(td)
        row.append(td.text)

        if i == 3:
            address = td.text
            print(address)
            # geocode = gmaps.geocode(address + ', Berkeley, CA')
            geocode = geocoder.osm(address + ', Berkeley, CA')
            print(geocode.osm)
            exit()

        url = td.find('a')
        if url:
            row.append(url['href'])

        i += 1

    # exit()

    # print("|".join(row))

    # print("\n")



