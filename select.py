import requests
from bs4 import BeautifulSoup

f = open("designers.txt", 'r')
lines = f.readlines()

for line in lines:
    try:
        response = requests.get(line[:-1], headers = {'User-agent': 'your bot 0.1'})
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        one = soup.select('div[class=perfumeslist]')

        for two in one:
            tree = two.select('a')
            four = str(tree[0])
            startIndex = four.find('"')
            endIndex = four.find('"', startIndex+1)
            print("https://www.fragrantica.com" + four[startIndex+1:endIndex])
    except:
        pass

f.close()
