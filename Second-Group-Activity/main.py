import time
import threading
from concurrent.futures import ThreadPoolExecutor

# Lock to simulate a single shared printer (critical section)
printer_lock = threading.Lock()

# Simulate printing a document
def print_document(doc):
    with printer_lock:  # Only one thread can print at a time
        time.sleep(0.5)  # simulate printing delay
        print(f"{doc} printed")  # simulate printing output
    return f"{doc} printed"

# Sequential execution (baseline)
def sequential_execution(documents):
    start = time.time()
    
    for doc in documents:
        print_document(doc)
    
    end = time.time()
    return end - start

# Parallel execution with data parallelism
def parallel_execution(documents, workers=4):
    start = time.time()
    
    with ThreadPoolExecutor(max_workers=workers) as executor:
        list(executor.map(print_document, documents))
    
    end = time.time()
    return end - start

def main():
    documents = [f"Document_{i}" for i in range(20)]
    
    print("Running Sequential Version...")
    seq_time = sequential_execution(documents)
    
    print("\nRunning Parallel Version...")
    par_time = parallel_execution(documents, workers=4)
    
    speedup = seq_time / par_time
    
    print("\n===== BENCHMARK REPORT =====")
    print(f"Total Documents: {len(documents)}")
    print(f"Sequential Time: {seq_time:.2f} seconds")
    print(f"Parallel Time: {par_time:.2f} seconds")
    print(f"Speedup: {speedup:.2f}x faster")
    
    # Simple Scaling Analysis
    ideal_speedup = 4  # number of workers
    efficiency = (speedup / ideal_speedup) * 100
    
    print(f"Parallel Efficiency: {efficiency:.2f}%")
    
    if speedup < ideal_speedup:
        print("\nExplanation:")
        print("Speedup is not perfectly linear due to thread overhead,")
        print("synchronization costs from the printer lock,")
        print("and shared resource limitations.")

if __name__ == "__main__":
    main()