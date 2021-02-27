from django.contrib import admin
# #################################28
# from .models import News
#################################40
from .models import News, Category

# ##################################32
# class NewsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'created_at', 'update_at', 'is_published')

# ##################################35
# class NewsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'created_at', 'update_at', 'is_published')
#     list_display_links = ('id', 'title')
#     search_fields = ('title', 'content')

##################################44
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'update_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    #############################################46
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')

##################################42
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

# #################################27
# admin.site.register(News)

# #################################33
# admin.site.register(News, NewsAdmin)

#################################41
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)