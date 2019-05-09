from django.db import models


LOCALE_CHOICES = (
    ('en', 'English'),
    ('ko', 'Korean'),
    ('ja', 'Japanese')
)


class Key(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


class Translation(models.Model):
    id = models.AutoField(primary_key=True)
    key_id = models.ForeignKey(
        'Key',
        related_name='translations',
        on_delete=models.CASCADE,
    )
    locale = models.CharField(
        max_length=2,
        choices=LOCALE_CHOICES,
    )
    value = models.TextField()
