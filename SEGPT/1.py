import pickle
with open('id_to_name.txt', 'rb') as f:
    content = pickle.load(f)
print(content)