from django.db import models




class Person(models.Model):
    name = models.CharField(max_length=100)
    email_id = models.EmailField(max_length=100)
    contact = models.CharField(max_length=12,blank=True)
    company = models.CharField(max_length=30)
    designation = models.CharField(max_length=15)
    description = models.TextField(blank=True)

    def __str__(self):
        return (self.name)




