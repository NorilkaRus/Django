from django import forms
from catalog.models import Product



class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        # fields = ('title', 'description')

    def clean_product(self):
        cleaned_data = self.cleaned_data['title', 'description']
        bad_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in bad_words:
            if word.title() in cleaned_data:
                raise forms.ValidationError('В названии или описании продукта используются запрещенные слова')
        return cleaned_data

