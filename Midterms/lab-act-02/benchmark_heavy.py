"""
heavy benchmark for multiprocessing vs multithreading.
tests with 1000 grades to show scaling behavior.
"""
import subprocess
import os
import sys
import time

# 1000 grades, all 1.5 because why not
NUM_GRADES = 1000
INPUT_STR = f"{NUM_GRADES}\n" + "1.5\n" * NUM_GRADES

def run_test(filename):
    """runs the script and retrieves the execution time."""
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    
    if not os.path.exists(script_path):
        print(f"file missing: {filename}")
        return None

    try:
        start = time.time()
        proc = subprocess.run(
            [sys.executable, script_path],
            input=INPUT_STR,
            text=True,
            capture_output=True,
            timeout=120  # 2 min timeout, spawning 1000 processes takes a while
        )
        wall_time = time.time() - start
        
        output = proc.stdout
        # parse the script's reported time
        for line in output.split("\n"):
            if "Execution Time" in line:
                parts = line.split(":")
                reported_time = float(parts[-1].strip())
                return reported_time, wall_time
                
        return None, wall_time
    except subprocess.TimeoutExpired:
        print(f"{filename} timed out after 120s")
        return None, None
    except Exception as e:
        print(f"crashed while testing {filename}: {e}")
        return None, None

if __name__ == "__main__":
    print(f"heavy benchmark: {NUM_GRADES} grades")
    print("this might take a bit...\n")
    
    mp_reported, mp_wall = run_test("multiprocessing_gwa.py")
    mt_reported, mt_wall = run_test("multithreading.py")
    
    if mp_reported is not None and mt_reported is not None:
        print("="*50)
        print(f"{'Technique':<20} | {'Reported (s)':<12} | {'Wall (s)':<10}")
        print("-" * 50)
        print(f"{'Multiprocessing':<20} | {mp_reported:<12.6f} | {mp_wall:<10.4f}")
        print(f"{'Multithreading':<20} | {mt_reported:<12.6f} | {mt_wall:<10.4f}")
        print("="*50)
        
        diff = abs(mp_reported - mt_reported)
        if mp_reported < mt_reported:
            print(f"\nmultiprocessing wins (faster by {diff:.6f}s)")
        else:
            print(f"\nmultithreading wins (faster by {diff:.6f}s)")
            
        print(f"\nnote: wall time includes process spawn overhead")
    else:
        print("\nsomething broke. check your files or increase timeout.")
