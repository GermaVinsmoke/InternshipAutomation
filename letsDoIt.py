import os
import bs4 as bs
import urllib.request
from selenium import webdriver
import requests
import time

myPath = "D:\\vaibhav\internship craps\\Automation script\\"
semester_list = ["Semester1", "Semester2", "Semester3"]
subject_list = ["1st&2nd Combined", "3rd Combined", "4th Combined",
                "Civil", "Computer Science", "Electrical & Electronics", "Electrical & Communication", "Mechanical",
                "CSE-Mtech", "Control Systems", "Machine Design", "Power Control & Drives", "Signal Processing", "Structural Engineering",
                "Telecommunication Engineering"]

driver = webdriver.Chrome("D:\\Programming Files\\chromedriver.exe")
driver.get('https://mbcetlibrary.wordpress.com/ktu-apj-abdul-kalam-technological-university-kerala-technological-university-previous-year-b-tech-m-tech-question-papers/')
count = 0
bm = 1
check = 1

for i in range(len(subject_list)):
    parentPath = os.path.join(myPath, subject_list[i])
    os.makedirs(parentPath)
    count += 1

    if(count > 8):
        bm = 2
        count = 1

    if(check > 3):
        for j in range(len(semester_list)):
            childPath = os.path.join(parentPath, semester_list[j])
            os.makedirs(childPath)
            time.sleep(5)
            driver.find_element_by_xpath(
                "//*[@id='pages-2']/ul/li/ul/li["+str(bm)+"]/ul/li["+str(count)+"]/ul/li["+str(j+1)+"]/a").click()
            sauce = urllib.request.urlopen(driver.current_url)
            soup = bs.BeautifulSoup(sauce, "lxml")
            num2 = 1
            for link in soup.find("div", class_="entry-content").find("ol").find_all("a"):
                print(link.get('href'))
                xyz = requests.get(link.get('href')).content
                with open(os.path.join(childPath, str(num2) + ".pdf"), 'wb') as g:
                    g.write(xyz)
                num2 += 1
    else:
        time.sleep(5)
        driver.find_element_by_xpath(
            "//*[@id='pages-2']/ul/li/ul/li["+str(bm)+"]/ul/li["+str(count)+"]/a").click()
        sauce = urllib.request.urlopen(driver.current_url)
        soup = bs.BeautifulSoup(sauce, "lxml")
        num1 = 1
        for link in soup.find("div", class_="entry-content").find("ol").find_all("a"):
            print(link.get('href'))
            xyz = requests.get(link.get('href')).content
            with open(os.path.join(parentPath, str(num1) + ".pdf"), 'wb') as g:
                g.write(xyz)
            num1 += 1
    check += 1
