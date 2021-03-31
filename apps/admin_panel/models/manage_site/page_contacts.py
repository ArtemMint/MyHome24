"""
Contacts models for web-site
"""

from django.db import models

from solo.models import SingletonModel
from ckeditor.fields import RichTextField
from ...models import SEO


class ContactsPage(SingletonModel):
    """
    Contacts main page model
    """
    title = models.CharField(
        max_length=100,
        default='',
        blank=True,
    )
    short_text = RichTextField(
        max_length=1000,
        default='',
        blank=True,
    )
    url = models.URLField(
        max_length=500,
        verbose_name='Link on commerce site',
    )
    seo = models.OneToOneField(
        SEO,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Setting SEO',
        related_name='contacts_page',
    )

    def __str__(self):
        return str(self.title)


class ContactsAddress(models.Model):
    """
    Contacts - address, phone, e-mail, etc.
    """
    name = models.CharField(
        max_length=100,
        default='',
        blank=True,
    )
    location = models.CharField(
        max_length=100,
        default='',
        blank=True,
    )
    address = models.CharField(
        max_length=100,
        default='',
        blank=True,
    )
    phone = models.CharField(
        max_length=100,
        default='',
        blank=True,
    )
    email = models.EmailField(
        max_length=100,
        default='',
        blank=True,
    )
    contacts = models.ForeignKey(
        ContactsPage,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Contacts',
        related_name='contacts_address',
    )

    def __str__(self):
        return str(self.name)


class ContactsMap(models.Model):
    """
    Model for contacts map
    """
    map = models.CharField(
        max_length=1000,
        default='',
        blank=False,
        verbose_name='Map code',
    )
    contacts = models.ForeignKey(
        ContactsPage,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Map',
        related_name='map',
    )

    def __str__(self):
        return 'Map'
