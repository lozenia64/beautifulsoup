import requests
from bs4 import BeautifulSoup

def func_height(strr):
    startIndex = strr.find('height')
    endIndex = strr.find(';',startIndex)
    return strr[startIndex+8:endIndex-2]

print("Name, Group, MainNote1, MainNote2, MainNote3, Season, Day/Night, Longevity, Sillage, Rating")

f = open("url/i.txt", 'r')
lines = f.readlines()

for line in lines:
    response = requests.get(line[:-1], headers = {'User-agent': 'your bot 0.1'})
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    rat = soup.select('span[itemprop=ratingValue]')
    print(soup)
    print(rat)
f.close()
