from django.db import models

# Import from user model


class Store(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stores")
    name = models.CharField(max_length=64)
    logo = models.ImageField(upload_to="logos")
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    description = models.TextField(blank=False)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}"
    

class Category(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="categories")
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"
    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=64)
    description = models.TextField(blank=False)
    # Product image was not in the initial diagram
    image = models.ImageField(upload_to="product_images")
    price = models.DecimalField(max_digits=12, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}"