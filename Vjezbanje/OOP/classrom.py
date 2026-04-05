class Classroom():
    def __init__(self, teacher):
        self.teacher = teacher
        self.students = []
    
    def add_student(self, name, grade):
        self.students.append({
            'name':name,
            'grade':grade
        })
    
    def __len__(self):
        return len(self.students)
    
    def __str__(self):
        grades = sum(student['grade'] for student in self.students)
        average =round(grades/ len(self.students),2)
        return f"Mr.{self.teacher}'s class: {len(self.students)}, average: {average}"
    
    def __contains__(self, name):
        return any(student['name']==name for student in self.students)
    
    def __getitem__(self,index):
        return self.students[index]['name']
    
cls1 = Classroom("Mr. Smith")
cls1.add_student("Daris", 95)
cls1.add_student("Ana", 88)
cls1.add_student("Marko", 82)

print(len(cls1))              # 3
print(cls1)                   # Mr. Smith's class: 3 students, average grade: 88.33
print("Daris" in cls1)        # True
print("Mirsad" in cls1)        # False
print(cls1[0])                # Daris
