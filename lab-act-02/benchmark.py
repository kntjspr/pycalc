import subprocess
import os
import sys

# standardized inputs so the playing field is level
# 5 subjects, passing grades.
INPUT_STR = "5\n1.0\n1.25\n1.5\n1.75\n2.0\n"

def run_test(filename):
    """runs the script and retrieves the execution time."""
    script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    
    if not os.path.exists(script_path):
        print(f"file missing: {filename}")
        return None

    try:
        # running the script via subprocess
        # capturing stdout to parse the time
        proc = subprocess.run(
            [sys.executable, script_path],
            input=INPUT_STR,
            text=True,
            capture_output=True
        )
        
        output = proc.stdout
        # basic parsing logic based on expected output format
        for line in output.split("\n"):
            if "Execution Time" in line:
                # expecting "multiprocessing execution time: 0.123"
                parts = line.split(":")
                return float(parts[-1].strip())
                
        return None
    except Exception as e:
        print(f"crashed while testing {filename}: {e}")
        return None

if __name__ == "__main__":
    print("starting benchmark...")
    
    t_mp = run_test("multiprocessing_gwa.py")
    t_mt = run_test("multithreading.py")
    
    if t_mp is not None and t_mt is not None:
        print("\n" + "="*35)
        print(f"{'Technique':<20} | {'Time (s)':<10}")
        print("-" * 35)
        print(f"{'Multiprocessing':<20} | {t_mp:.6f}")
        print(f"{'Multithreading':<20} | {t_mt:.6f}")
        print("="*35)
        
        diff = abs(t_mp - t_mt)
        if t_mp < t_mt:
            print(f"\nmultiprocessing wins (faster by {diff:.6f}s)")
        else:
            print(f"\nmultithreading wins (faster by {diff:.6f}s)")
    else:
        print("\nsomething went wrong. check your files.")
