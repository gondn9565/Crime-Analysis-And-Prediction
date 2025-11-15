from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import io

app = Flask(__name__)
CORS(app)

# Store uploaded data temporarily
uploaded_df = pd.DataFrame()

@app.route("/api/upload", methods=["POST"])
def upload_file():
    global uploaded_df
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']
    uploaded_df = pd.read_csv(file)
    return jsonify({
        "message": "File uploaded successfully",
        "rows": len(uploaded_df),
        "columns": list(uploaded_df.columns)
    })

@app.route("/api/stats", methods=["GET"])
def get_stats():
    # Return dummy data for now
    data = {
        "totalCrimes": 1432,
        "totalDelta": "-12% from last month",
        "violentCrimes": 342,
        "violentDelta": "-8% from last month",
        "predictionAccuracy": 94.5,
        "accuracyDelta": "+2.3% improvement",
        "citiesCovered": 24,
        "citiesDelta": "+3 new cities",
        "monthlyTrend": [
            {"name": "Jan", "value": 120},
            {"name": "Feb", "value": 150},
            {"name": "Mar", "value": 130},
            {"name": "Apr", "value": 170},
            {"name": "May", "value": 180},
        ],
        "distributionByType": [
            {"type": "Assault", "value": 120},
            {"type": "Robbery", "value": 80},
            {"type": "Burglary", "value": 60},
            {"type": "Theft", "value": 100},
     ]
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)