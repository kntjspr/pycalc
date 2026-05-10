import uuid
import random
import time
import requests

# Replace with the URL Render gives you after deploying the API
API_URL = "https://my-voting-api.onrender.com/vote"

def generate_vote():
    """Generates unique vote data for a distributed source[cite: 71, 74]."""
    return {
        "user_id": str(uuid.uuid4()), 
        "poll_id": "poll_final_exam",
        "choice": random.choice(["Candidate_A", "Candidate_B", "Candidate_C"]),
        "timestamp": time.time()
    }

def send_vote():
    """Sends vote to the cloud with retry logic for fault tolerance[cite: 88, 90]."""
    vote = generate_vote()
    # Fault Tolerance: Retry loop to handle network instability [cite: 20, 91]
    for attempt in range(3):
        try:
            response = requests.post(API_URL, json=vote, timeout=5)
            if response.status_code == 200:
                print(f"Vote Success: {vote['user_id']} voted {vote['choice']}")
                break
        except Exception as e:
            print(f"Attempt {attempt + 1} failed (Network Latency/Failure): {e}")
            time.sleep(2) # Wait before retrying [cite: 3]

if __name__ == "__main__":
    print("Edge Node Active. Simulating distributed data generation... ")
    while True:
        send_vote()
        # Random delay (1-3s) to simulate variable edge behavior [cite: 106]
        time.sleep(random.uniform(1, 3))