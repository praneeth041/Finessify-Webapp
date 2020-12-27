from datetime import datetime, timedelta

from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

import pickle

scopes = ['https://www.googleapis.com/auth/calendar']
flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
credentials = flow.run_console()

pickle.dump(credentials, open("token.pkl", "wb"))

credentials = pickle.load(open("token.pkl", "rb"))

service = build("calendar", "v3", credentials=credentials)

result = service.calendarList().list().execute()

calendar_id = result['items'][0]['id']

events = service.events().list(calendarId=calendar_id, timeZone="Asia/Kolkata").execute()

start_time = datetime(2020, 12, 31, 19, 30, 0)
end_time = start_time + timedelta(hours=1.5)
timezone = 'Asia/Kolkata'

event = {
  'summary': 'Workout',
  'location': 'Hyderabad',
  'description': '',
  'start': {
    'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
    'timeZone': timezone,
  },
  'end': {
    'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
    'timeZone': timezone,
  },
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },
}

service.events().insert(calendarId=calendar_id, body=event).execute()