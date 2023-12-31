import pickle

# Open a file for binary reading
with open('serialized_object.pkl', 'rb') as file:
    # Call pickle.load function to deserialize the object from the file
    deserialized_object = pickle.load(file)
    print(deserialized_object)

# Unpickling multiple objects from one file
with open('multiple_objects.pkl', 'rb') as file:
    # Deserialize the first object
    deserialized_object1 = pickle.load(file)
    print(deserialized_object1)

    # Deserialize the second object
    deserialized_object2 = pickle.load(file)
    print(deserialized_object2)
