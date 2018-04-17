import json

path = "data/bitly_usagov.txt"
open(path).readline()

records = [json.loads(line) for line in open(path)]
