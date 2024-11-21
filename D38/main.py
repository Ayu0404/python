from apis import restApi

apis = restApi()

exercises = input('Enter the exercises you did ')
apis.enterExercises(exercises)
