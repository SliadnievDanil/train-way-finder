from django.db import models
from django.urls import reverse


class City(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='City')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cities'
        verbose_name = 'City'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('cities:detail', kwargs={'pk': self.pk})
