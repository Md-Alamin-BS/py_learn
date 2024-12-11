class student:
    def __init__ (self, name, age, grade, major, is_on_probation):
        self.name = name
        self.age = age
        self.grade = grade
        self.major = major
        self.is_on_probation = is_on_probation

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}, Major: {self.major}, Is on probation: {self.is_on_probation}"
    
    def my_method(self):
        print("This is a method that prints student name: " + self.name)
        
    def grading(self):
        if self.grade >= 3.5:
            print(f"{self.name} is a good student")
        else:
            print(f"{self.name} needs to work harder")


if __name__ == "__main__":
    # Creating an instance of the student class
    student2 = student("Al-Amin", 25, 3.6, "Computer Science", False)
    print(student2)  # This will invoke the __str__ method and print the string representation of the student2 object
    print(student2.age)

    # Calling the my_method on the instance student2
    student2.my_method()  # This will invoke the my_method function and print the student name




class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
        

