from django.db import models

# Import from user model


class Store(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stores")
    brandName = models.CharField(max_length=64)
    logo = models.ImageField(upload_to="logos")
    contactEmail = models.EmailField(max_length=100)
    contactPhone = models.CharField(max_length=15)
    description = models.TextField(blank=False)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.brandName}"
    

class Category(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="categories")
    categoryName = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.categoryName}"
    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="products")
    productName = models.CharField(max_length=64)
    description = models.TextField(blank=False)
    # Product image was not in the initial diagram
    image = models.ImageField(upload_to="product_images")
    price = models.DecimalField(max_digits=12, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.productName}"