list = [("student1", "A"),("student2", "B"),("student3","A"),("student4","F"),("student5","D"),("student6","B")]
dict={}
dict['A'] = []
dict['B'] = []
dict['C'] = []
dict['D'] = []
dict['F'] = []

while list:
	dict[list[0][1]].append(list.pop(0)[0])

print(dict)
