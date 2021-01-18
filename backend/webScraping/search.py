import requests
import nltk
import random
from bs4 import BeautifulSoup

user_sleep = '10pm to 6:30am'
sleep = nltk.word_tokenize(user_sleep)

tasks = "Meditation, run, Socialize, Workout, Study"

activities = nltk.word_tokenize(tasks)
matched = []


def getTime(activities):

    for activity in activities:

        url = 'https://www.google.com/search?q=when+is+the+most+ideal+time+to+'+activity+'&rlz=1C1CHBF_enIN932IN932&oq=When+&aqs=chrome.0.69i59l3j69i57j0i67i395i457j69i61l3.2148j1j1&sourceid=chrome&ie=UTF-8'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}

        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')

        result = soup.find('div', class_="LGOjhe")

        if result is not None:

            sentence = str(result.text).lower()
            words = nltk.word_tokenize(sentence)
            matched.append(activity)

            for i in range(len(words)):
                if words[i] =='am' or words[i] =='pm' or words[i] =='a.m.' or words[i] =='p.m.':
                    matched.append(words[i-1] + words[i])
                elif words[i] =='morning' or words[i] =='afternoon' or words[i] =='evening' or words[i] =='night' or words[i] == 'sunrise' or words[i] == 'sunset':
                    matched.append(words[i])

    if matched is not None:
        return matched

Timings = getTime(activities)
act = []

for activity in activities:
    if activity in Timings:
        act.append(activity)

for i in range(len(Timings)):
    if Timings[i] == act[0] or Timings[i] == act[1] or Timings[i] == act[2] or Timings[i] == act[3] or Timings[i] == act[4]:
        if Timings 

def getTime2(Timings, sleep):
    pass


