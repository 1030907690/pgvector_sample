from django.db import models

# Create your models here.

from datetime import datetime


# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True) #主键可省略不写
    name = models.CharField(max_length=32)
    age = models.IntegerField(default=20)
    phone = models.CharField(max_length=16)
    create_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 't_user'  # 指定数据库表名
