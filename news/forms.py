from .models import Articles
from django.forms import ModelForm, Textarea, DateTimeInput, TextInput

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'announce', 'text', 'date_time']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            'announce': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Полный текст'
            }),
            'date_time': DateTimeInput(attrs={
                'hidden': 'True',
                'value': '2000-10-10 10:10:10'
            })
        }