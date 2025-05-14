from flask import Flask, request, jsonify

app = Flask(__name__)

reservations = []

@app.route("/reserve", methods=["POST"])
def reserve():
    data = request.json
    required_fields = ["name", "id", "age", "priority", "source", "destination"]

    for field in required_fields:
        if field not in data or data[field] == "":
            return jsonify({"message": f"Missing field: {field}"}), 400

    # You can enhance this with duplicate checks, seat limits, etc.
    reservations.append({
        "name": data["name"],
        "id": data["id"],
        "age": data["age"],
        "priority": data["priority"],
        "source": data["source"],
        "destination": data["destination"]
    })

    return jsonify({"message": "Reservation successful!"}), 200
