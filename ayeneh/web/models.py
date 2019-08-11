from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Quiz(models.Model):
    Name = models.CharField(max_length=120)
    Description = models.TextField(null=True, blank=True)
    Layout = models.CharField(max_length=120 , blank=True , null=True)

    Number = models.IntegerField(auto_created=True , blank=True , null=True , default=0)


    def save(self, *args, **kwargs):
        if not self.__class__.objects.filter(id=self.id).exists() :
            self.Number = self.__class__.objects.all().count()  + 1
        super(Quiz, self).save(*args, **kwargs)



class Question(models.Model):
    Quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    Number = models.IntegerField(auto_created=True , blank=True)
    Text = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = (('Quiz', 'Number'),)

    def save(self, *args, **kwargs):

        self.Number = self.__class__.objects.filter(Quiz = self.Quiz).count() + 1
        super(Question, self).save(*args, **kwargs)



class Answer(models.Model):
    Question = models.ForeignKey(Question, on_delete=models.CASCADE)
    Text = models.TextField(null=True, blank=True)
    Number = models.IntegerField(auto_created=True , blank=True)

    class Meta:
        unique_together = (('Question', 'Number'),)

    def save(self, *args, **kwargs):
        self.Number = self.__class__.objects.filter(Question=self.Question).count() + 1
        super(Answer, self).save(*args, **kwargs)



class Parameter(models.Model):
    Name = models.CharField(max_length=100)
    Quiz = models.ForeignKey(Quiz , on_delete=models.CASCADE)



class Assessment(models.Model):
    Answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    Parameter = models.ForeignKey(Parameter , on_delete=models.CASCADE)
    Value = models.IntegerField(default=0)


class Student(models.Model):
    Username = models.OneToOneField(User, on_delete=models.CASCADE)
    PhoneNumber = models.CharField(max_length=15, blank=True)
    Name = models.CharField(max_length=40, blank=True)
    Credit = models.IntegerField(blank=True , default=0)
    State = models.CharField(max_length=40, blank=True ,default="1")


    def __str__(self):
        return "{}".format(self.Name)


class Result(models.Model):
    Username = models.ForeignKey(Student, on_delete=models.CASCADE)
    Answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

