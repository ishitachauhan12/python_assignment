import mysql.connector
import re
import pandas as pd


class Employee:
    def setter_function(
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
        if self.validate_email(email):
            self.email = email
        self.name = name
        if self.validate_phone(phone):
            self.phone = phone
        self.pfId = pfId
        self.dateOfJoining = dateOfJoining
        self.dateOfBirth = dateOfBirth
        self.department = department

    def connect(self):
        connection = mysql.connector.connect(
            host="localhost",
            username="root",
            password="Sara@123",
            database="employee",
        )

        print("Connected!")
        return connection

    def commit_and_disconnect(self, connection):
        connection.commit()
        connection.close()
        print("disconnected")

    def validate_email(self, email):
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if re.match(pattern, email):
            print("valid email!")
            return True
        else:
            print("Invalid email format. Please enter a valid email.")
            return False

    def validate_phone(self, phone):
        pattern = r"^\d{10}$"
        if re.match(pattern, phone):
            print("valid phone!")
            return True
        else:
            print("Invalid phone number format. Please enter a 10-digit phone number.")
            return False

    def create_table(self):
        connection = self.connect()
        my_cursor = connection.cursor()
        my_cursor.execute(
            "create table employeeData(employeeId int(6) primary key,email varchar(100),name varchar(100),phone varchar(10),pfId int(4),dateOfJoining date,dateOfBirth date,department varchar(100))"
        )
        print("table created")
        self.commit_and_disconnect(connection)

    def add_employee(self):
        connection = self.connect()
        my_cursor = connection.cursor()

        while True:
            add = input("Add an employee? (y/n): ")
            if add == "n":
                break
            employeeId = input("enter employee id: ")
            email = input("enter employee email: ")
            while not self.validate_email(self.email):
                email = input("enter valid employee email: ")
            name = input("enter employee name: ")
            phone = input("enter employee phone: ")
            while not self.validate_phone(self.phone):
                email = input("enter valid employee phone: ")
            pfId = input("enter employee pfId: ")
            dateOfJoining = input("enter employee joing date(yy-mm-dd): ")
            dateOfBirth = input("enter employee birth date(yy-mm-dd): ")
            department = input("enter department: ")

            sql = "INSERT INTO employeeData (employeeId, email, name, phone, pfId, dateOfJoining, dateOfBirth, department) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (
                employeeId,
                email,
                name,
                phone,
                pfId,
                dateOfJoining,
                dateOfBirth,
                department,
            )
            my_cursor.execute(sql, values)
            print("Added employees successfully")
            self.commit_and_disconnect(connection)

    def read_employee(self):
        connection = self.connect()
        my_cursor = connection.cursor()
        my_cursor.execute("SELECT * FROM employeeData")
        employeeList = list()
        for row in my_cursor:
            employeeList.append(row)
        df = pd.DataFrame(employeeList)
        self.commit_and_disconnect(connection)
        print(df)

    def update_employee(self):
        connection = self.connect()
        my_cursor = connection.cursor()
        fieldToChange = input("Change which column? ")
        value = input("Input changed value: ")

        if fieldToChange == "email":
            if self.validate_email(value):
                print("valid email")
            else:
                print("Invalid email")

        if fieldToChange == "phone":
            if self.validate_phone(value):
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

        self.commit_and_disconnect(connection)
        print("Data updated!")


def console_app():
    print("1. read employee list")
    print("2. update employee")
    print("3. add employee")

    value = input()
    obj = Employee()
    obj.setter_function(
        1,
        "kbedding0@buzzfeed.com",
        "Keane Bedding",
        "3471534436",
        1,
        "10/17/2022",
        "8/9/2022",
        "Research and Development",
    )
    # obj.create_table()
    if value == "1":
        obj.read_employee()
    elif value == "2":
        obj.update_employee()
    elif value == "3":
        obj.add_employee()


console_app()
