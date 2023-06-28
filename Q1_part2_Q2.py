import mysql.connector
import csv
from datetime import datetime
import re
import pandas as pd

connection = mysql.connector.connect(
    host="localhost",
    username="root",
    password="Sara@123",
    database="employee",
)

my_cursor = connection.cursor()


# Get all the employees having their year of joining as 2023 and write all the employees into the csv file.
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


# write_employee_data_in_csv()
# # or


# def write_employee_data_in_csv_using_pandas():
#     my_cursor.execute("SELECT name FROM employeeData WHERE YEAR(dateOfJoining)=2023")
#     employeeData = list()
#     for row in my_cursor:
#         employeeData.append(row)
#     df = pd.DataFrame(employeeData)
#     df.to_csv("Q1_employee_data_pandas.csv")


# write_employee_data_in_csv_using_pandas()


# 2. Create a python script which reads from a csv file and inserts multiple employees data in the database at once.
def add_employee_at_once():
    connection = mysql.connector.connect(
        host="localhost",
        username="root",
        password="Sara@123",
        database="employee",
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

            # Insert employee data into the database
            sql = "INSERT INTO employeeData (employeeId, email, name, phone, pfId, dateOfJoining, dateOfBirth, department) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (
                employeeId,
                email,
                name,
                phone,
                pfId,
                formattedJoiningDate,
                formattedBirthDate,
                department,
            )
            my_cursor.execute(sql, values)
            print("Added employees successfully")

        connection.commit()


add_employee_at_once()
