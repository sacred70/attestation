from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Supplier, NetworkNode, Product


class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'country', 'city', 'street', 'house_number', 'supplier_link']
    list_filter = ['city']
    actions = ['clear_debt']

    def supplier_link(self, obj):
        link = reverse('admin:sales_network_supplier_change', args=[obj.supplier.id])
        return format_html('<a href="{}">{}</a>', link, obj.supplier.name)

    def clear_debt(self, request, queryset):
        for node in queryset:
            node.products.update(debt=0)

    supplier_link.short_description = 'Поставщик'
    clear_debt.short_description = 'Очистить задолженность'


admin.site.register(NetworkNode, NetworkNodeAdmin)
admin.site.register(Supplier)
admin.site.register(Product)
