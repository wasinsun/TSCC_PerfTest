import json

with open('InterdayWSConfig.json', 'r') as myfile:
    data=myfile.read()

# parse file
obj = json.loads(data)

print (str(obj['parameters']['interval']))