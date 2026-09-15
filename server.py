from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# A list called 'events' with a couple of sample event dictionaries
# (Each dictionary should have an 'id' and a 'title')
events = [
    {"id": 1, "title": "Yoga in the Park"},
    {"id": 2, "title": "Lake 5K Run"}
]


# A route for "/"
# (This route should return a JSON welcome message)
@app.route("/", methods=["GET"])
def welcome():
    return jsonify({"message": "Welcome!"}), 200


# A GET route for "/events"
# (This route should return the full list of events as JSON)
@app.route("/events", methods=["GET"])
def get_events():
    return jsonify(events), 200


# A POST route for "/events"
# (This route should:
# 1. Get the JSON data from the request
# 2. Validate that "title" is provided
@app.route("/events", methods=["POST"])
def add_event():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400
# 3. Create a new event with a unique ID and the provided title
    new_id = max((e["id"] for e in events), default=0) + 1
    new_event = {"id": new_id, "title": data["title"]}
# 4. Add the new event to the events list
    events.append(new_event)
# 5. Return the new event with status code 201)
    return jsonify(new_event), 201


if __name__ == "__main__":
    app.run(debug=True)
