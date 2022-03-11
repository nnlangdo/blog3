from django.contrib import admin
from .models import Post,Comment,Category
from mptt.admin import MPTTModelAdmin
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','status','pub_date')


admin.site.register(Category)

admin.site.register(Comment,MPTTModelAdmin)