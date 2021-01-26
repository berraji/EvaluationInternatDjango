from django.db import models
from django.contrib.auth.models import User

# Create your models here.

QUES_TYPE = (
    ('SC','Single Choice'),
    ('MC','Multiple Choices'),
    ('SH','Short'),
    ('PA','Paragraph'),
)


class Form(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    form_title = models.CharField(max_length = 120)
    
    
    def __str__(self):
        return self.form_title
class Question(models.Model):
    ques_title = models.CharField(max_length=1000)
    ques_type = models.CharField(max_length=20, choices=QUES_TYPE, default='')
    #Many to many relationships between form and questions
    forms = models.ManyToManyField(Form)
    def __str__(self):
        return self.ques_title



class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=200)

