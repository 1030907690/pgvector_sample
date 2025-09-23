from django.db import models

# Create your models here.

from datetime import datetime
from pgvector.django import VectorField

class Item(models.Model):
    id = models.AutoField(primary_key=True)  # 主键可省略不写
    embedding = VectorField(dimensions=512)

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'items'  # 指定数据库表名
