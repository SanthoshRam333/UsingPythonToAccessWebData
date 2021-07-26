#JSON - JavaScript Object Notation
#JSON represents data as nested "lists" and "dictionaries"

#Example -1
import json
data = '''{
"name" : "Chuck",
"phone" : {
    "type" : "intl",
    "number" : "+1 632 373 2171"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
print('Number:', info["phone"]["number"])

#Example -2
import json
input = '''[
    {   "id" : "001",
        "x : "2",
        "name" : "Chuck"
    } ,
    {   "id" : "009",
        "x : "7",
        "name" : "Bret"
    }
]'''

info = json.loads(input)
print('User Count:', len(info))
for item in info:
    print('Name:', item['name'])
    print('Id:', item['id'])
    print('Attr:', item['x'])
