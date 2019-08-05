from django.db import models

# Create your models here.

class Quiz(models.Model):
    Name = models.CharField(max_length=120)
    Description = models.TextField(null=True, blank=True)



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