from data_parallelism import run_data_parallelism
from task_parallelism import run_task_parallelism


def header():
    print("\n" + "=" * 50)
    print(" PAYROLL PARALLEL COMPUTATION DEMONSTRATION ")
    print("=" * 50)


def menu():
    print("\nSelect an option:")
    print("1 - Task Parallelism (Single Employee Deductions)")
    print("2 - Data Parallelism (All Employees Payroll)")
    print("3 - Run Both Demonstrations")
    print("0 - Exit")


def run_choice(choice):
    if choice == "1":
        print("\nRunning Task Parallelism...\n")
        run_task_parallelism()

    elif choice == "2":
        print("\nRunning Data Parallelism...\n")
        run_data_parallelism()

    elif choice == "3":

        print("\nRunning Task Parallelism...\n")
        run_task_parallelism()
        
        print("\nRunning Task Parallelism...\n")
        run_task_parallelism()

        print("\nRunning Data Parallelism...\n")
        run_data_parallelism()

    elif choice == "0":
        print("\nProgram terminated.")
        return False

    else:
        print("\nInvalid selection.")

    return True


def main():
    header()

    running = True
    while running:
        menu()
        choice = input("\nEnter choice: ")
        running = run_choice(choice)


if __name__ == "__main__":
    main()
