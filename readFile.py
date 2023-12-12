import pickle

with open("urls.data", "rb") as file:
    data = pickle.load(file)
    
for raw in data:
    print(raw)