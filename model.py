from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pickle

# dummy data (5 features same as app)
X = np.random.rand(200, 5)
y = np.random.randint(0, 2, 200)

model = RandomForestClassifier()
model.fit(X, y)

# IMPORTANT: binary mode
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ NEW model.pkl created successfully")
