class student:
    def __init__(self, name, age, grade):
        # initializes the student object
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"name: {self.name}, age: {self.age}, grade: {self.grade}")

# creating objects
student1 = student("monik", 10, "10th")
student2 = student("edvin", 5, "11th")

# accessing object methods
student1.display_info()
student2.display_info()
