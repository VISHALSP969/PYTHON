persons = ['John', 'Mathew', 'Albert']
print("Hello "+persons[0])
print("Hello "+persons[1])
print("Hello "+persons[2])

print(persons)
print(persons[1])
persons[1]="Michael"
print(persons)
print("Hello "+persons[0])
print("Hello "+persons[1])
print("Hello "+persons[2])

print(persons)
persons.insert(0,'Benson')
print(persons)
persons.insert(2,'Charles')
print(persons)
persons.append('Robert')
print(persons)
print("Hello "+persons[0])
print("Hello "+persons[1])
print("Hello "+persons[2])
print("Hello "+persons[3])
print("Hello "+persons[4])
print("Hello "+persons[5])

print(persons)
persons.pop()
persons.pop()
persons.pop()
persons.pop()
print(persons)

print("Hello "+persons[0])
print("Hello "+persons[1])

print(persons)
del persons[-1]
print(persons)
del persons[-1]
print(persons)
