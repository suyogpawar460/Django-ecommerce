from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Product, Contact, Customer, Cart, Payment, OrderPlaced, Wishlist


# Register your models here.
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'discounted_price', 'category', 'product_image']
    ordering = ['id']


admin.site.register(Product, ProductModelAdmin)


class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']
    ordering = ['id']


admin.site.register(Contact, ContactModelAdmin)


class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'locality', 'city', 'state', 'zipcode']
    ordering = ['id']


admin.site.register(Customer, CustomerModelAdmin)


class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']
    ordering = ['id']

    def products(self, obj):
        link = reverse('admin:app_product_change', args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)


admin.site.register(Cart, CartModelAdmin)


class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'amount', 'razorpay_order_id', 'razorpay_payment_id',
                    'razorpay_payment_status', 'paid']
    ordering = ['id']


admin.site.register(Payment, PaymentModelAdmin)


class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customers', 'products', 'quantity', 'ordered_date', 'status', 'payments']
    ordering = ['id']

    def products(self, obj):
        link = reverse('admin:app_product_change', args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)

    def customers(self, obj):
        link = reverse('admin:app_customer_change', args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>', link, obj.customer.name)

    def payments(self, obj):
        link = reverse('admin:app_payment_change', args=[obj.payment.pk])
        return format_html('<a href="{}">{}</a>', link, obj.payment.razorpay_payment_id)


admin.site.register(OrderPlaced, OrderPlacedModelAdmin)


class WishlistModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'products']
    ordering = ['id']

    def products(self, obj):
        link = reverse('admin:app_product_change', args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)


admin.site.register(Wishlist, WishlistModelAdmin)
