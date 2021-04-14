from django import forms

from .models import Product,Comment


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'image',]

class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'image',]

    def save(self, commit=True):
        product_Product = self.instance
        product_Product.product_name = self.cleaned_data['product_name']
        product_Product.description = self.cleaned_data['description']

        if self.cleaned_data['image']:
            product_Product.image = self.cleaned_data['image']

        if commit:
            product_Product.save()
        return product_Product


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)