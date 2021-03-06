# libraries
from bs4 import BeautifulSoup
import requests
from APIFunctions import *
from videolibrary import *
import lxml
import os
from colorama import Fore, Back, Style

# Directory search
directory_array = next(os.walk('.'))[1]
del directory_array[-1]  # Fix for the
directory_array.pop(0)  # Extra directories
directory_array.pop(0)  # From GIT and pycharm


# print(directory_array) use for testing array
def clear():
    directorycounter = 1
    for x in directory_array:
        summary = ""
        data = [{'type': 'num', 'section': 0, 'summary': '', 'summaryformat': 1, 'visible': 1, 'highlight': 0,
                 'sectionformatoptions': [{'name': 'level', 'value': '1'}]}]
        # Assign the correct summary
        data[0]['summary'] = summary
        # Set the correct section number
        data[0]['section'] = directorycounter
        # Write the data back to Moodle
        sec_write = LocalUpdateSections(courseid, data)


def updatelinks():
    directorycounter = 1
    for x in directory_array:
        # BS4 magic
        htmlfile = open("wk" + str(directorycounter) + "/index.html", encoding="utf8")
        soup = BeautifulSoup(htmlfile, 'lxml')
        soup = soup.title
        # Building summary
        title = '<h2>' + soup.string + '</h2>'
        powerpoint = '<a href="https://mikhail-cct.github.io/ooapp/wk' + str(
            directorycounter) + '/">' + '<img src="https://icon-library.net//images/powerpoint-icon-vector/powerpoint' \
                                        '-icon-vector-29.jpg" width="50" /> <b><h3>Powerpoint</h3></b>' + '</a> '
        video = '<a href="' + WeekRecording[directorycounter] + '"/><img src="https://icon-library.net//images' \
                                                                '/recording-icon-png/recording-icon-png-25.jpg" ' \
                                                                'width="50" /><b><h3>Recording</h3></b></a> '
        pdf = '<a href="https://github.com/mikhail-cct/ca3-test/raw/master/wk{}/wk{}.pdf"><img ' \
              'src="https://icon-library.net//images/pdf-icon-image/pdf-icon-image-27.jpg" width="50" ' \
              '/><b><h3>PDF</h3></b></a>'.format(
            str(directorycounter),
            str(directorycounter))
        summary = title + '<hr> ' + video + '<hr> ' + powerpoint + '<hr> ' + pdf
        data = [{'type': 'num', 'section': 0, 'summary': '', 'summaryformat': 1, 'visible': 1, 'highlight': 0,
                 'sectionformatoptions': [{'name': 'level', 'value': '1'}]}]
        # Assign the correct summary
        data[0]['summary'] = summary
        # Set the correct section number
        data[0]['section'] = directorycounter
        # Write the data back to Moodle
        sec_write = LocalUpdateSections(courseid, data)
        print(Fore.YELLOW+json.dumps(sec.getsections[directorycounter]['summary'], indent=4, sort_keys=True))
        directorycounter += 1


# main program
courseid = "23"  # Course ID
sec = LocalGetSections(courseid)
instalationcheck = input(Fore.CYAN + "Would you like to perform library setup:y/n?: ")
if instalationcheck == "y":
    os.system('pip install lxml')
    os.system('pip install requests')
    os.system('pip install bs4')
    os.system('pip install colorama')
    print(Fore.LIGHTGREEN_EX + "Setup Complete!")
    print("\n")
else:
    print("\n")

while True:
    command = input(Fore.LIGHTBLUE_EX+">> ")
    if command == "/gdrive":
        getdrivelinks()
    elif command == "/update":
        updatelinks()
    elif command == "/clear":
        confirm = input(Fore.RED + "Are you sure you want to clear? y/n: ")
        if confirm == "y":
            clear()
            print(Fore.LIGHTCYAN_EX + "Cleared Moodle page")
    elif command == "/dir":
        print(Fore.CYAN)
        print(directory_array)
    else:
        print("Commands: /gdrive, /update, /clear /dir")
