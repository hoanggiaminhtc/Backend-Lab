from django.contrib import admin
from news.models import News,Comment
# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date']
    search_fields = ['title']
class CommentAdmin(admin.ModelAdmin):
    list_display = ['body','post', 'author']
    list_filter = ['date']
    search_fields = ['body','post', 'author']
admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)