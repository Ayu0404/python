import pandas

data=pandas.read_csv('D25/2018_CEntral_Park_Squirrel_Census.csv')

grey=len(data[data['Primary Fur Color']=='Gray'])
black=len(data[data['Primary Fur Color']=='Black'])
cinnamon=len(data[data['Primary Fur Color']=='Cinnamon'])

consolidated_squirrel_colors={
    'Fur Color':['Grey','Cinnamon','Black'],
    'count':[grey,cinnamon,black]    
}

df=pandas.DataFrame.from_dict(consolidated_squirrel_colors)
df.to_csv('squirrel_summary')
