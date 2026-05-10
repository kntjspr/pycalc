# Distributed Voting System

## System Overview & Architecture
This project implements a decoupled, event-driven voting system designed for high availability and fault tolerance. The architecture separates the ingestion of data from the processing logic to ensure that a surge in votes does not crash the database or the user-facing API.

### Architecture Diagram


### Data Flow:
1. **Edge Node (Producer):** A Python script simulates distributed voters sending POST requests.
2. **Cloud Run API (Ingestion):** A Flask-based API receives the vote and immediately pushes it to a Pub/Sub topic (Redis Queue).
3. **Pub/Sub (Message Broker):** Acts as a buffer, holding votes in a "first-in, first-out" (FIFO) queue.
4. **Worker Service (Consumer):** A background process that pulls messages from the queue and performs the database write.
5. **Firestore (Persistence):** The final storage layer where votes are recorded using an idempotent key (`user_id + poll_id`).

### Architecture Diagram

```mermaid
graph LR
    subgraph Edge_Environment [Edge Environment]
        A[Edge Node: Laptop Script]
    end

    subgraph Cloud_Ingestion [Cloud Ingestion]
        B[Cloud Run API: Flask]
    end

    subgraph Messaging_Layer [Messaging Layer]
        C[(Pub/Sub: Redis Queue)]
    end

    subgraph Processing_Layer [Processing Layer]
        D[Worker Service: Consumer]
    end

    subgraph Persistence_Layer [Persistence Layer]
        E[(Firestore: MongoDB Atlas)]
    end

    A -- HTTP POST JSON --> B
    B -- lpush (Messaging) --> C
    C -- brpop (Buffering) --> D
    D -- insert_one (Persistence) --> E

    style C fill:#f9f,stroke:#333,stroke-width:2px
    style E fill:#bbf,stroke:#333,stroke-width:2px


## Setup and Execution Instructions

### 1. Database Setup (Firestore/MongoDB)
* Create a cluster and a database named `voting_db`.
* Add `0.0.0.0/0` to the Network Access to allow cloud services to connect.
* Create a database user and save the credentials.

### 2. Messaging Layer (Pub/Sub/Redis)
* Provision a Redis instance.
* Copy the connection URL (`rediss://...`) for the API and Worker.

### 3. API Deployment (Cloud Run)
* Set the root directory to `cloud_api`.
* Use the command `gunicorn main:app`.
* Deploy and copy the provided public URL.

### 4. Worker Deployment
* Set the root directory to `worker_service`.
* Ensure the background thread logic is enabled to process the queue asynchronously.
* Use the command `gunicorn main:app`.

### 5. Running the Edge Node
* Update `edge_script.py` with your Cloud Run API URL.
* Run `python edge_script.py` to begin the simulation.


## Individual Reflections

- [BONIEL.md](docs/Boniel.md)
- [LERIO.md](docs/LERIO.md)
- [SISI.md](docs/SISI.md)
- [SORONGON.md](docs/SORONGON.md)

## Proof:
