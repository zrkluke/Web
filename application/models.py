from django.db import models

content = '{"orderID":"", "promissoryAmount":"", ' \
          '"promissoryNote":"", "nationalID":"", ' \
          '"address":"", "promissoryAddress":"", ' \
          '"promissoryDate":"","promissoryLastDate":"", ' \
          '"promissoryNoticeDate":"", "promissoryCourt":"", "date":"", "price":"1800"}'

content2 = '{"manName":" ", "manNationalID":"", "manAddress":"", ' \
           '"womanName":"", "womanNationalID":"", "womanAddress":"",' \
           '"firstWitnessName":"", "firstWitnessNationalID":"", "firstWitnessAddress":"",' \
           '"secondWitnessName":"", "secondWitnessNationalID":"", "secondWitnessAddress":""}'
items = "{[1,2,3]}"


class Consumer(models.Model):
    LineID = models.CharField(max_length=1024, primary_key=True, verbose_name="LineID")
    name = models.CharField(max_length=1024, default="", verbose_name="請輸入全名")
    email = models.CharField(max_length=1024, default="", verbose_name="ex:xxxx@gmail.com", blank=True)
    phone = models.CharField(max_length=10, default="", verbose_name="ex:0912345678")
    timeStamp = models.TextField()

    class Meta(object):
        db_table = "tblCustomer"


class ApplicationCategory(models.Model):
    categoryID = models.TextField(primary_key=True)
    category = models.TextField()

    class Meta(object):
        db_table = "tblApplicationCategory"


class ApplicationItem(models.Model):
    category = models.ForeignKey(ApplicationCategory, on_delete=models.CASCADE)
    itemID = models.TextField(primary_key=True)
    name = models.TextField()
    content = models.TextField()

    class Meta(object):
        db_table = "tblApplicationItem"


class Order(models.Model):
    orderID = models.CharField(max_length=12, primary_key=True)
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE, default="")
    price = models.TextField()
    orderStatus = models.TextField()
    content = models.TextField(default="")
    timeStamp = models.TextField(default="")

    class Meta(object):
        db_table = "tblOrder"
