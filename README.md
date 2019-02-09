# Scraping Yellow Pages

A collection of python scripts which scrapes data from yellow pages using BeautifulSoup. Beautiful Soup is a Python package for parsing HTML and XML documents. The data includes schools and colleges in Nepal. 

## Webpages

- http://yellowpagesnepal.com/index.php?cat=541&page=1
- http://yellowpagesnepal.com/index.php?cat=196
- http://www.ypnepal.com/index.php?cat=530&Schools-&-Higher-Secondary-Schools
- http://www.ypnepal.com/index.php?cat=196&Colleges

## Requirement
Install its dependencies using
```
pip install -r requirements.txt
```

## How to run scripts
Open terminal and simply run the python script files.

```python ypnepal_college.py
python ypnepal_school.py	
python yellowpagesnepal_college.py	
python yellowpagesnepal_school.py	
```

```Tested using BeautifulSoup 4.4.0, Python 3.7.0```

---
## How to use data
The scripts dump the data in CSV, JSON files. You can click  <a href="https://github.com/hbvj99/dataset-collection" target="_blank">here</a> to find more dataset like this. Please refer to the licence below on how you can manipulate the data. The different information each files crawl from yellow pages includes;
```
- Name
- Address
- City
- Country
- Phone
- P.O.Box
- Email
- Mobile
- Webpage
- Fax
- Updatedon
```

#### CSV Dataset sample
```
Name,Address,City,Country,Phone,P.O.Box,Email,Mobile,Webpage,Fax,Updatedon
Aayaam International College,Kumaripati,Lalitpur,Nepal,"5550778,5537674",,aayaamcollege@gmail.com,,www.aayaamcollege.edu.np,	5552785,2015-10-08
Asian Institute of Technology & Management (AITM),Khumaltar,Lalitpur,Nepal,"5541179,5552376",,enquiries@aitm.edu.np,,www.aitm.edu.np,	5548772,2015-01-07
B & C Medical College & Teaching Hospital & Research Center,Birtamod-5,Jhapa,Nepal,"023-545566,542242",,info.bnchospital@gmail.com,,www.bnchospital.edu.np,,2018-06-13
```
#### JSON Sample
```
[{"Name": "Adarsha Kanya Niketan Higher Secondary School", "Address": "MangalBazar", "City": "Kathmandu", "Country": "Nepal", "Phone": "00977-1-5521488", "Email": "aknschool12@gmail.com", "Updatedon": "2009-11-07"}, {"Name": "Alok Vidyashram", "Address": "Gyaneshwor", "P.O.Box": "806,Ktm", "City": "Kathmandu", "Country": "Nepal", "Phone": "00977-1-4415912,016219909", "Email": "alokvidyashram@gmail.com", "Webpage": "www.alokvidyashram.edu.np", "Updatedon": "2017-02-13"}, {"Name": "Bhanubhakta Memorial Higher Secondary School", "Address": "Panipokhari", "P.O.Box": "10597,Ktm", "City": "Kathmandu", "Country": "Nepal", "Phone": "00977-1-4415538,4413586", "Fax": "\t00977-1-4428931", "Email": "info@bhanu.edu.np", "Webpage": "www.bhanu.edu.np", "Updatedon": "2009-11-07"}, {"Name": "Cambridge International Boarding Higher Secondary School", "Address": "Kalanki-14", "City": "Kathmandu", "Country": "Nepal", "Phone": "00977-1-5219858,5218003", "Email": "cambridge.college.kathmandu@gmail.com", "Webpage": "www.cambridgecollegekalanki.edu.np", "Updatedon": "2009-11-07"}, {"Name": "Galaxy Public School", "Address": "Gyaneshwor", "P.O.Box": "4901,Ktm", "City": "Kathmandu", "Country": "Nepal", "Phone": "00977-1-4410076,4411362", "Fax": "\t00977-1-4416989", "Email": "info@galaxy.edu.np", "Webpage": "www.galaxy.edu.np", "Updatedon": "2009-11-07"}]

```
---


### Contributions
You can modify the content, optimize the code or even use the dataset commercially as you may like. You can credit me by mentioning this repository if you wish. Pull requests are welcomed.

SUPPORT OPEN-SOURCE!


## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2019 © <a href="http://vijaypathak.com.np" target="_blank">Vijay Pathak</a>.
