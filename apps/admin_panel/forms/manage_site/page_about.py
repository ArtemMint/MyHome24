"""
About page forms
"""

from django import forms

from admin_panel.models.manage_site.page_about import (
    AboutPage,
    AboutGallery,
    AboutExtraGallery,
    AboutDocument,
    AboutExtraInfo,
)


class AboutPageForm(forms.ModelForm):
    """
    About page form
    """

    class Meta:
        """
        Class Meta
        """
        model = AboutPage
        fields = (
            'title',
            'short_text',
            'image',
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
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }


class AboutGalleryForm(forms.ModelForm):
    """
    About gallery form
    """

    class Meta:
        """
        Class Meta
        """
        model = AboutGallery
        fields = ('image',)
        widgets = {
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }


class AboutExtraInfoForm(forms.ModelForm):
    """
    Extra info in About
    """

    class Meta:
        """
        Class Meta
        """
        model = AboutExtraInfo
        fields = (
            'title',
            'short_text',
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
        }


class AboutExtraGalleryForm(forms.ModelForm):
    """
    About gallery form
    """

    class Meta:
        """
        Class Meta
        """
        model = AboutExtraGallery
        fields = ('image',)
        widgets = {
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }


class AboutDocumentForm(forms.ModelForm):
    """
    About document form
    """

    class Meta:
        """
        Class Meta
        """
        model = AboutDocument
        fields = (
            'document',
            'name',
        )
        widgets = {
            'document': forms.FileInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


AboutGalleryFormset = forms.inlineformset_factory(
    AboutPage,
    AboutGallery,
    AboutGalleryForm,
    fields=('image',),
    extra=1,
    max_num=5,
    min_num=1,
)
AboutExtraInfoFormset = forms.inlineformset_factory(
    AboutPage,
    AboutExtraInfo,
    AboutExtraInfoForm,
    fields=(
        'title',
        'short_text',
    ),
    extra=0,
    max_num=1,
    min_num=1,
)
AboutExtraGalleryFormset = forms.inlineformset_factory(
    AboutPage,
    AboutExtraGallery,
    AboutExtraGalleryForm,
    fields=('image',),
    extra=1,
    max_num=5,
    min_num=1,
)
AboutDocumentFormset = forms.inlineformset_factory(
    AboutPage,
    AboutDocument,
    AboutDocumentForm,
    fields=(
        'document',
        'name',
    ),
    extra=0,
    max_num=5,
    min_num=1,
)
