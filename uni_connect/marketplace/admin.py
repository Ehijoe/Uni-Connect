from django.contrib import admin
from .models import User, Store, Product, Category

admin.site.register(User)
admin.site.register(Store)
admin.site.register(Product)
admin.site.register(Category)