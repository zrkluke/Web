from django.db import models
import uuid


# Create your models here.
class Customer(models.Model):

    name = models.CharField(max_length=50)
    GUID = uuid.uuid4()
    

    def __str__(self):
        return self.name

    class Meta(object):
        db_table = "Customer"
