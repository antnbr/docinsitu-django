from django import forms
from .models import Article
from .models import Snap

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('text',)

class SnapForm(forms.ModelForm):

    class Meta:
        model = Snap
        fields = ('data',)
