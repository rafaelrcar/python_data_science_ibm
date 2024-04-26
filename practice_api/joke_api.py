import requests
import json
import pandas as pd

data = requests.get("https://official-joke-api.appspot.com/jokes/ten")
results = json.loads(data.text)

df = pd.DataFrame(results)
df.drop(columns=["type","id"],inplace=True)

df.to_csv('./Jokes.csv')