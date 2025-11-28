import json

filename = 'HumanData01.json'

with open(file=filename, mode= 'rt', encoding='utf-8') as myfile:
    mystring = myfile.read()
    jsondata = json.loads(mystring)

print(f'원본 JSON 타입 : {type(jsondata)}')
print(f'요소 갯수 : {len(jsondata)}')

humanList = list()

for data in jsondata:
    name = jsondata[data]['name']
    age = jsondata[data]['age']
    street = jsondata[data]['location']['address']['street']
    city = jsondata[data]['location']['address']['city']
    gu = jsondata[data]['location']['address']['gu']
    address = city + gu + city
    mobile = jsondata[data]['contact']['mobile']
    email = jsondata[data]['contact']['email']
    job = jsondata[data]['job']['title']
    companyName = jsondata[data]['job']['company']['name']
    companyLocation = jsondata[data]['job']['company']['location']
    skills = jsondata[data]['skills']
    mytuple = (name, age, address, mobile, email, job, companyName, companyLocation, skills )
    humanList.append(mytuple)

print(humanList)
