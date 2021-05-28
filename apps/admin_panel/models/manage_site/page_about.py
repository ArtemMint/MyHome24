"""
About models for web-site
"""

from django.db import models

from solo.models import SingletonModel


class AboutPage(SingletonModel):
    """
    About page
    """
    title = models.CharField(
        max_length=100,
        default='',
        blank=False,
        verbose_name='Заголовок',
    )
    short_text = models.CharField(
        blank=False,
        max_length=3000,
        verbose_name='Краткий текст',
    )
    image = models.ImageField(
        verbose_name='Рекомендуемый размер: (250x310)',
        upload_to='images/about/director/',
        blank=True,
    )
    seo = models.OneToOneField(
        'admin_panel.SEO',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name='Setting SEO',
        related_name='about_page',
    )

    def __str__(self):
        return str(self.title)


class AboutGallery(models.Model):
    """
    Gallery in About
    """
    about = models.ForeignKey(
        'admin_panel.AboutPage',
        on_delete=models.CASCADE,
        related_name='gallery',
    )
    image = models.ImageField(
        blank=True,
        upload_to='images/about/gallery/',
        verbose_name='Рекомендуемый размер: (1200x1200)',
    )


class AboutExtraInfo(models.Model):
    """
    Additional info in About
    """
    about = models.OneToOneField(
        'admin_panel.AboutPage',
        on_delete=models.CASCADE,
        related_name='extra_info',
    )
    title = models.CharField(
        max_length=100,
        default='',
        blank=True,
        verbose_name='Заголовок',
    )
    short_text = models.CharField(
        blank=True,
        max_length=1000,
        verbose_name='Краткий текст',
    )

    def __str__(self):
        return str(self.title)


class AboutExtraGallery(models.Model):
    """
    Gallery in About
    """
    about = models.ForeignKey(
        'admin_panel.AboutPage',
        on_delete=models.CASCADE,
        related_name='extra_gallery',
    )
    image = models.ImageField(
        blank=True,
        upload_to='images/about/additional_gallery/',
        verbose_name='Рекомендуемый размер (1200x1200)',
    )


class AboutDocument(models.Model):
    """
    Document in About
    """
    about = models.ForeignKey(
        'admin_panel.AboutPage',
        on_delete=models.CASCADE,
        related_name='documents',
    )
    document = models.FileField(
        blank=True,
        upload_to='files/about/',
        verbose_name='PDF, JPG (максимальный размер 20 Mb)',
    )
    name = models.CharField(
        verbose_name='Название документа',
        max_length=100,
        null=True,
        blank=True,
    )
