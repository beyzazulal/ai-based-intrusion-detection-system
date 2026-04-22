from pymongo import MongoClient
import pandas as pd

client = MongoClient("mongodb://localhost:27017/")
db = client["ids_project"]
collection = db["feedback_samples"]

docs = list(collection.find({}, {"_id": 0}))
df_feedback = pd.DataFrame(docs)

print("Feedback dataframe shape:", df_feedback.shape)
print(df_feedback.head())