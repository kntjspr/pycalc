from concurrent.futures import ProcessPoolExecutor
from employees import employees


def compute_payroll(employee):
    name, salary = employee

    sss = salary * 0.045
    philhealth = salary * 0.025
    pagibig = salary * 0.02
    tax = salary * 0.10

    total_deduction = sss + philhealth + pagibig + tax
    net_salary = salary - total_deduction

    return {
        "name": name,
        "salary": salary,
        "total_deduction": total_deduction,
        "net_salary": net_salary,
    }


def run_data_parallelism():
    print("=== DATA PARALLELISM (ProcessPoolExecutor) ===\n")

    with ProcessPoolExecutor() as executor:
        results = list(executor.map(compute_payroll, employees))

    for r in results:
        print(f"Employee: {r['name']}")
        print(f"Gross Salary: {r['salary']:.2f}")
        print(f"Total Deduction: {r['total_deduction']:.2f}")
        print(f"Net Salary: {r['net_salary']:.2f}")
        print("-" * 30)
