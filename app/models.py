from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta



class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class CourseSchedule(models.Model):
    DAYS = (
        ('sun-tue-thu','sunday-tuesday-thursday'),
        ('mon-wed','monday-wednesday'),
        ('sun-thu','sunday-thursday'),
    )
    
    TIMES =(
        ('8:00','8:00'),
        ('9:30','9:30'),
        ('11:00','11:00'),
        ('12:30','12:30'),
        ('2:00','2:00')
    )
    
    ENDTIMES =(
        ('9:15','9:15'),
        ('10:45','10:45'),
        ('12:15','12:15'),
        ('1:45','1:45'),
        ('3:15','3:15')
    )
    days = models.CharField(max_length=20,choices=DAYS)
    start_time = models.CharField(max_length=10,choices=TIMES)
    end_time = models.CharField(max_length=10,choices=ENDTIMES)

    def __str__(self):
        return f"{self.days}: {self.start_time} - {self.end_time}"

class Course(models.Model):
    id = models.IntegerField(auto_created=True,primary_key=True)
    code = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.CharField(max_length=100)
    
    capacity = models.IntegerField()
    schedule = models.ForeignKey(CourseSchedule, on_delete=models.CASCADE)
    enrolled_students = models.ManyToManyField(User, through='StudentRegistration')
    

    def __str__(self):
        return f"{self.name}: {self.instructor}"

class StudentRegistration(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_registered = models.DateTimeField(auto_now_add=True)

class Notification(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    is_expired = models.BooleanField(default=False)
    message = models.TextField()

    def __str__(self):
        return f'Notification for {self.course.name}: {"Expired" if self.is_expired else "Active"}'