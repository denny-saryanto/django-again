from django import forms

class ArticleForm(forms.Form):
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