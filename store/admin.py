from django.contrib import admin
from .models import Category, Product, Product3DFile


class Product3DFileAdminInline(admin.TabularInline):
    model = Product3DFile
    max_num = 1


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('sku',)
    inlines = (Product3DFileAdminInline,)


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
