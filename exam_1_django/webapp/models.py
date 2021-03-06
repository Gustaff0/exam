from django.db import models

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    mail = models.EmailField(max_length=254, null=False, blank=False,)
    text = models.TextField(max_length=3000, null=False, blank=False)
    time_start = models.DateTimeField(auto_now_add=True, null=False, blank=True)
    time_edit = models.DateTimeField(auto_now=True, blank=True, null=False)
    status = models.CharField(max_length=200, null=False, blank=False, default='active')


    class Meta:
        db_table = 'Hotel'
        verbose_name = 'Регистрация'
        verbose_name_plural = 'Регистрации'

    def __str__(self):
        return f'{self.id}. {self.time_start}: {self.name} - {self.status} - {self.time_edit}'
