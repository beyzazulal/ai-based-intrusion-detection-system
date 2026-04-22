from flask import Flask, request, jsonify
from pymongo import MongoClient
import os
import traceback
import joblib
import pandas as pd

app = Flask(__name__)

# ===== Config =====
MODEL_PATH = os.environ.get(
    "IDS_MODEL_PATH",
    "final_xgboost_ids.pkl"
)

FEEDBACK_PATH = os.environ.get(
    "IDS_FEEDBACK_PATH",
    "api_feedback.csv"
)

MONGO_URI = os.environ.get(
    "IDS_MONGO_URI",
    "mongodb://localhost:27017/"
)

MONGO_DB_NAME = os.environ.get(
    "IDS_MONGO_DB_NAME",
    "ids_project"
)

MONGO_COLLECTION_NAME = os.environ.get(
    "IDS_MONGO_COLLECTION_NAME",
    "feedback_samples"
)

# ===== MongoDB =====
mongo_client = MongoClient(MONGO_URI)
mongo_db = mongo_client[MONGO_DB_NAME]
mongo_collection = mongo_db[MONGO_COLLECTION_NAME]

# ===== Load model once at startup =====
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")

model = joblib.load(MODEL_PATH)


def save_feedback_record(record: dict, csv_path: str) -> int:
    """Append one feedback record to CSV and return total row count."""
    df_new = pd.DataFrame([record])

    if os.path.exists(csv_path):
        df_old = pd.read_csv(csv_path)
        df_all = pd.concat([df_old, df_new], ignore_index=True)
    else:
        df_all = df_new

    df_all.to_csv(csv_path, index=False)
    return len(df_all)


def save_feedback_to_mongo(record: dict) -> str:
    """Insert one feedback record into MongoDB and return inserted id."""
    result = mongo_collection.insert_one(record)
    return str(result.inserted_id)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "AI-Based IDS API is running",
        "endpoints": ["/health", "/predict", "/feedback"]
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "model_loaded": True,
        "model_path": MODEL_PATH,
        "mongo_db": MONGO_DB_NAME,
        "mongo_collection": MONGO_COLLECTION_NAME
    })


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No JSON body provided"}), 400

        sample = pd.DataFrame([data])

        pred = int(model.predict(sample)[0])
        proba = model.predict_proba(sample)[0]

        result = {
            "prediction": "ATTACK" if pred == 1 else "BENIGN",
            "predicted_label": pred,
            "benign_probability": float(proba[0]),
            "attack_probability": float(proba[1])
        }

        return jsonify(result), 200

    except Exception as e:
        return jsonify({
            "error": str(e),
            "trace": traceback.format_exc()
        }), 500


@app.route("/feedback", methods=["POST"])
def feedback():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No JSON body provided"}), 400

        # CSV'ye kaydet
        total_records = save_feedback_record(data, FEEDBACK_PATH)

        # MongoDB'ye kaydet
        mongo_id = save_feedback_to_mongo(data)

        return jsonify({
            "message": "Feedback saved successfully",
            "total_records_csv": total_records,
            "mongo_inserted_id": mongo_id,
            "feedback_path": FEEDBACK_PATH,
            "mongo_db": MONGO_DB_NAME,
            "mongo_collection": MONGO_COLLECTION_NAME
        }), 200

    except Exception as e:
        return jsonify({
            "error": str(e),
            "trace": traceback.format_exc()
        }), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)