from django import forms
from .models import Product, Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in forbidden_words:
            if word in name.lower():
                raise forms.ValidationError("Название продукта содержит запрещенное слово")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in forbidden_words:
            if word in description.lower():
                raise forms.ValidationError("Описание продукта содержит запрещенное слово")
        return description


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ['product', 'version_number', 'version_name', 'is_active']
        widgets = {
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    def clean_is_active(self):
        is_active = self.cleaned_data['is_active']
        if is_active and Version.objects.filter(product=self.cleaned_data['product'], is_active=True).exclude(
                pk=self.instance.pk).exists():
            raise forms.ValidationError('Only one active version is allowed per product')
        return is_active
