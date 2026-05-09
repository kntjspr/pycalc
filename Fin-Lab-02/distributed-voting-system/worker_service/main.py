import json
from google.cloud import pubsub_v1, firestore

# REPLACE with your friend's Project ID and YOUR unique Subscription name
PROJECT_ID = "friend-project-id"
SUBSCRIPTION_ID = "group02-vote-sub"

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(PROJECT_ID, SUBSCRIPTION_ID)
db = firestore.Client()

def callback(message):
    try:
        data = json.loads(message.data.decode("utf-8"))
        
        # IDEMPOTENCY: Use user_id + poll_id as the document name
        # This prevents the same person from voting twice if a message is retried
        doc_name = f"{data['user_id']}_{data['poll_id']}"
        
        # Save to a unique collection for your group
        db.collection("group02-votes").document(doc_name).set(data)
        
        print(f"Processed & Saved: {doc_name}")
        message.ack() # Tell Pub/Sub the message is done
    except Exception as e:
        print(f"Error processing: {e}")

if __name__ == "__main__":
    print("Worker listening for votes...")
    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    try:
        streaming_pull_future.result()
    except KeyboardInterrupt:
        streaming_pull_future.cancel()