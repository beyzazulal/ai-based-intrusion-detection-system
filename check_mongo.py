from pymongo import MongoClient

# Mongo bağlantısı
client = MongoClient("mongodb://localhost:27017/")

# Database ve collection
db = client["ids_project"]
collection = db["feedback_samples"]

# kayıt sayısını göster
count = collection.count_documents({})
print("Toplam kayıt:", count)

print("\nKayıtlar:\n")

# ilk 5 kaydı göster
for doc in collection.find().limit(5):
    print(doc)