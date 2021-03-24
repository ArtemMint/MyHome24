"""
Index page forms
"""

from django import forms

from ..models.page_index import (
    IndexPage,
    IndexBlock,
    IndexSlider,
)


class IndexPageForm(forms.ModelForm):
    """
    Index page form
    """

    class Meta:
        """
        Class Meta
        """
        model = IndexPage
        fields = (
            'main_title',
            'short_text',
            'apps_status'
        )
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'short_text': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'apps_status': forms.CheckboxInput(
                attrs={
                    # 'class': 'form-check-input'
                }
            ),
        }


class IndexSliderForm(forms.ModelForm):
    """
    Slider images
    """
    class Meta:
        """
        Class Meta
        """
        model = IndexSlider
        fields = ('image',)
        widgets = {
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }


class IndexBlockForm(forms.ModelForm):
    """
    Slider images
    """
    class Meta:
        """
        Class Meta
        """
        model = IndexBlock
        fields = (
            'image',
            'title',
            'description'
        )
        widgets = {
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


IndexSliderFormset = forms.inlineformset_factory(
    IndexPage,
    IndexSlider,
    IndexSliderForm,
    fields=('image',),
    extra=3,
    max_num=3,
    min_num=3,
)
IndexBlockFormset = forms.inlineformset_factory(
    IndexPage,
    IndexBlock,
    IndexBlockForm,
    fields=(
        'image',
        'title',
        'description'
    ),
    extra=5,
    max_num=6,
    min_num=3,
    can_delete=True,
)
