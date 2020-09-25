import json

'''jString = '{"name":"Felix", "age": 20, "city": "Toronto"}'

data = json.loads(jString)


print(data["name"])


jstr = '{"name":{"firstName":"Julius","lastname":"Caesar"},"address":{"city":"Toronto","province":"ON"}}'

data2 = json.loads(jstr)

print(data2["name"]["firstName"])


str = '[{"name":{"firstName":"Cleopatra", "lastName":"Ptolemy"}, "address":{"city":"Alexandria", "province":"Egypt"}}, {"name":{"firstName":"Marc", "lastName":"Antony"}, "address":{"city":"Rome", "province":"Italia"}}]'

data3 = json.loads(str)

print(data3[0]["name"]["lastName"])'''



inData = '{"quiz": {"sport": {"q1": {"question": "Which one is a correct team name in NBA?","options": ["New York Bulls","Los Angeles Kings","Golden State Warriros","Houston Rocket"],"answer": "Houston Rocket"}},"maths": {"q1": {"question": "5 + 7 = ?","options": ["10","11","12","13"],"answer": "12"},"q2": {"question": "12 - 8 = ?","options": ["1","2","3","4"],"answer": "4"}}}}'

jsonFormat = json.loads(inData)

print(jsonFormat)


for j in jsonFormat["quiz"]["sport"]:
    print(j)
