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
    input_string = data.get("input", "Apple").lower()  # default to "Apple" and convert to lowercase

    # Determine which folder to use based on input
    if input_string == "cat":
        folder = "cat"
    else:
        folder = "apple"  # default to apple for any other input

    # Dummy response data based on input
    response = {
        "name": input_string.capitalize(),
        "description": f"Learn how to draw a {input_string} in 4 easy steps.",
        "steps": [
            {"stepNumber": 1, "imageUrl": f"/uploads/{folder}/step1.png", "steps": "Draw a rough shape"},
            {"stepNumber": 2, "imageUrl": f"/uploads/{folder}/step2.png", "steps": "Add details"},
            {"stepNumber": 3, "imageUrl": f"/uploads/{folder}/step3.png", "steps": "Refine the outline"},
            {"stepNumber": 4, "imageUrl": f"/uploads/{folder}/step4.png", "steps": "Color it in"},
        ]
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
