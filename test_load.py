import pickle
with open("survival_model.pkl", "rb") as file:
    model = pickle.load(file)
