from django.db import models

# Create your models here.

class noise(models.TextChoices):
   undo='U',"Not yet Started"
   on='O',"ONGOING"
   done='D',"DONE"

class dmt(models.Model):
   name=models.CharField(verbose_name="Task name",max_length=65,unique=True)
   status=models.CharField(verbose_name="Task status",max_length=10,choices=noise.choices)

def _mint_(self):
   return self.name
