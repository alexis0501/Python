x = [ [5,2,3], [10,8,9] ]
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

def changeX():
    x[1][0] = 15
changeX()
print(x)

def changeName():
    students[0]['last_name'] = 'Bryant'
changeName()
print(students)

def changeSports():
    sports_directory['soccer'][0] = 'Andres'
changeSports()
print(sports_directory)


def changeY():
    z[0]['y'] = '30'
changeY()
print(z)

def iterateDictionary(some_list):
    for item in some_list:
        for key_name in item:
            print key_name, item[key_name]

iterateDictionary(students)
#3
def iterateDictionary2(key, some_list):
    for dictionary in some_list:
        print(dictionary[key])

iterateDictionary2('last_name', students)
iterateDictionary2('last_name', students)

def printInfo(some_dict):
    for key_name in some_dict:
        one_list = some_dict[key_name]
        print len(one_list), key_name.upper()
        for item in one_list:
            print(item)
        print("")
        

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)