from django.db import models

# Create your models here.


class Part(models.Model):
    part_id = models.IntegerField()
    name = models.CharField(max_length=200)
    text = models.TextField()
    total_number = models.IntegerField()
    used_number = models.IntegerField()

    def add_part(self):
        self.total_number = self.total_number + 1
        self.save()

    def take_part(self):
        self.total_number = self.total_number - 1
        self.used_number = self.used_number + 1
        self.save()

    def return_part(self):
        self.used_number = self.used_number - 1
        self.save()

    def getTotal(self):
        return self.total_number

    def getUsed(self):
        return self.used_number

    def getFree(self):
        free_parts = self.total_number - self.used_number
        return free_parts

    def __str__(self):
        return self.name