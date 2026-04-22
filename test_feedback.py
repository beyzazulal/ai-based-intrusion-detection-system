import requests

sample_data = {
    "Destination Port": 53,
    "Flow Duration": 225064,
    "Total Fwd Packets": 1,
    "Total Backward Packets": 1,
    "Total Length of Fwd Packets": 38,
    "Total Length of Bwd Packets": 119,
    "Fwd Packet Length Max": 38,
    "Fwd Packet Length Min": 38,
    "Fwd Packet Length Mean": 38.0,
    "Fwd Packet Length Std": 0.0,
    "Bwd Packet Length Max": 119,
    "Bwd Packet Length Min": 119,
    "Bwd Packet Length Mean": 119.0,
    "Bwd Packet Length Std": 0.0,
    "Flow Bytes/s": 697.5793552,
    "Flow Packets/s": 8.886361213,
    "Flow IAT Mean": 225064.0,
    "Flow IAT Std": 0.0,
    "Flow IAT Max": 225064,
    "Flow IAT Min": 225064,
    "true_label": 0,
    "predicted_label": 0
}

r = requests.post("http://127.0.0.1:5000/feedback", json=sample_data)
print(r.json())