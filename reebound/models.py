from django.db import models
class Gallery(models.Model):
    image =  models.FileField(null=True)
class Trainers(models.Model):
    name = models.TextField(max_length=50)
    image =  models.FileField(null=True)
    field =  models.TextField(max_length= 50)
    def __str__(self):
        return self.name
class Plan(models.Model):
    plantime = models.TextField(max_length= 50)
    planamount = models.TextField(max_length= 50)
    classperiod = models.TextField(max_length= 50)
    classtype = models.TextField(max_length= 50)
    classequiment = models.TextField(max_length= 50)
    trainer = models.TextField(max_length= 50)
    classtime = models.TextField(max_length= 50)

class Workout(models.Model):
    image = models.FileField(null=True)
    workouttypes = models.TextField(max_length=20)
    workoutmethods = models.TextField(max_length=20)
class ABOUTUS(models.Model):
    video = models.FileField(null=True)
class SERVICES(models.Model):
    video = models.FileField(null=True)
class TimeTable(models.Model):
    time = models.TextField(max_length=20)
    mondayworkout = models.TextField(max_length=20, null=True)
    monday_trainer = models.ForeignKey(Trainers, on_delete=models.CASCADE, null=True)
    Tuesdayworkout = models.TextField(max_length=20)
    Tuesday_trainer = models.TextField(max_length=20)
    Wednesdayworkout = models.TextField(max_length=20)
    Wednesday_trainer = models.TextField(max_length=20)
    Thusdayworkout = models.TextField(max_length=20)
    Thusday_trainer = models.TextField(max_length=20)
    Fridayworkout = models.TextField(max_length=20)
    Friday_trainer = models.TextField(max_length=20)
    Saturdayworkout = models.TextField(max_length=20)
    Saturday_trainer = models.TextField(max_length=20)
    Sundayworkout = models.TextField(max_length=20)
    Sunday_trainer = models.TextField(max_length=20)

class blog(models.Model):
    image = models.FileField(null=True)
    heading = models.TextField(max_length=50)
    para = models.TextField(max_length=200)








