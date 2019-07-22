from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class Question(models.Model):
    questionText=models.CharField(max_length=200)
    pubDate = models.DateTimeField()

    def was_published_recently(self):
        return self.pubDate >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.questionText

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choiceText = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.choiceText
