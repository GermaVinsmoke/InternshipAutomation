import bs4 as bs
import urllib.request
import requests
import re
import os

source = urllib.request.urlopen(
    "http://www.aceec.ac.in/jntuh-previous-question-papers-b-tech-i-year/#1520074086827-09e642fd-ad73")
soup = bs.BeautifulSoup(source, "lxml")

myPath = "D:\\vaibhav\internship craps\\Automation script\\JNTUH"
count = 1
for link in soup.find("div", class_="wpb_wrapper").find_all("a"):
    if(link.get('href')[0] is not "#"):
        print(link.text)
        xyz = requests.get(link.get('href')).content
        with open(os.path.join(myPath, str(count) + ".pdf"), 'wb') as g:
            g.write(xyz)
        count += 1
