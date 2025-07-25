from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    message = models.TextField(max_length=500)

class ItemList(models.Model):
   Category_name = models.CharField(max_length=100)
   def __str__(self):
        return self.Category_name
   
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    Category = models.ForeignKey(ItemList, related_name='Name', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='items/')
    def __str__(self):
        return self.name

class AboutUs(models.Model):
    Description = models.TextField(blank=False)

class Feedback(models.Model):
    User_name = models.CharField(max_length=100)
    Description = models.TextField(blank=False)
    Image = models.ImageField(upload_to='feedback_images/', null=True, blank=True)  # Optional: allow null and blank for existing data
    def __str__(self):
        return self.User_name
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Cho phép null
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15) 
    province = models.CharField(max_length=100)  
    district = models.CharField(max_length=100) 
    address = models.TextField()
    note = models.TextField(blank=True, null=True)
    payment_method = models.CharField(max_length=50,)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
     username = self.user.username if self.user and hasattr(self.user, "username") else "Guest"
     return f"Order {self.id} - {username} ({self.name})"
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.CharField(max_length=255)  
    image = models.ImageField(upload_to='media/Order_Img')
    quantity = models.CharField(max_length=30)
    price = models.CharField(max_length=50)
    total = models.CharField(max_length=1000)
    def __str__(self):
        username = self.order.user.username if self.order.user else "Guest"
        return f"OrderItem: {self.product} - {username}" 
 
 
     


