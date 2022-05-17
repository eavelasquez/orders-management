from django.db import models

# Create your models here.


class Service(models.Model):
    name = models.CharField(
        max_length=200, verbose_name='Name', unique=True, null=False)
    description = models.TextField(verbose_name='Description', null=False)
    icon = models.CharField(max_length=200, verbose_name='Icon', null=False)
    image = models.ImageField(verbose_name='Image', null=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated')

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.name
