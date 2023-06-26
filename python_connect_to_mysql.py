import mysql.connector
import csv
from datetime import datetime
import re
import pandas as pd

connection = mysql.connector.connect(
    host="localhost",
    username="root",
    password="[your_password]",
    database="[your_db_name]",
)

my_cursor = connection.cursor()

connection.commit()

print("Connected!")


class Employee:
    def __init__(
        self,
        employeeId,
        email,
        name,
        phone,
        pfId,
        dateOfJoining,
        dateOfBirth,
        department,
    ):
        self.employeeId = employeeId
        if Employee.validateEmail(email):
            self.email = email
        self.name = name
        if Employee.validatePhone(phone):
            self.phone = phone
        self.pfId = pfId
        self.dateOfJoining = dateOfJoining
        self.dateOfBirth = dateOfBirth
        self.department = department

    def add_employee():
        while True:
            add = input("Add an employee? (y/n): ")
            if add == "n":
                break
            employeeId = input("enter employee id: ")
            email = input("enter employee email: ")
            while not Employee.validateEmail(email):
                email = input("enter valid employee email: ")
            name = input("enter employee name: ")
            phone = input("enter employee phone: ")
            while not Employee.validatePhone(phone):
                email = input("enter valid employee phone: ")
            pfId = input("enter employee pfId: ")
            dateOfJoining = input("enter employee joing date(yy-mm-dd): ")
            dateOfBirth = input("enter employee birth date(yy-mm-dd): ")
            department = input("enter department: ")
            e1 = Employee(
                employeeId,
                email,
                name,
                phone,
                pfId,
                dateOfJoining,
                dateOfBirth,
                department,
            )
            sql = "INSERT INTO employeeData (employeeId, email, name, phone, pfId, dateOfJoining, dateOfBirth, department) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (
                e1.employeeId,
                e1.email,
                e1.name,
                e1.phone,
                e1.pfId,
                e1.dateOfJoining,
                e1.dateOfBirth,
                e1.department,
            )
            my_cursor.execute(sql, values)
            print("Added employees successfully")
            connection.commit()

    def read_employee():
        my_cursor.execute("SELECT * FROM employeeData")
        employeeList = list()
        for row in my_cursor:
            # print(row)
            employeeList.append(row)
        df = pd.DataFrame(employeeList)
        print(df)

    def update_employee():
        fieldToChange = input("Change which column? ")
        value = input("Input changed value: ")

        if fieldToChange == "email":
            if Employee.validateEmail(value):
                print("valid email")
            else:
                print("Invalid email")

        if fieldToChange == "phone":
            if Employee.validatePhone(value):
                print("valid phone no.")
            else:
                print("Invalid phone no.")

        employeeId = input("Input employee id: ")
        sql = "UPDATE employeeData SET `{}` = %s WHERE employeeId = %s".format(
            fieldToChange
        )

        # Execute the SQL statement with the provided values
        values = (value, employeeId)
        my_cursor.execute(sql, values)

        my_cursor.execute(sql, values)
        connection.commit()
        print("Data updated!")

    # Apply validations for emp_id. It should be unique and a number.
    # Apply validation for email. It should be a valid email address.
    # Apply validation on the phone number as it should be of at least 10 digits and a number.

    @staticmethod
    def validateEmail(email):
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if re.match(pattern, email):
            print("valid email!")
            return True
        else:
            print("Invalid email format. Please enter a valid email.")
            return False

    @staticmethod
    def validatePhone(phone):
        pattern = r"^\d{10}$"
        if re.match(pattern, phone):
            print("valid phone!")
            return True
        else:
            print("Invalid phone number format. Please enter a 10-digit phone number.")
            return False


# Get all the employees having their year of joining as 2021 and write all the employees into the csv file.
def write_employee_data_in_csv():
    my_cursor.execute("SELECT name FROM employeeData WHERE YEAR(dateOfJoining)=2023")

    with open("Q1.csv", mode="w", newline="") as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(["Names of Employees Joined in 2023"])

        # Write the employee data rows
        for row in my_cursor:
            writer.writerow(row)

    connection.close()
    print("Employee data for employees joined in 2022 has been written to Q1.csv.")


