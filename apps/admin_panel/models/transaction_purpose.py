from django.db import models


class TransactionPurpose(models.Model):

    TYPE = (
        ('Приход', 'Приход'),
        ('Расход', 'Расход'),
    )
    name = models.CharField(
        max_length=150,
        verbose_name='Название',
        blank=False,
    )
    type = models.CharField(
        max_length=150,
        verbose_name='Приход/Расход',
        choices=TYPE,
    )

    def __str__(self):
        return self.name
