from App.forms import User
from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.
class Medicine_Group(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)    
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Medicine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4) 
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='Images/',default='Images/default.jpg')
    group = models.ForeignKey(Medicine_Group,on_delete=models.CASCADE)
    power = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    uses = models.TextField(max_length=2000)
    doses = models.TextField(max_length=2000)
    side_effect = models.TextField(max_length=1000)
    alternate_brands = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name + self.power
    


class Question(models.Model):
    question = models.CharField(max_length=500)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=timezone.localtime(timezone.now()), blank=True)
    
    def __str__(self):
        return self.question

class Answer(models.Model):
    answer = models.CharField(max_length=500)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    date_added = models.DateTimeField(default=timezone.localtime(timezone.now()), blank=True)
    def __str__(self):
        return self.answer
    
    
    

       
    
    