from bs4 import BeautifulSoup
import requests
import re

# session = requests.Session()
# html = session.get('http://berkeleyheritage.com/berkeley_landmarks/landmarks1-100.html')
# print(html.content)
# soup = BeautifulSoup(html.content, 'html.parser')

with open('./landmarks1-100.html', 'r', encoding='latin-1') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
    # print(soup.prettify())

table = soup.find_all('table')[0]
# print(table)
# exit()

# for td in table.find_all('td'):
for td in table.find_all('td'):
    print(td)

    # print("\n")



