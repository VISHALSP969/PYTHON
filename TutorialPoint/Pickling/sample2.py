import pickle

# open the file to read the pickled data
with open('data.pickle','rb') as file:
    # load the picked data
    loaded_data=pickle.load(file)

print(loaded_data)      # output {'name': 'Alice', 'age': 30, 'job': 'Engineer'}
