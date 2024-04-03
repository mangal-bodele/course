from django.db import models

class Course(models.Model):
    GENDER = [('F','Female'),('M','Male'),('O','Other')]
    COURSE = [('PY','python'),('JV','java'),('DJG','django'),('RCT','react')]
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)
    mobile_number = models.IntegerField()
    address = models.CharField(max_length=10)
    dob = models.DateField()
    gender = models.CharField(max_length=10,choices=GENDER)
    course =  models.CharField(max_length=10,choices=COURSE)
    fees = models.IntegerField()

