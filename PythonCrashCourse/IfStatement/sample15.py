users=['John','Ram','George','Admin','Muhammed']

for name in users:
    if name=='Admin':
        print('Hello Admin, would you like to see a status report?')
    else:
        print('Hello '+name+" thank you for logging in again.")

users=[]
if users:
    users = ['John', 'Ram', 'George', 'Admin', 'Muhammed']
    for name in users:
        if name == 'Admin':
            print('Hello Admin, would you like to see a status report?')
        else:
            print('Hello ' + name + " thank you for logging in again.")
else:
    print("We need to find some users.")

current_users=['Ram','Mohan','George','John','Lewis','Muhammed']
new_users=['George','Mathew','MOHAN']
for name in new_users:
    if name.title() in current_users:
        print(name+' will need to enter a new username')
    else:
        print(name+" is available")

numbers=[1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number==1:
        print("1st")
    elif number==2:
        print("2nd")
    elif number==3:
        print("3rd")
    else:
        print(f"{number}th")
