from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField('Name', max_length=150, unique=True)
    address = models.CharField('Address', max_length=150, unique=True)
    phone = models.CharField('Phone', max_length=150, unique=True)
    email = models.EmailField('E-mail', max_length=150, unique=True)
    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField('User name', max_length=150, unique=True)
    last_name = models.CharField('Last name', max_length=150, unique=True)
    id_card = models.IntegerField('C.C', unique=True)
    id_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    address = models.CharField('Address', max_length=150, unique=True)
    phone = models.CharField('Phone', max_length=150, unique=True)
    email = models.EmailField('E-mail', max_length=150, unique=True)
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
