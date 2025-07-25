from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)

@app.route("/get-images", methods=["POST"])
def get_images():
    data = request.get_json()
    input_string = data.get("input", "Apple")  # default to "Apple"

    # Dummy response data based on input
    response = {
        "name": input_string,
        "description": f"Learn how to draw a {input_string.lower()} in 4 easy steps.",
        "steps": [
            {"stepNumber": 1, "imageUrl": "/uploads/step1.png", "steps": "Draw a rough shape"},
            {"stepNumber": 2, "imageUrl": "/uploads/step2.png", "steps": "Add details"},
            {"stepNumber": 3, "imageUrl": "/uploads/step3.png", "steps": "Refine the outline"},
            {"stepNumber": 4, "imageUrl": "/uploads/step4.png", "steps": "Color it in"},
        ]
    }

    # print(jsonify(response))
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
