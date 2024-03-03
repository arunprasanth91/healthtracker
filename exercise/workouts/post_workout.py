import requests
import json
from constants import constants
ENDPOINT = "https://api.sheety.co/akshdasjdhkasjh23213jsldfasjh2398yejdskfbskdjf123/myWorkouts/workouts"
header = {
    "Authorization": constants.Sheets_Auth
}
workoutData = None

with open("exercise/workouts/workout.json",'r') as workouts:
    workoutData = json.load(workouts)
    print(workoutData)


response = requests.post(url=ENDPOINT,json=workoutData,headers=header)
response.raise_for_status
print(response.status_code)
