import json

class Student:
    def __init__(self, id, name, grades = []):
        self.name = name
        self.id = id
        self.grades = grades
        self.average = 0

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        self.average = sum(self.grades) / len(self.grades)
        return self.average
    
    def status(self):
        if self.average >= 60:
            return "pass"
        else:
            return "fail"
    
    def store(self):

        student = {
            "id": self.id,
            "name": self.name,
            "grades": self.grades,
            "average": self.average,
            "status": self.status()
        }

        with open("students.json", "w") as file:
            file.write(f"{json.dumps(student)}\n")

# initialize the student object
student = Student(1, "Pawan", [90, 85, 84, 75, 60])

# add grade to the student
student.add_grade(80)

# get the average of the student
average = student.get_average()
print(f"Average of student {student.name} is: {average}")

# get the status of the student
status = student.status()
print(f"Status of student {student.name} is: {status}")

# store the student data in JSON format
student.store()