# or


def write_employee_data_in_csv_using_pandas():
    my_cursor.execute("SELECT name FROM employeeData WHERE YEAR(dateOfJoining)=2023")
    employeeData = list()
    for row in my_cursor:
        employeeData.append(row)
    df = pd.DataFrame(employeeData)
    df.to_csv("Q1_employee_data_pandas.csv")


# write_employee_data_in_csv_using_pandas()


# 2. Create a python script which reads from a csv file and inserts multiple employees data in the database at once.
def add_employee_at_once():
    connection = mysql.connector.connect(
        host="localhost",
        username="root",
        password="[your_password]",
        database="[your_db_name]",
    )
    my_cursor = connection.cursor()
    print("Connected2!")

    with open("employee_data.csv", mode="r") as file:
        csvFile = csv.reader(file)
        next(csvFile)

        for row in csvFile:
            (
                employeeId,
                email,
                name,
                phone,
                pfId,
                dateOfJoining,
                dateOfBirth,
                department,
            ) = row

            joiningDate = dateOfJoining
            joiningDateObject = datetime.strptime(joiningDate, "%m/%d/%Y")
            birthDate = dateOfBirth
            birthDateObject = datetime.strptime(birthDate, "%m/%d/%Y")
            formattedJoiningDate = joiningDateObject.strftime("%Y-%m-%d")
            formattedBirthDate = birthDateObject.strftime("%Y-%m-%d")

            e1 = Employee(
                employeeId,
                email,
                name,
                phone,
                pfId,
                formattedJoiningDate,
                formattedBirthDate,
                department,
            )

            # Insert employee data into the database
            sql = "INSERT INTO employeeData (employeeId, email, name, phone, pfId, dateOfJoining, dateOfBirth, department) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (
                e1.employeeId,
                e1.email,
                e1.name,
                e1.phone,
                e1.pfId,
                e1.dateOfJoining,
                e1.dateOfBirth,
                e1.department,
            )
            my_cursor.execute(sql, values)
            print("Added employees successfully")

        connection.commit()


# def add_employee_at_once_using_pandas():
#     connection = mysql.connector.connect(
#         host="localhost",
#         username="root",
#         password="Sara@123",
#         database="employee_pandas",
#     )
#     my_cursor = connection.cursor()
#     df = pd.read_csv("employee_data.csv", skiprows=[0])
#     df2 = df.to_string(index=False)
#     print("Connected2!", df.to_string(index=False))

#     for row in df2:
#         (
#             employeeId,
#             email,
#             name,
#             phone,
#             pfId,
#             dateOfJoining,
#             dateOfBirth,
#             department,
#         ) = row

#         joiningDate = dateOfJoining
#         joiningDateObject = datetime.strptime(joiningDate, "%m/%d/%Y")
#         birthDate = dateOfBirth
#         birthDateObject = datetime.strptime(birthDate, "%m/%d/%Y")
#         formattedJoiningDate = joiningDateObject.strftime("%Y-%m-%d")
#         formattedBirthDate = birthDateObject.strftime("%Y-%m-%d")

#         e1 = Employee(
#             employeeId,
#             email,
#             name,
#             phone,
#             pfId,
#             formattedJoiningDate,
#             formattedBirthDate,
#             department,
#         )
#         print(e1, "ok")

#         # Insert employee data into the database
#         sql = "INSERT INTO employeeData (employeeId, email, name, phone, pfId, dateOfJoining, dateOfBirth, department) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
#         values = (
#             e1.employeeId,
#             e1.email,
#             e1.name,
#             e1.phone,
#             e1.pfId,
#             e1.dateOfJoining,
#             e1.dateOfBirth,
#             e1.department,
#         )
#         my_cursor.execute(sql, values)
#         print("Added employees successfully")

#     connection.commit()


# update_employee()
add_employee_at_once()
# Employee.add_employee()
# Employee.read_employee()
Employee.update_employee()
connection.close()
