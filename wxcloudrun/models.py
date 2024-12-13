from datetime import datetime

from django.db import models


# Create your models here.
class Counters(models.Model):
    id = models.AutoField
    count = models.IntegerField(max_length=11, default=0)
    createdAt = models.DateTimeField(default=datetime.now(), )
    updatedAt = models.DateTimeField(default=datetime.now(),)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Counters'  # 数据库表名
class ReminderStatus(models.Model):
    reminder_enabled = models.BooleanField(default=False)  # 用于存储喝水提醒是否开启的状态，默认是关闭

    def __str__(self):
        return f"喝水提醒状态: {self.reminder_enabled}"