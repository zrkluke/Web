from django.db import models
from enum import Enum
from infrastructure.components.methods import convert_from_json


# 建立每一個表單所需要的table

class Promissory(models.Model):
    orderID = models.CharField(max_length=12, primary_key=True,
                               default="", blank=True)
    promissoryAmount = models.CharField(max_length=1024, default="1")
    promissoryNote = models.CharField(max_length=1024, default="1")
    nationalID = models.CharField(max_length=1024, default="1")
    address = models.CharField(max_length=1024, default="1")
    promissoryAddress = models.CharField(max_length=1024, default="")
    promissoryDate = models.CharField(max_length=1024, default="1")
    promissoryLastDate = models.CharField(max_length=1024, default="1")
    promissoryNoticeDate = models.CharField(max_length=1024, default="1")
    promissoryCourt = models.CharField(max_length=1024, default="1")
    date = models.CharField(max_length=1024, default="1")
    price = models.IntegerField(default="1800")

    @classmethod
    def from_json(cls, data):
        return cls(**convert_from_json(data))

    class Meta(object):
        db_table = "tblPromissory"


class OrderStatus(Enum):
    Created = 0
    UnPaid = 1
    Paid = 2
