from django.db import models


class Consumer(models.Model):
    LoginID = models.CharField(u'LineID', max_length=20)
    Name = models.CharField(u'姓名', max_length=10)
    Sex = models.BooleanField(default=True)
    email = models.CharField(max_length=50, null=True)
