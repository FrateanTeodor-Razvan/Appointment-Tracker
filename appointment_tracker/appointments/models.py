import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
class Application(models.Model):
    application_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.application_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Reply(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    reply_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.reply_text
