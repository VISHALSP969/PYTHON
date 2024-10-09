import pickle

# python object to be pickled (serialized)
data = {'name': 'Alice', 'age': 30, 'job': 'engineer'}

# open a file to save the picked data
with open('data.pickle', 'wb') as file:
    # pickle the data and write it to the file
    pickle.dump(data, file)
