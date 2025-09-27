class student:
    school_name = "Digital school"
    def __init__(self, name, age, cours):
        self.name = name
        self.age = age
        self.cours = cours

student1=student("Elssa", 17, "python")
student2=student("Alisa", 27, "wordpress")
print(student1.cours)
print(student2.cours)