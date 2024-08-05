from django.db import models


class Student(models.Model):
    student_nr = models.PositiveIntegerField()
    first_name = models.CharField(blank=False, null=True, max_length=50)
    second_name = models.CharField(blank=False, null=True, max_length=50)
    age = models.PositiveIntegerField(blank=False, null=True)
    email = models.EmailField(blank=False,null=True,max_length=100)
    number = models.PositiveIntegerField(blank=False, null=True)
    nationality = models.CharField(blank=False, null=True, max_length=100)
    field_of_study = models.CharField(blank=False, null=True, max_length=50)
    bio = models.TextField(null=True, max_length=255)
    upload = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        permissions = [
            ("give_medal", "Can give medals"),
        ]

    def __str__(self):
        return f'Student: {self.first_name} {self.second_name}'

    def gpa(self):
        grade_count = self.grade_set.count()
        if grade_count == 0:
            return None
        return sum(g.grade for g in self.grade_set.all()) / grade_count


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    assignments = models.BooleanField(default=False, null=True)
    grade = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f"{self.student} - {self.subject}: {self.grade}"





