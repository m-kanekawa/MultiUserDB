from django.db import models

class Person(models.Model):
    name     = models.CharField(verbose_name='氏名', max_length=50, default='')
    age      = models.IntegerField(verbose_name='年齢', default=0)
    objects  = models.Manager()
    def __str__(self):
        return "%s(%d)" % (self.name, age)
