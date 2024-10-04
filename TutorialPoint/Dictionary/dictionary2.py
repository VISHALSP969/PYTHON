dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print(dict1['Name'])
# print(dict['Alice'])    #Key Error
# print(dict['Zara'])     # Key Error

print(dict1)

dict1['Age'] = 10
print(dict1)

dict1['Place'] = 'New York'
dict1['School'] = 'DPS School'
print(dict1)

del dict1['Place']
print(dict1)

dict1.clear()
print(dict1)

del dict1
# print(dict1)      # Name Error
