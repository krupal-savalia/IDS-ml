import joblib
import pandas as pd
import numpy as np

model = joblib.load("model/ids_model.pkl")

sample = pd.DataFrame([[
    0, 0, 0, 181, 5450, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 0, 0, 1, 1, 0
]])

prediction = model.predict(sample)
print("Predicted class:", prediction[0])
