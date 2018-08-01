from django.contrib import admin
from .models import Book, Author


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'pub_house', 'pub_date')
    search_fields = ('name',)
    fieldsets = (
        ['Main',{
            'fields':('name', 'author', 'pub_house'),
        }],
        ['Advance',{
            'classes': ('collapse',),  # CSS
            'fields': ('pub_date',),
        }]
    )
# 自己定义，此时将按照新的进行管理，也就是可以对管理员增加单独的新增或者配置功能页面
# Register your models here


admin.site.register(Book, ContactAdmin)
admin.site.register(Author)

