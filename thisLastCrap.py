import requests
import bs4 as bs
import os
import time
from selenium import webdriver


def mtechDownload(i, myPath):
    parentPath = os.path.join(myPath, subjectList[i-1])
    print(parentPath)
    os.makedirs(parentPath)
    mtechSemester(i, parentPath)


def btechDownload(i, myPath):
    parentPath = os.path.join(myPath, subjectList[i-1])
    print(parentPath)
    os.makedirs(parentPath)
    if(i in noSemesterList):
        getNoSemester(i, parentPath)
    else:
        getSemester(i, parentPath)


def getNoSemester(i, parentPath):
    # time.sleep(5)
    driver.find_element_by_xpath(
        "//*[@id='pages-2']/ul/li[4]/ul/li[1]/ul/li["+str(i)+"]/a").click()
    url = driver.current_url
    page = requests.get(url)
    soup = bs.BeautifulSoup(page.text, 'lxml')
    downloadAndSave(soup, parentPath)


def getSemester(i, parentPath):
    if i == 9:
        takeList = informationTechList
    else:
        takeList = btechSemesterList
    for k in range(len(takeList)):
        childPath = os.path.join(parentPath, btechSemesterList[k])
        os.makedirs(childPath)
        print(childPath)
        # time.sleep(5)
        driver.find_element_by_xpath(
            "//*[@id='pages-2']/ul/li[4]/ul/li[1]/ul/li["+str(i)+"]/ul/li["+str(k+1)+"]/a").click()
        url = driver.current_url
        page = requests.get(url)
        soup = bs.BeautifulSoup(page.text, 'lxml')
        downloadAndSave(soup, childPath)


def mtechSemester(i, parentPath):
    for j in range(len(mtechSemesterList)):
        childPath = os.path.join(parentPath, mtechSemesterList[j])
        os.makedirs(childPath)
        print(childPath)
        # time.sleep(5)
        driver.find_element_by_xpath(
            "//*[@id='pages-2']/ul/li[4]/ul/li[2]/ul/li["+str(i-10)+"]/ul/li["+str(j+1)+"]/a").click()
        url = driver.current_url
        page = requests.get(url)
        soup = bs.BeautifulSoup(page.text, 'lxml')
        downloadAndSave(soup, childPath)


def downloadAndSave(soup, finalPath):

    count = 1
    for link in soup.find('div', class_='entry-content').find('ol').find_all('a'):
        print(link.get('href'))
        xyz = requests.get(link.get('href')).content
        with open(os.path.join(finalPath, "btech_1sem_"+str(count)+"_2016"+".pdf"), 'wb') as g:
            g.write(xyz)
        count += 1


myPath = "D:\\vaibhav\\Python\\JNTUH"

btechSemesterList = ['Semester 3', 'Semester 4',
                     'Semester 5', 'Semester 6', 'Semester 7', 'Semester 8']
mtechSemesterList = ['Semester 1', 'Semester 2']
informationTechList = ['Semester 4', 'Semester 5',
                       'Semester 6', 'Semester 7', 'Semester 8']
subjectList = ['1&2 Semester Combined', 'Civil', 'Combined Semester 3', 'Combined Semester 4', 'Combined Semester 5',
               'Computer Science', 'Electrical and Electronics', 'Electronics and Communication', 'Information Technology',
               'Mechanical', 'Mtech Computer Science', 'Control System', 'Machine Design', 'Power Control and Drives', 'Signal Processing',
               'Structural Engineering', 'Telecommunication Engineering']
noSemesterList = [1, 3, 4, 5]

driver = webdriver.Chrome("D:\\Programming Files\\chromedriver.exe")
driver.get('https://enggportal.wordpress.com/kerala-university-previous-year-question-papers-b-tech-m-tech/')
headers = {'User-Agent': 'Chrome/67.0.3396.99'}

for i in range(1, len(subjectList)+1):
    if(i < 11):
        btechDownload(i, myPath)
    else:
        mtechDownload(i, myPath)
