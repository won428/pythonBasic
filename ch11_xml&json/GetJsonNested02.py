import json
filename = 'HumanData02.json'

with open(file=filename, mode='rt', encoding='utf-8') as myfile:
    mystring = myfile.read()
    myjson = json.loads(mystring)

for data in myjson:
    menu = data
    name = myjson[data]['basic']['name']
    origin = myjson[data]['basic']['origin']
    roast = myjson[data]['basic']['roast']
    recipe = myjson[data]['recipe']
    brand = myjson[data]['store']['brand']
    branch = myjson[data]['store']['branch']
    last_brewed = myjson[data]['store']['last_brewed']
    status = myjson[data]['store']['status']
    print(menu, name, origin, roast, recipe, brand, branch, last_brewed, status)
