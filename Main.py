from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# ========= Data Storage (Tables) =========
employees = []
attendances = []
performances = []
leave_records = []
departments = []

# ========= DEPARTMENTS =========
# Create 3 departments
for i in range(3):
    departments.append({
        "id": i + 1,
        "name": fake.job().split()[0] + " Dept",
        "location": fake.city(),
        "manager": fake.name()
    })

# ========= EMPLOYEES =========
# Create 5 employees
for i in range(5):
    emp_id = i + 1
    department = random.choice(departments)

    employee = {
        "id": emp_id,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "hire_date": fake.date_between(start_date='-2y', end_date='-3m'),
        "department_id": department["id"],
        "job_title": fake.job()
    }
    employees.append(employee)

    # ========= ATTENDANCE =========
    for day in range(3):  # Last 3 days
        attendances.append({
            "employee_id": emp_id,
            "date": (datetime.today() - timedelta(days=day)).date(),
            "check_in": fake.time(pattern="%H:%M"),
            "check_out": fake.time(pattern="%H:%M"),
            "status": random.choice(["Present", "Absent", "Late"]),
        })

    # ========= PERFORMANCE =========
    performances.append({
        "employee_id": emp_id,
        "review_date": fake.date_between(start_date='-1y', end_date='today'),
        "reviewer": fake.name(),
        "rating": round(random.uniform(2.5, 5.0), 1),
        "feedback": fake.sentence(nb_words=8),
        "goals_achieved": random.choice(["Yes", "No"]),
    })

    # ========= LEAVE RECORD =========
    leave_records.append({
        "employee_id": emp_id,
        "leave_type": random.choice(["Sick", "Casual", "Paid"]),
        "start_date": fake.date_between(start_date='-2M', end_date='-1M'),
        "end_date": fake.date_between(start_date='-1M', end_date='today'),
        "status": random.choice(["Approved", "Pending", "Rejected"])
    })

# ========= PRINT ALL TABLES =========
from pprint import pprint

print("\n========= Departments =========")
pprint(departments)

print("\n========= Employees =========")
pprint(employees)

print("\n========= Attendance =========")
pprint(attendances)

print("\n========= Performance =========")
pprint(performances)

print("\n========= Leave Records =========")
pprint(leave_records)
