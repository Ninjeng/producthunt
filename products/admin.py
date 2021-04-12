from django.contrib import admin
from django.contrib.admin import ModelAdmin
from . models import Product


class ProductAdmin(ModelAdmin):
    list_display = ('product_name','description', 'upvote', 'downvote', 'author', 'date_published')
    search_fields = ('product_name','author',)
    readonly_fields = ('date_published',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Product, ProductAdmin)
