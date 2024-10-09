import pickle

# data to pickle
data1 = [1, 2, 3]
data2 = {'name': 'Bob', 'age': 25}

# open a file for writing
with open('multiple_data.pickle','wb') as file:
    pickle.dump(data1,file)
    pickle.dump(data2,file)

# read pickled data
with open('multiple_data.pickle','rb') as file:
    loaded_data1=pickle.load(file)
    loaded_data2=pickle.load(file)

print(loaded_data1)
print(loaded_data2)

