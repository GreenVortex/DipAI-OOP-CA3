# libraries
from bs4 import BeautifulSoup
import requests
from APIFunctions import *
import lxml
import os

courseid = "23"  # Course ID
sec = LocalGetSections(courseid)
print(json.dumps(sec.getsections[1]['summary'], indent=4, sort_keys=True))
month = parser.parse(list(sec.getsections)[1]['name'].split('-')[0])
print(month)

data = [{'type': 'num', 'section': 0, 'summary': '', 'summaryformat': 1, 'visible': 1, 'highlight': 0,
         'sectionformatoptions': [{'name': 'level', 'value': '1'}]}]
summary = '<a href="https://mikhail-cct.github.io/ooapp/wk1/">Week 1: Introduction</a>'
# Assign the correct summary
data[0]['summary'] = summary

# Set the correct section number
data[0]['section'] = 1

# Write the data back to Moodle
sec_write = LocalUpdateSections(courseid, data)

sec = LocalGetSections(courseid)
print(json.dumps(sec.getsections[1]['summary'], indent=4, sort_keys=True))

# BS4
HttpRequest = requests.get('https://mikhail-cct.github.io/ooapp/wk1/')
HttpRequest = HttpRequest.text
soup = BeautifulSoup(HttpRequest, 'lxml')
# print(soup.prettify())
print(soup.title)


# Directory search
def getweeksdir():
    directory_array = next(os.walk('.'))[1]
    del directory_array[-1]  # Fix for the
    directory_array.pop(0)   # Extra directories
    directory_array.pop(0)   # From GIT and pycharm
    print(directory_array)


# main program
getweeksdir()
