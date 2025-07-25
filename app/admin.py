from django.contrib import admin
from .models import *

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'message']  

class OrderItemInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ['name','phone','province','created_at']
    search_fields = ['name','phone','province']
    
admin.site.register(ItemList)
admin.site.register(Item)
admin.site.register(AboutUs)
admin.site.register(Feedback)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)

# Register your models here.
