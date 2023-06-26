import mysql.connector
import csv

# opening the CSV file
with open("employee_data.csv", mode="r") as file:
    # reading the CSV file
    csvFile = csv.reader(file)


def add_employee():
    next(csvFile)  # Skip the header row

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
        e1 = Employee(
            employeeId, email, name, phone, pfId, dateOfJoining, dateOfBirth, department
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

    connection.commit()
