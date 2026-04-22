from pymongo import MongoClient
import pandas as pd

client = MongoClient("mongodb://localhost:27017/")
db = client["ids_project"]
collection = db["feedback_samples"]

docs = list(collection.find({}, {"_id": 0}))
df_feedback = pd.DataFrame(docs)

print("Original feedback shape:", df_feedback.shape)

# retraining için sadece feature + true_label kullan
if "predicted_label" in df_feedback.columns:
    df_feedback = df_feedback.drop(columns=["predicted_label"])

print("Retraining-ready feedback shape:", df_feedback.shape)
print(df_feedback.head())