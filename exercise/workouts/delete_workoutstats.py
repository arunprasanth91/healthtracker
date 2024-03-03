import requests
ENDPOINT = "https://api.sheety.co/e878a0e14fd508abbd56447e8e6d1fbf/myWorkouts/workouts/"
from constants import constants
header = {
    "Authorization": constants.Sheets_Auth
}
response = requests.delete(url=f"ENDPOINT{2}",headers=header)

response.raise_for_status
print(response.status_code)
