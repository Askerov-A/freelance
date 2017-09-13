from django.db import models

# Create your models here.

class Work(models.Model):
    work_content = models.CharField(max_length=1000)
    date_of_pub = models.DateTimeField('Создано')
    def __str__(self):
        x = ''
        if(self.done == true):
            x = 'Выполнено'
        else:
            x = 'Не выполнено'
        return self.work_content + ': ' + x
    done = models.BooleanField('Доделано или нет')
