from django import forms

from .models import Product


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'image','upvote','downvote']

class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'image','upvote','downvote']

    def save(self, commit=True):
        product_Product = self.instance
        product_Product.product_name = self.cleaned_data['product_name']
        product_Product.description = self.cleaned_data['description']

        if self.cleaned_data['image']:
            product_Product.image = self.cleaned_data['image']

        if commit:
            product_Product.save()
        return product_Product


class UpvoteForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['upvote']
    
    def save(self, commit=True):
        product_Product = self.instance
        product_Product.upvote = self.cleaned_data['upvote']+1

        if commit:
            product_Product.save()
        return product_Product