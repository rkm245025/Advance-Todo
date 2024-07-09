from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class ToDoItem(models.Model):
    PRIORITY_CHOICES=[
        ('L','Low'),
        ('M','Medium'),
        ('H','High'),
    ]
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    due_date=models.DateField(null=True,blank=True)
    priority=models.CharField(max_length=1,choices=PRIORITY_CHOICES)
    completed=models.BooleanField(default=False)
    categories=models.ManyToManyField(Category,blank=True)


    def __str__(self):
        return self.title
    
class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.first_name





