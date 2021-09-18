from django.db import models

# Create your models here.

class Amount(models.Model):
    modalities = models.CharField(max_length=200)
    grades = models.FloatField()
    def	__str__(self):
        return	self.modalities + ":" + str(self.grades)

class Age(models.Model):
    modalities = models.CharField(max_length=200)
    grades = models.FloatField()
    def	__str__(self):
        return	self.modalities + ":" + str(self.grades)

class Duration(models.Model):
    modalities = models.CharField(max_length=200)
    grades = models.FloatField() 
    def	__str__(self):
        return	self.modalities + ":" + str(self.grades)

class Rate(models.Model):
    modalities = models.CharField(max_length=200)
    grades = models.FloatField()
    def	__str__(self):
        return	self.modalities + ":" + str(self.grades)
