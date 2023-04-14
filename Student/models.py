from django.db import models

# Create your models here.
class City(models.Model):
    city_name = models.CharField(max_length=40)

    def __str__(self):
        return self.city_name

class Course(models.Model):
    course_name = models.CharField(max_length=40)

    def __str__(self):
        return self.course_name

class Student(models.Model):
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    mobile = models.BigIntegerField()
    city = models.ForeignKey(City, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)

    def __str__(self):
        return self.fname