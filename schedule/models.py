from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def student_count(self):
        return self.students.count()


class Student(models.Model):
    name = models.CharField(max_length=100)
    school_class = models.ForeignKey(
        Class, related_name="students", on_delete=models.CASCADE
    )


class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subjects = models.ManyToManyField(Subject, related_name="teachers")


class Schedule(models.Model):
    school_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    day_of_week = models.IntegerField(choices=[(i, i) for i in range(1, 8)])
    hour = models.TimeField()

    class Meta:
        ordering = ["day_of_week", "hour"]
        indexes = [
            models.Index(fields=["day_of_week", "school_class"]),
            models.Index(fields=["school_class", "day_of_week"]),
            models.Index(fields=["hour"]),
        ]
