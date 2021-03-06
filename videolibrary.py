from bs4 import BeautifulSoup
import requests
import requests
import re

# Array of google drive links
WeekRecording = ["", "", "", "", "", "", "", "", ""]
WeekRecording[1] = "https://drive.google.com/file/d/1vyPoSlUc5hcXajllDyaqMKvlJOiYxbNH/view?usp=sharing"
WeekRecording[2] = "https://drive.google.com/file/d/1elgdm2482AMcARz_NUVTjg8KBPmoLTxj/view?usp=sharing"
WeekRecording[3] = "https://drive.google.com/file/d/1_RgK_fcatlpGOSDn6yokgOEZAFxKmTlc/view?usp=sharing"
WeekRecording[4] = "https://drive.google.com/file/d/1AFfRgg3y_ebWYsmJmANSQYFgOeDnVnwJ/view?usp=sharing"
WeekRecording[5] = "https://drive.google.com/file/d/1Gx_QXD9kQFJNi9_oOlQN4Sa9Irz0ki2K/view?usp=sharing"
WeekRecording[6] = "https://drive.google.com/file/d/1nx7eMPpso7oXgU-KViMQZb48qUZahLru/view?usp=sharing"
WeekRecording[7] = "https://drive.google.com/file/d/1hKgn7qnNlnd91_2YdzcFPwQvn5NeQS2A/view?usp=sharing"
WeekRecording[8] = "https://drive.google.com/file/d/1rQM7k4oCRTxnAb8gzIGVCgTv1gVuT3Wq/view?usp=sharing"


# BS4 magic
def getdrivelinks():
    # Send request for google drive page
    gdriverequest = requests.get("https://drive.google.com/drive/folders/1pFHUrmpLv9gEJsvJYKxMdISuQuQsd_qX")
    # Create a file and store google drive page with videos for offline use
    gdrivewebsite = open("gdrive.html", "w")
    gdrivewebsite.write(gdriverequest.text)
    gdrivewebsite.close()
    # Load the file with the Google drive page source
    gdriveraw = open('gdrive.html')
    # Let's make some tasty soup with it now
    soup = BeautifulSoup(gdriveraw, 'lxml')
    # Check for divs containing the data-tooltip as they contain the metadata for the individual videos
    soup = soup.find_all('div', {'data-tooltip'})
    # print the list of all the video names
    print(soup)

# TODO: Fix the issue with the regular expression and load video file names into array to use for summary payload
