"""
Module with main page tables of the website
"""

from django.db import models

from ckeditor.fields import RichTextField
from solo.models import SingletonModel
from .page_seo import SEO


class IndexPage(SingletonModel):
    """
    Table with main page info
    """
    main_title = models.CharField(
        max_length=100,
        default='',
        blank=True,
        verbose_name='Заголовок',
    )
    short_text = RichTextField(
        blank=False,
        max_length=1000,
        verbose_name='Краткий текст',
    )
    apps_status = models.BooleanField(
        default='False',
        verbose_name='Показать ссылки на приложения',
    )
    seo = models.OneToOneField(
        SEO,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Settings SEO',
        related_name='index_page'
    )

    def __str__(self):
        """
        Display title of main page
        """
        return str(self.main_title)


class IndexSlider(models.Model):
    """
    Slider on main page
    """
    index = models.ForeignKey(
        IndexPage,
        on_delete=models.CASCADE,
        related_name='slider'
    )
    image = models.ImageField(
        blank=True,
        upload_to='images/index/slider/',
        verbose_name='Рекомендуемый размер: (1920x800)'
    )

    def __str__(self):
        return str(self.image)


class IndexBlock(models.Model):
    """
    Places near building
    """
    index = models.ForeignKey(
        IndexPage,
        on_delete=models.CASCADE,
        verbose_name='Title of the block',
        related_name='block',
    )
    image = models.ImageField(
        blank=True,
        upload_to='images/index/near_us/',
        verbose_name='Рекомендуемый размер: (1000x600)'
    )
    title = models.CharField(
        blank=True,
        max_length=100,
        verbose_name='Заголовок блока',
    )
    description = models.TextField(
        blank=True,
        max_length=350,
        verbose_name='Описание',
    )

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.title)
