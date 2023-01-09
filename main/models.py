from django.db import models
# Create your models here.

class Skills(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)

class Message(models.Model):
    name=models.CharField(max_length=255,verbose_name='Имя')
    email=models.EmailField(verbose_name='Почта')
    text=models.TextField(verbose_name='Сообщение')

class Project(models.Model):
    title=models.CharField(max_length=255)
    discripsion=models.TextField()
    link=models.TextField()
    image=models.ImageField(upload_to='static')