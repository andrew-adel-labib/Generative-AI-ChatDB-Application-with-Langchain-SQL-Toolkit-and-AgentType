import sqlite3 

connection = sqlite3.connect("student.db")
cursor = connection.cursor()

table_info = """

CREATE TABLE Student(
Name VARCHAR(255),
Class VARCHAR(255),
Section VARCHAR(255),
Marks INT
);

"""

cursor.execute(table_info)

table_records = """

INSERT INTO Student(`Name`, `Class`, `Section`, `Marks`) 
VALUES
("Andrew", "Data Science", "A", 100),
("Tareq", "Cyber Security", "B", 100),
("Sherief", "Computer Science", "A", 99);

"""

cursor.execute(table_records)

table_show = """

SELECT * FROM Student;

"""

print("The Inserted Records are: ")
records = cursor.execute(table_show)

for record in records:
    print(record)

connection.commit()
connection.close()