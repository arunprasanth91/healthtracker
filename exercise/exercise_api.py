from constants import constants
import requests
import json
import datetime as dt
ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise/"

exercise = input("What was your workout today? ")

headers = {
    'x-app-id':constants.Nutritionix_APPID,
    'x-app-key':constants.Nutritionix_APP_KEY,
    'x-remote-user-id':"ArunPrasanth",
    'Content-type':"application/json"
}

with open("exercise/exercise.json") as jsonData:
    payLoad = json.load(jsonData)
    payLoad['query'] = exercise
    print(payLoad)

    


date = dt.datetime.now().strftime("%D")
time = dt.datetime.now().strftime("%H:%M:%S")
response = requests.post(url=ENDPOINT,json=payLoad,headers=headers)
data = response.json()
print(f"Response json: {data}")
uploadData = []
uploadDataDict = {}
for d in data['exercises']:
    data_dict = {}
    data_dict['date'] = date,
    data_dict['time'] = time,
    data_dict['exercise'] = d['user_input']
    data_dict['duration'] = d['duration_min']
    data_dict['calories'] = d['nf_calories']
    uploadData.append(data_dict)

uploadDataDict['workout'] = uploadData

with open('exercise/workouts/workout.json','w') as workoutData:
    json.dump(uploadDataDict,workoutData)


    

