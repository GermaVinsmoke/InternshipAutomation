import bs4 as bs
import requests
import os

myPath = "D:\\vaibhav\\Python\\SGT"
url = 'https://www.wctmgurgaon.com/question-paper.php'
headers = {'User-Agent': 'Chrome/67.0.3396.99'}
page = requests.get(url)
soup = bs.BeautifulSoup(page.text, 'lxml')
for link in soup.find("div", class_="right_side").find_all("a"):
    if('2015' in link.get('href')):
        print(link.get('href'))
        xyz = requests.get('https://www.wctmgurgaon.com/' +
                           link.get('href')).content
        with open(os.path.join(myPath, link.get('href').replace('questionpaper/', '')), 'wb') as g:
            g.write(xyz)
