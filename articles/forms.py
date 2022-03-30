from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
    
    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = Article.objects.all().filter(title__icontains=title) # Title Duplicate Detect
        if qs.exists():
            self.add_error("title", "{} already in use. Please pick another title".format(title))
        return data

class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # def clean_title(self):
    #     title = self.cleaned_data.get('title')
    #     if title.lower().strip() == "the office":
    #         raise forms.ValidationError("This title is taken")
    #     return title
    
    def clean(self):
        cleaned_data = self.cleaned_data
        title = self.cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.lower().strip() == "the office":
            self.add_error('title', 'This title is taken')
            # raise forms.ValidationError("This title is taken")
        return cleaned_data