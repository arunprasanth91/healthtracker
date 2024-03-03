import requests
from constants import constants

ENDPOINT = "https://api.sheety.co/e878a0e14fd508abbd56447e8e6d1fbf/myWorkouts/workouts"
header = {
    "Authorization": constants.Sheets_Auth
}
response = requests.get(url=ENDPOINT,headers=header)
response.raise_for_status
responseData = response.json()
print(responseData)