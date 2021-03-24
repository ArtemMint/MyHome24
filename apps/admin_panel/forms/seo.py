"""
SEO form
"""

from django import forms

from admin_panel.models.page_seo import *


class SEOForm(forms.ModelForm):
    """
    SEO form
    """

    class Meta:
        model = SEO
        fields = (
            'seo_title',
            'seo_description',
            'seo_keywords',
        )
        widgets = {
            'seo_title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'seo_description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '6',
                }
            ),
            'seo_keywords': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '6',
                }
            ),
        }
