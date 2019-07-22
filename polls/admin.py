from django.contrib import admin
from .models import *
# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #在后台显示的字段列表
    #fields = ['pubDate','questionText']
    #字段分组
    fieldsets = [
        (None,{'fields':['questionText']}),
        ('Date info',{'fields':['pubDate']})
    ]
    inlines = [ChoiceInline]
    list_display = ['questionText','pubDate','was_published_recently']
    list_filter = ['pubDate']
    search_fields = ['questionText']

admin.site.register(Question,QuestionAdmin)
# admin.site.register(Choice)
