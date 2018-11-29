from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
# import re
import requests
import csv

with open('college.csv','a') as csv_file:
    fieldname = ['Name', 'Address', 'PO_BOX', 'Phone', 'Email', 'Webpage']
    scl = csv.DictWriter(csv_file, fieldnames=fieldname)
    scl.writeheader()

def removeDuplicates(listofElements):
    # Create an empty list to store unique elements
    uniqueLinks = []
    # Iterate over the original list and for each element
    # add it to uniqueList, if its not already there.
    for elem in listofElements:
        if elem not in uniqueLinks:
            uniqueLinks.append(elem)
    # Return the list of unique elements
    return uniqueLinks

page = ("http://yellowpagesnepal.com/index.php?cat=196&page=1")

m_page = (page)

req = Request(m_page)meaningmeaning
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "lxml")

page_no = []

page_no.append(page)

for page in soup.find_all(True,{"class": ["paging"]}):
    page_no.append('http://yellowpagesnepal.com/%s' % page.get('href'))

page_no = removeDuplicates(page_no)
# print(page_no,"\n")

category_links = []    

for url in page_no[:1]: #page_no 
    # print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    soup = soup.find("div",{"class":"box-content2"})
    category = soup.find_all(True,{"class": ["category"]})
    for cat in category:
        category_links.append('http://yellowpagesnepal.com/%s' % cat.get('href'))

category_links = removeDuplicates(category_links)
# print("\n",category_links,"\n")
# print(len(category_links))]

for url in category_links[:20]: #print 20
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    # print(url)
    # print(len(category_links))
    label_right = soup.findAll('div',class_= "labelRight")

    # name = soup.find('h1')
    name =  soup.select("h1")[0].text.strip()

    # address = soup.findAll('div',class_= "labelRight")[0].text.strip()
    #address = label_right[0].text.strip()
    try:
        address = label_right[0].text.strip()
    except IndexError:
        address = ''

    # p_box = label_right[1].text.strip()
    try:
        p_box = label_right[1].text.strip()
    except IndexError:
        p_box = ''

    # phone = label_right[2].text.strip()
    try:
        phone = label_right[2].text.strip()
    except IndexError:
        phone = ''

    # email = label_right[3].text.strip()
    try:
        email = label_right[3].text.strip()
    except IndexError:
        email = ''   

    # webpage = label_right[4].text.strip()
    try:
        webpage = label_right[4].text.strip()
    except IndexError:
        webpage = ''    

    print(name)
    print(address)
    print(p_box)
    print(phone)
    print(email)
    print(webpage,"\n")

    flist = [name,address,p_box,phone,email,webpage]

    # print(flist)
    with open('college.csv','a') as csv_file:
        scl = csv.writer(csv_file)
        scl.writerow(flist)
