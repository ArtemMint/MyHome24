"""
Contacts models for web-site
"""

from django.db import models

from solo.models import SingletonModel
from ckeditor.fields import RichTextField


class ContactsPage(SingletonModel):
    """
    Contacts main page model
    """
    title = models.CharField(
        max_length=100,
        default='',
        blank=True,
        verbose_name='Заголовок',
    )
    short_text = RichTextField(
        max_length=1000,
        default='',
        blank=True,
        verbose_name='Краткий текст',
    )
    url = models.URLField(
        max_length=500,
        verbose_name='Ссылка на коммерческий сайт',
    )
    seo = models.OneToOneField(
        'admin_panel.SEO',
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
        verbose_name='ФИО',
    )
    location = models.CharField(
        max_length=100,
        default='',
        blank=True,
        verbose_name='Локация',
    )
    address = models.CharField(
        max_length=100,
        default='',
        blank=True,
        verbose_name='Адрес',
    )
    phone = models.CharField(
        max_length=100,
        default='',
        blank=True,
        verbose_name='Телефон',
    )
    email = models.EmailField(
        max_length=100,
        default='',
        blank=True,
        verbose_name='E-mail',
    )
    contacts = models.ForeignKey(
        'admin_panel.ContactsPage',
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
        verbose_name='Код карты',
    )
    contacts = models.ForeignKey(
        'admin_panel.ContactsPage',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Map',
        related_name='map',
    )

    def __str__(self):
        return 'Map'
