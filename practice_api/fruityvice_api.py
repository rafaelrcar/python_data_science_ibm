import requests
import json
import pandas as pd

data = requests.get("https://fruityvice.com/api/fruit/all")
results = json.loads(data.text)

pd.DataFrame(results)

df = pd.json_normalize(results)
#print(df)

cherry = df.loc[df["name"] == 'Cherry']
print('name: ' + (cherry.iloc[0]['name']) + ', family: ' + (cherry.iloc[0]['family']) + ', genus: ' + (cherry.iloc[0]['genus']))

banana = df.loc[df["name"] == 'Banana']
print('name: ' + (banana.iloc[0]['name']) + ', calories: ' + str(banana.iloc[0]['nutritions.calories']))
