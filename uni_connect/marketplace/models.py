from django.db import models

class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"


class Store(models.Model):
    brandName = models.CharField(max_length=50)
    contactEmail = models.EmailField(max_length=100)
    contactPhone = models.CharField(max_length=15)
    logo = models.ImageField(upload_to='logo')
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.brandName}"


class Product(models.Model):
    productName = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    stock = models.PositiveSmallIntegerField()
    description = models.TextField(blank=False)

    def __str__(self):
        return f"{self.productName}"

class Category(models.Model):
    categoryName = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.categoryName}"
    
    #Add category types

