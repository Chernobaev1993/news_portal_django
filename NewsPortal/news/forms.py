from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    content = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'type_of',
            'content',
            'author',
        ]

    # def clean(self):
    #     cleaned_data = super().clean()
    #     name = cleaned_data.get("name")
    #     description = cleaned_data.get("description")
    #
    #     if name == description:
    #         raise ValidationError(
    #             "Описание не должно быть идентично названию."
    #         )
    #
    #     return cleaned_data
