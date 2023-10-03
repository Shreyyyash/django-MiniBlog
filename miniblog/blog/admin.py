from django.contrib import admin
from blog.models import Post,Contact
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display =["id","title","desc","author"]

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=["name","email","address","message"]
        