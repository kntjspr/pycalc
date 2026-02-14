from concurrent.futures import ThreadPoolExecutor
import threading
import random
from employees import employees

def compute_sss(salary):
    thread = threading.current_thread().name
    amount = salary * 0.045
    print(f"[{thread}] SSS computed")
    return amount

def compute_philhealth(salary):
    thread = threading.current_thread().name
    amount = salary * 0.025
    print(f"[{thread}] PhilHealth computed")
    return amount

def compute_pagibig(salary):
    thread = threading.current_thread().name
    amount = salary * 0.02
    print(f"[{thread}] Pag-IBIG computed")
    return amount

def compute_tax(salary):
    thread = threading.current_thread().name
    amount = salary * 0.10
    print(f"[{thread}] Withholding Tax computed")
    return amount

def run_task_parallelism():
    print("\n===== TASK PARALLELISM =====\n")

    name, salary = random.choice(employees)

    print(f"Selected Employee: {name}")
    print(f"Salary: ₱{salary:,.2f}")

    with ThreadPoolExecutor(max_workers=4) as executor:
        f_sss = executor.submit(compute_sss, salary)
        f_ph = executor.submit(compute_philhealth, salary)
        f_pi = executor.submit(compute_pagibig, salary)
        f_tax = executor.submit(compute_tax, salary)

        sss = f_sss.result()
        philhealth = f_ph.result()
        pagibig = f_pi.result()
        tax = f_tax.result()

    total = sss + philhealth + pagibig + tax

    print("\n--- Deductions ---")
    print(f"SSS: ₱{sss:,.2f}")
    print(f"PhilHealth: ₱{philhealth:,.2f}")
    print(f"Pag-IBIG: ₱{pagibig:,.2f}")
    print(f"Withholding Tax: ₱{tax:,.2f}")
    print("----------------------")
    print(f"TOTAL DEDUCTION: ₱{total:,.2f}")
