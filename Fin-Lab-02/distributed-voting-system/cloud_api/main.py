import os
import json
from flask import Flask, request, jsonify
from google.cloud import pubsub_v1

app = Flask(__name__)

# REPLACE with your friend's Project ID and YOUR unique Topic name
PROJECT_ID = "friend-project-id" 
TOPIC_ID = "group02-vote-topic" 

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

@app.route("/vote", methods=["POST"])
def receive_vote():
    vote_data = request.get_json()
    
    # Validation (Required by Lab)
    if not vote_data or "user_id" not in vote_data:
        return jsonify({"error": "Invalid Data"}), 400

    try:
        # Publish to Pub/Sub (Asynchronous)
        message_bytes = json.dumps(vote_data).encode("utf-8")
        publisher.publish(topic_path, data=message_bytes)
        return jsonify({"status": "Accepted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))