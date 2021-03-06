# libraries
from bs4 import BeautifulSoup
import requests
from APIFunctions import *
from videolibrary import *
import lxml
import os

# Directory search
directory_array = next(os.walk('.'))[1]
del directory_array[-1]  # Fix for the
directory_array.pop(0)  # Extra directories
directory_array.pop(0)  # From GIT and pycharm


# print(directory_array) use for testing array


def updatelinks():
    directorycounter = 1
    for x in directory_array:
        # BS4 magic
        htmlfile = open("wk"+str(directorycounter)+"/index.html", encoding="utf8")
        soup = BeautifulSoup(htmlfile, 'lxml')
        soup = soup.title
        summary = '<a href="https://mikhail-cct.github.io/ooapp/wk' + str(directorycounter) + '/">' + soup.string + '</a> &nbsp ''<a href="' + WeekRecording[directorycounter] + '> Week ' + str(directorycounter) + ' video </a> ' + '&nbsp <a href="https://github.com/mikhail-cct/ca3-test/raw/master/wk'+ str(directorycounter) +'/wk'+ str(directorycounter) +'.pdf>PDF Lesson</a>'
        data = [{'type': 'num', 'section': 0, 'summary': '', 'summaryformat': 1, 'visible': 1, 'highlight': 0,
                 'sectionformatoptions': [{'name': 'level', 'value': '1'}]}]
        # Assign the correct summary
        data[0]['summary'] = summary
        # Set the correct section number
        data[0]['section'] = directorycounter
        # Write the data back to Moodle
        sec_write = LocalUpdateSections(courseid, data)
        print(json.dumps(sec.getsections[directorycounter]['summary'], indent=4, sort_keys=True))
        directorycounter += 1


# main program
courseid = "23"  # Course ID
sec = LocalGetSections(courseid)
updatelinks()
