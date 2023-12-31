from django import forms
from catalog.models import Product, Version



class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        #fields = '__all__'
        #fields = ('title', 'description')
        exclude = ('owner', )

    def clean_title(self):
        cleaned_data = self.cleaned_data['title']
        bad_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in bad_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('В названии продукта используются запрещенные слова')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        bad_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in bad_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('В описании продукта используются запрещенные слова')
        return cleaned_data

class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'