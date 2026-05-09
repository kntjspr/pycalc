import uuid
import random
import time
import requests

# This URL will be provided by GCP after you deploy the Cloud Run API
API_URL = "https://YOUR_CLOUD_RUN_URL_HERE.a.run.app/vote" 

def generate_vote():
    return {
        "user_id": str(uuid.uuid4()), 
        "poll_id": "poll_final_01",
        "choice": random.choice(["Candidate_A", "Candidate_B", "Candidate_C"]),
        "timestamp": time.time()
    }

def send_vote():
    vote = generate_vote()
    # Fault Tolerance: Retry up to 3 times if the network fails
    for attempt in range(3):
        try:
            response = requests.post(API_URL, json=vote, timeout=5)
            if response.status_code == 200:
                print(f"Vote Success: {vote['user_id']} voted for {vote['choice']}")
                break
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(2)

if __name__ == "__main__":
    print("Edge Node Started. Sending votes every 2 seconds...")
    while True:
        send_vote()
        time.sleep(2)