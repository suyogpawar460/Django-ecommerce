from django.contrib.auth.models import User
from django.db import models

# Create your models here.

STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled'),
    ('Pending', 'Pending')
)

CATEGORY_CHOICES = (
    ('CR', 'Curd'),
    ('ML', 'Milk'),
    ('LS', 'Lassi'),
    ('MS', 'Milkshake'),
    ('PN', 'Paneer'),
    ('GH', 'Ghee'),
    ('CS', 'Cheese'),
    ('IC', 'Ice-Cream'),
)

STATE_CHOICES = (
    ('MH', 'Maharashtra'),
    ('MP', 'Madhya Pradesh'),
    ('KA', 'Karnataka'),
    ('KL', 'Kerala'),
    ('GA', 'Goa'),
    ('GJ', 'Gujarat'),
    ('HP', 'Himachal Pradesh'),
    ('AP', 'Andhra Pradesh'),
    ('AR', 'Arunachal Pradesh'),
    ('TS', 'Telangana'),
    ('TL', 'Tamilnadu'),
    ('PB', 'Punjab'),
    ('HR', 'Haryana'),
    ('MZ', 'Mizoram'),
    ('AS', 'Asam'),
    ('MG', 'Meghalaya'),
    ('CG', 'Chhattisgarh'),
    ('DL', 'Delhi'),
    ('JK', 'Jammu and Kashmir'),
    ('JH', 'Jharkhand'),
    ('MN', 'Manipur'),
    ('NL', 'Nagaland'),
    ('SK', 'Sikkim'),
    ('TR', 'Tripura'),
    ('PY', 'Pondicherry'),
    ('OR', 'Orisa'),
    ('RJ', 'Rajasthan'),
    ('WB', 'West Bengal'),
    ('BR', 'Bihar')
)


class Product(models.Model):
    title = models.CharField(max_length=200)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.email


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=200)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length=200, blank=True, null=True)
    razorpay_payment_status = models.CharField(max_length=200, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=200, blank=True, null=True)
    paid = models.BooleanField(default=False)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default='Pending', null=True, max_length=50, choices=STATUS_CHOICES)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
