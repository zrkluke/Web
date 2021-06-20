from django.db import models
from .base import model_base
content = '{"promissoryAmount":" ", ' \
          '"promissoryNote":"", "nationalID":"", ' \
          '"address":"", "promissoryAddress":"", ' \
          '"promissoryDate":"","promissoryLastDate":"", ' \
          '"promissoryNoticeDate":"", "promissoryCourt":"", "Date":""}'

items = "{[1,2,3]}"


class Consumer(models.Model):
    orderID = models.TextField()
    loginID = models.TextField(primary_key=True, verbose_name="LineID")
    name = models.TextField(default="", verbose_name="請輸入全名")
    email = models.TextField(max_length=50, default="", verbose_name="ex:xxxx@gmail.com", blank=True)
    phone = models.TextField(max_length=10, default="", verbose_name="ex:0912345678")
    timeStamp = models.DateTimeField()

    class Meta(object):
        db_table = "tblCustomer"


class ApplicationItem(models.Model):
    itemID = models.TextField(primary_key=True)
    name = models.TextField()
    content = models.TextField()

    class Meta(object):
        db_table = "tblApplicationItem"


class ApplicationCategory(models.Model):
    categoryID = models.TextField(primary_key=True)
    category = models.TextField()
    item = models.ForeignKey(ApplicationItem, on_delete=models.CASCADE)

    class Meta(object):
        db_table = "tblApplicationCategory"

