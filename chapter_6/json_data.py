import pandas as pd
import numpy as np
import json

obj = """
{"name": "Wes",
"places_lived": ["United States", "Spain", "Germany"],
"pet": null,
"siblings": [{"name": "Scott", "age": 30, "pets": ["Zeus", "Zuko"]},
{"name": "Katie", "age": 38,
"pets": ["Sixes", "Stache", "Cisco"]}]
}
"""
print(obj)
result = json.loads(obj)
print(result)
asjson = json.dumps(result)
print(asjson)

print(result['siblings'])
siblings = pd.DataFrame(result['siblings'], columns=['name', 'age'])
print(siblings)

data = pd.read_json('chapter_6/ex7.json')
print(data)
print(data.to_json())
print(data.to_json(orient='records'))