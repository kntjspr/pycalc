from mpi4py import MPI
from threading import Lock
import time
import random
import sys

ITEMS = [
    "Laptop", "Keyboard", "Monitor", "Mouse", "Headphones",
    "Webcam", "USB Hub", "SSD Drive", "RAM Stick", "Desk Lamp"
]


def master_process(comm, size):
    shared_orders = []
    lock = Lock()

    print("\n" + "=" * 60)
    print("   DISTRIBUTED ORDER PROCESSING SYSTEM")
    print("   Master: Process 0  |  Workers: {}".format(size - 1))
    print("=" * 60)

    num_orders = random.randint(5, 8)
    orders = [
        {"order_id": "ORD-{}".format(1000 + i), "item": random.choice(ITEMS)}
        for i in range(num_orders)
    ]

    print("\n[Master] Generated {} orders:".format(num_orders))
    for o in orders:
        print("         {}  ->  {}".format(o["order_id"], o["item"]))

    worker_assignments = {w: [] for w in range(1, size)}
    for idx, order in enumerate(orders):
        target = (idx % (size - 1)) + 1
        worker_assignments[target].append(order)

    print("\n[Master] Distributing orders to {} worker(s)...".format(size - 1))
    for w, assigned in worker_assignments.items():
        comm.send(assigned, dest=w, tag=1)
        print("         -> Sent {} order(s) to Worker {}".format(len(assigned), w))

    print("\n[Master] Waiting for workers to return results...\n")
    for w in range(1, size):
        results = comm.recv(source=w, tag=2)
        print("[Master] Received {} result(s) from Worker {}".format(len(results), w))

        for result in results:
            with lock:
                shared_orders.append(result)
                print("         [Lock] Written -> {}  ({})".format(
                    result["order_id"], result["item"]
                ))

    print("\n" + "=" * 60)
    print("   FINAL COMPLETED ORDERS  (Collected by Master)")
    print("=" * 60)
    for entry in shared_orders:
        print("   [DONE]  {}  |  {:<14}  |  Worker {}  |  {:.2f}s".format(
            entry["order_id"], entry["item"], entry["worker"], entry["duration"]
        ))
    print("\n   Total completed: {} / {}".format(len(shared_orders), num_orders))
    print("=" * 60 + "\n")


def worker_process(comm, rank):
    orders = comm.recv(source=0, tag=1)

    print("[Worker {}] Received {} order(s): {}".format(
        rank, len(orders), [o["order_id"] for o in orders]
    ))

    results = []
    for order in orders:
        delay = random.uniform(0.5, 2.0)
        print("[Worker {}] Processing {}  ({})  --  {:.2f}s ...".format(
            rank, order["order_id"], order["item"], delay
        ))

        time.sleep(delay)

        results.append({
            "order_id": order["order_id"],
            "item":     order["item"],
            "worker":   rank,
            "duration": delay,
        })
        print("[Worker {}] [OK] {} done.".format(rank, order["order_id"]))

    comm.send(results, dest=0, tag=2)
    print("[Worker {}] Results sent to master.".format(rank))


if __name__ == '__main__':
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if size < 2:
        print("[ERROR] Run with at least 2 processes.")
        print("        mpiexec -np 4 python distributed_orders.py")
        sys.exit(1)

    if rank == 0:
        master_process(comm, size)
    else:
        worker_process(comm, rank)