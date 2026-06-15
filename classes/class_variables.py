class Employee:
    """Сотрудник компании."""

    company = "TechCorp"
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def info(self):
        print(f"{self.name} works at {Employee.company}, salary {self.salary}")


if __name__ == "__main__":
    e1 = Employee("Anna", 5000)
    e2 = Employee("Boris", 6000)

    e1.info()
    e2.info()

    print("Company (e1):", e1.company)
    print("Company (e2):", e2.company)
    print("Total employees:", Employee.employee_count)

    Employee.company = "NewTechCorp"
    print("After change, e1.company:", e1.company)
    print("After change, e2.company:", e2.company)

    e1.salary = 9999
    print("e1 salary:", e1.salary)
    print("e2 salary:", e2.salary)
