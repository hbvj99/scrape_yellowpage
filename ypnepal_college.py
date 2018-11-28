from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests
import csv
import json

def removeDuplicates(listofElements):
    uniqueLinks = []
    for elem in listofElements:
        if elem not in uniqueLinks:
            uniqueLinks.append(elem)
    return uniqueLinks

page = ("http://www.ypnepal.com/index.php?cat=196&Colleges")

m_page = (page)

req = Request(m_page)
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "lxml")

page_no = []

page_no.append(page)
college_data = []

for page in soup.find_all(True,{"class": ["paging"]}):
    page_no.append('http://www.ypnepal.com/%s' % page.get('href'))

page_no = removeDuplicates(page_no)
# print(page_no,"\n")

category_links = []    

for url in page_no: #page_no 
    print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    # soup = soup.find("div",{"class":"box-content2"})
    category = soup.find_all(True,{"class": ["category"]})
    for cat in category:
        category_links.append('http://www.ypnepal.com/%s' % cat.get('href'))

# print("\n",category_links,"\n")
# print(len(category_links))

college_data = []

def strip_data(label_data):
    lab = []
    for label in label_data:
        label_text = label.text
        label_text = label_text.replace(":", "")
        label_text = label_text.replace("\n", "")
        label_text = label_text.replace(" ", "")
        label_text = label_text.replace("http//", "")
        lab.append(label_text)
    return lab

for url in category_links:
    response = requests.get(url)
    print(url)

    if response.ok:
        soup = BeautifulSoup(response.content, "html.parser")
        # print(url)
        # print(len(category_links))

        name =  soup.select("h1")[0].text.strip()
        data = {'Name': name}

        label_left = soup.findAll('div',class_= "labelLeft")
        key = strip_data(label_left)
        
        label_right = soup.findAll('div',class_= "labelRight")
        if label_right:
            label_right.pop()

        value = strip_data(label_right)
        
        data.update(dict(zip(key, value)))

        if data.get('Description',None): data.pop('Description') #remove
        if data.get('ListingName',None): data.pop('ListingName')
        
        college_data.append(data)
        
print(college_data)

with open('ypnepal_college.csv', 'w') as csv_file:  
    fieldname = ['Name', 'Address', 'City','Country','Phone','P.O.Box','Email','Mobile', 'Webpage','Fax','Updatedon']
    scl = csv.DictWriter(csv_file, fieldnames=fieldname)
    scl.writeheader()
    scl.writerows(college_data)

with open ('ypnepal_college.json','w') as json_file:
    json.dump(college_data,json_file)