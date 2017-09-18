from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class WorkCategory(models.Model):
    category_name = models.CharField(max_length=100)
    category_slug = models.CharField(max_length=100)
    def __str__(self):
        return self.category_name

class Work(models.Model):
    work_title = models.CharField(max_length=100)
    work_content = models.CharField(max_length=1000)
    work_category = models.ForeignKey(WorkCategory, blank = True, null = True)
    work_employee = models.ForeignKey(User, related_name='work_created')
    work_worker = models.ForeignKey(User, related_name='work_assigned', blank = True)
    date_of_pub = models.DateTimeField('Создано')
    def __str__(self):
        x = ''
        if(self.done == True):
            x = 'Выполнено'
        else:
            x = 'Не выполнено'
        return self.work_title + ' | ' + str(self.work_employee) + ' | ' + str(self.work_category) + ' | ' + x
    done = models.BooleanField('Доделано или нет')
