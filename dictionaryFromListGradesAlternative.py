list = [("student1", "A"),("student2", "B"),("student3","A"),("student4","F"),("student5","D"),("student6","B")]
dict={}
dict['A'] = []
dict['B'] = []
dict['C'] = []
dict['D'] = []
dict['F'] = []

for i in list:
	dict[i[1]].append(i[0])


print(dict)