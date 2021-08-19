from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)


class ToMeet(models.Model):
    persone = models.CharField(max_length=100)
    phone_number = models.IntegerField("Number")
    date_of_meeting = models.DateTimeField("Meet")
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)



class Goal_for_month(models.Model):
    goal = models.CharField(max_length=100)
    month = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=100)
    reason_for_goal = models.CharField(max_length=100)


    # def __init__(self):
    #     return self.title 

 
