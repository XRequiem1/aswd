from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    age = models.PositiveIntegerField(default=1, verbose_name='Возраст')
    gender = models.ForeignKey('gender', on_delete=models.CASCADE)
    birthDay = models.DateField(verbose_name='Дата рождения', default='2023-03-05')

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'

class Gender(models.Model):
    sex = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.sex} пол'
