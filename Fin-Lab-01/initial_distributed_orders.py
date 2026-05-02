from mpi4py import MPI
from multiprocessing import Manager, Lock
import sys

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if size < 2:
        if rank == 0:
            print("Run with: mpiexec -np 4 python -u distributed_orders.py", flush=True)
        return

    manager = Manager()
    shared_orders = manager.list()
    lock = Lock()

    if rank == 0:
        orders = [
            {"id": 101, "item": "Laptop"}, {"id": 102, "item": "Mouse"},
            {"id": 103, "item": "Keyboard"}, {"id": 104, "item": "Monitor"},
            {"id": 105, "item": "Headset"}, {"id": 106, "item": "Webcam"},
            {"id": 107, "item": "Desk Lamp"}
        ]
        
        print(f"[Master] Distributing {len(orders)} tasks...", flush=True)
        sys.stdout.flush()

        for i, order in enumerate(orders):
            worker_dest = (i % (size - 1)) + 1
            comm.send(order, dest=worker_dest, tag=1)
            print(f"[Master] Sent Order {order['id']} to Worker {worker_dest}", flush=True)
            sys.stdout.flush()

        for w in range(1, size):
            comm.send(None, dest=w, tag=99)
    else:
        while True:
            order = comm.recv(source=0)
            if order is None: 
                break
            
            with lock:
                shared_orders.append(f"Order {order['id']} ({order['item']}) - Done by Rank {rank}")
            
            print(f"[Worker {rank}] Processed Order {order['id']}", flush=True)
            sys.stdout.flush()

    comm.Barrier()

    if rank == 0:
        print("\n" + "="*45, flush=True)
        print("FINAL COMPLETED ORDERS (SHARED MEMORY):", flush=True)
        for entry in list(shared_orders):
            print(f"- {entry}", flush=True)
        print("="*45, flush=True)
        sys.stdout.flush()
        
        manager.shutdown()

if __name__ == "__main__":
    main()