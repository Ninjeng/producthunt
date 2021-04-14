from django.contrib import admin
from django.contrib.admin import ModelAdmin
from . models import Product,Comment


class ProductAdmin(ModelAdmin):
    list_display = ('product_name','description','author', 'date_published')
    search_fields = ('product_name','author',)
    readonly_fields = ('date_published',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Product, ProductAdmin)
admin.site.register(Comment)
