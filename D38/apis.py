import datetime
import requests
import os
from dotenv import load_dotenv

load_dotenv()


class restApi:

    intakeEndPoint = "https://trackapi.nutritionix.com/v2/natural/nutrients"
    exerciseEndPoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
    allExercises = "https://api.sheety.co/eeaa41014b3e0eb466468ab65d427a79/myWorkouts/workouts"
    now = datetime.datetime.now()
    headers = {
        'Content-Type': 'application/json',
        'x-app-id': os.getenv('NUTRITIONIX_APP_ID'),
        'x-app-key': os.getenv('NUTRITIONIX_API_KEY')
    }

    def enterExercises(self, data):
        body = {
            "query": data
        }
        try:
            res = requests.post(url=self.exerciseEndPoint,
                                headers=self.headers, json=body)
        except Exception as e:
            print(e)
        else:
            data = res.json()
            payload = {"workout": []}
            for exercise in data['exercises']:
                payload["workout"] = {
                    "date": self.now.date().strftime("%Y-%m-%d"),
                    "time": self.now.strftime("%H:%M"),
                    "exercise": exercise['user_input'].title(),
                    "duration": exercise['duration_min'],
                    "calories": exercise['nf_calories']
                }
                print(payload)
                try:
                    response = requests.post(
                        url=self.allExercises, headers=self.headers, json=payload)
                    print(response.json())
                except Exception as e:
                    print(e)
