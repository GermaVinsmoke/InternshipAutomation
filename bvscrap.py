import requests
import bs4 as bs
import os

myPath = "D:\\vaibhav\\Python\\JNTUH"
url = 'https://www.bvrit.ac.in/index.php/latest-news/607-b-tech-i-year-previous-question-papers'
headers = {'User-Agent': 'Chrome/67.0.3396.99'}
page = requests.get(url)
soup = bs.BeautifulSoup(page.text, 'lxml')
count = 0
for link in soup.find('div', class_='item-page').find_all("a"):
    print(link.get('href'))
    xyz = requests.get('https://www.bvrit.ac.in' +
                       link.get('href')).content
    with open(os.path.join(myPath, link.get('href').replace('/images/Articles/Examinations/', '')), 'wb') as g:
        g.write(xyz)
    count += 1
