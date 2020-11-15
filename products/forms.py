from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'content', 'price']

    # it's only work when you use forms in html page
    # def clean_title(self):
    #     data = self.cleaned_data.get('title')
    #     if len(data) < 4:
    #         raise forms.ValidationError("Title length is not long enough.")
    #     return data

# class ProductForm(forms.Form):
#     title = forms.CharField()
#     content = forms.CharField(widget=forms.Textarea, required=False)
#     price = forms.IntegerField(required=False, initial=0)
