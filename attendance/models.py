from django.db import models
from django.contrib.auth.models import User
from recurrence.fields import RecurrenceField
from datetime import datetime


# table for storing maximum number of leaves that
# could be taken by a person

class Category(models.Model):

    BEGINNER = 'BEG'

    CATEGORIES_CHOICES =[
        ('CON','Convited'),
        ('BEG','Beginner'),
        ('INT','Intermediate'),
        ('ADV','Advanced'),
        ('MON','Monitor'),
        ('COA','Coach'),
        ('COO','Coordinator'),
    ]

    def __str__(self):
        return self.get_category_display()

    class Meta:
        verbose_name_plural = "Categories"

    category=models.CharField(max_length=3,choices=CATEGORIES_CHOICES ,default=BEGINNER)
    max_casual_leave=models.IntegerField()
    max_compensation_leave=models.IntegerField()
    max_earned_leave=models.IntegerField()
    max_half_pay_leave=models.IntegerField()
    max_leave_with_allowance=models.IntegerField()
    max_duty_leave=models.IntegerField()


# table for storing hod's and principal ( people who have to approve leaves
class Team(models.Model):

    def __str__(self):
        return self.name

    name=models.CharField(max_length=30)
    status=models.BooleanField(default=True, choices=[
        (True, 'Active'),
        (False, 'Inactive')])
    recurrences = RecurrenceField(null=True)
    time_in = models.TimeField(null=True)
    time_out = models.TimeField(null=True)


# table for storing details of the staff
class Athlete(models.Model):

    def __str__(self):
         return str(self.name)


    ON_HOLD = 'OH'
    UNDER_EVALUATION = 'UE'
    APT = 'AP'
    INAPT = 'IN'
    MEMBER = 'ME'
    DROPOUT = 'DO'

    STATUS_CHOICES = [
        (ON_HOLD, 'On hold'),
        (UNDER_EVALUATION, 'Under evaluation'),
        (APT, 'Apt'),
        (INAPT, 'Inapt'),
        (MEMBER, 'Member'),
        (DROPOUT, 'Dropout'),
    ]

    user=models.OneToOneField(User,on_delete=models.CASCADE, blank=True, null=True)
    athlete_id=models.IntegerField(primary_key=True ,unique=True) #must be alphanumeric
    name=models.CharField(max_length=100)
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    team=models.ForeignKey(Team, models.SET_NULL, blank=True, null=True)
    status=models.CharField(max_length=2,choices=STATUS_CHOICES, default=ON_HOLD)
    joining_date=models.DateField(default=None, blank=True, null=True)
    termination_date=models.DateField(default=None,blank=True, null=True)

    def create_athlete(user):
        athlete = Athlete(user=user)
        athlete.save()
    # post_save.connect(create_athlete, sender=User)


class Appointment(models.Model):

    def __str__(self):
        return str(datetime.strftime(self.date, '%A (%B %d, %Y)'))

    date = models.DateField(default=None, blank=True)
    team = models.ForeignKey(Team, models.SET_NULL, blank=True, null=True)


class Attendance(models.Model):

    ABSENT = 'AB'
    PRESENT = 'PR'
    EXCUSED = 'EX'
    COMPENSATION = 'CO'

    STATUS_CHOICES = [
        (ABSENT, 'Absent'),
        (PRESENT, 'Present'),
        (EXCUSED, 'Excused'),
        (COMPENSATION, 'Compensation')
    ]
    
    def __str__(self):
         return str(self.athlete) + ' [' + self.get_status_display() + ' on ' + str(self.appointment) + ']'

    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    status = models.CharField(max_length=2,choices=STATUS_CHOICES, default=ABSENT)
    justification = models.TextField(max_length=250, blank=True)

    class Meta:
        unique_together = (("athlete", "appointment"),)     
    