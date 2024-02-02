from django.contrib import admin
from .models import Products
# Register your models here.

#admin.site.register(Products)

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'cumparat')
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        if user.is_superuser:
            return queryset

        return queryset.filter(user=user)