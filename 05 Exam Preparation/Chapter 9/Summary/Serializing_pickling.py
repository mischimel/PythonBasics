import pickle

# Sample object to pickle
data_to_pickle = {'name': 'John', 'age': 30, 'city': 'New York'}

# Open a file for binary writing
with open('serialized_object.pkl', 'wb') as file:
    # Call pickle.dump function to serialize the object and write it to the file
    pickle.dump(data_to_pickle, file)

# Pickling multiple objects to one file
additional_data = [1, 2, 3, 4, 5]
with open('multiple_objects.pkl', 'wb') as file:
    pickle.dump(data_to_pickle, file)
    pickle.dump(additional_data, file)
