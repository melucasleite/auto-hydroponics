from django.db import models


class Pump(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)


class Activation(models.Model):
    pump = models.ForeignKey(Pump, on_delete=models.CASCADE)
    date = models.DateTimeField('date activated')
    duration = models.IntegerField(max_length=99999)
    executed = models.BooleanField(default=False)