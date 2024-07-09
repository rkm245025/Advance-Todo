from django.contrib import admin
from .models import Category,ToDoItem,Customer



# Register your models here.

admin.site.register(Category)
admin.site.register(ToDoItem)
admin.site.register(Customer)