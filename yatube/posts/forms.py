from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group',)
        help_text = {"help_text": "Подсказка"
                     }
        labels = {
            'text': ('текст'),
            'group': ('группа'),
            'help_text': ('подсказка')
        }
