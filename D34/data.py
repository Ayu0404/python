import requests

URL='https://opentdb.com/api.php'
params={
    'amount':30,
    'type':'boolean',
}
response=requests.get(url=URL,params=params)
response.raise_for_status()
question_data=response.json()['results']