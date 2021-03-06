from .models import Group, Post

from django.contrib import admin


class PostAdmin(admin.ModelAdmin):
    list_editable = ('group',)
    list_display = ('pk', 'text', 'pub_date', 'author', 'group')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'description')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Group, GroupAdmin)
admin.site.register(Post, PostAdmin)
