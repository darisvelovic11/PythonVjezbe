class License:
    def __init__(self, category, issued_date):
        self.category = category
        self.issued_date = issued_date

    def __str__(self):
        return f"License {self.category} — issued: {self.issued_date}"


class Instructor:
    def __init__(self, name, experience_years):
        self.name = name
        self.experience_years = experience_years

    def __str__(self):
        return f"Instructor {self.name} ({self.experience_years} years experience)"


class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"


class Student:
    def __init__(self, name, age, vehicle, instructor):
        self.name = name
        self.age = age
        self.vehicle = vehicle
        self.instructor = instructor
        self.license = None

    def assign_license(self, license):
        self.license = license

    def __str__(self):
        if self.license is None:
            license_info = "Not yet assigned"
        else:
            license_info = str(self.license)   # calls License.__str__

        return (f"Student: {self.name} (age {self.age})\n"
                f"Instructor: {self.instructor}\n"    # calls Instructor.__str__
                f"Vehicle: {self.vehicle}\n"          # calls Vehicle.__str__
                f"License: {license_info}")


vehicle = Vehicle("Toyota", "Corolla", 2022)
instructor = Instructor("Ana", 8)
student = Student("Daris", 20, vehicle, instructor)

print(student)

license = License("B", "2024-01-15")
student.assign_license(license)

print("---")
print(student)


"""**Output:**
```
Student: Daris (age 20)
Instructor: Instructor Ana (8 years experience)
Vehicle: 2022 Toyota Corolla
License: Not yet assigned
---
Student: Daris (age 20)
Instructor: Instructor Ana (8 years experience)
Vehicle: 2022 Toyota Corolla
License: License B — issued: 2024-01-15"""