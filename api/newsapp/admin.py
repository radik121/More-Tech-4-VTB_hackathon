from django.contrib import admin
from .models import News, Positions, Insites, Trends


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'date')


class PositionsAdmin(admin.ModelAdmin):
    fields = ('name', 'slug',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(News, NewsAdmin)
admin.site.register(Positions, PositionsAdmin)
admin.site.register(Insites)
admin.site.register(Trends)
