import requests
from constants import constants
ENDPOINT = "https://api.sheety.co/e878a0e14fd508abbd56447e8e6d1fbf/myWorkouts/workouts/"
header = {
    "Authorization": constants.Sheets_Auth
}
workoutData = None

with open("exercise/workouts/workout.json",'r') as workouts:
    workoutData = json.load(workouts)

response = requests.put(url=f"ENDPOINT{2}",json=workoutData,headers=header)
response.raise_for_status

responseJson = response.json()

for key in responseJson.keys():
    if key == "calories":
        assert responseJson[key] == 220
