# Dictionary Comprehension - 
# Creating a new dictionary - {key:value for item in dict if test}
# Using an existing dictionary - {key:value for (key,value) in dict.items() if test}

sentence='The quick brown fox jumped over the lazy dog'
inspection={word:len(word) for word in sentence.split()}
# print(inspection)

weather_c = {
    'Monday':22,
    'Tuesday':20,
    'Wednesday':29,
    'Thursday':24,
    'Friday':29,
    'Saturday':23,
    'Sunday':20
}

weather_f={day:temp*9/5 for (day,temp) in weather_c.items()}
print(weather_f)
