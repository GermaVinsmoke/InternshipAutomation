import requests
import bs4 as bs
import os

myPath = "D:\\vaibhav\\Python\\JNTUH"
url = 'https://www.keralauniversity.ac.in/downs'
headers = {'User-Agent': 'Chrome/67.0.3396.99'}
page = requests.get(url)
soup = bs.BeautifulSoup(page.text, 'lxml')
count = 1
for link in soup.find_all('a'):
    if 'Question' in link.text:
        print(link.text)
        xyz = requests.get('https://www.keralauniversity.ac.in' +
                           link.get('href')).content
        with open(os.path.join(myPath, str(count)+'.pdf'), 'wb') as g:
            g.write(xyz)
        count += 1
