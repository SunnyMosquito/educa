from django.contrib import admin
from .models import Subject, Course, Module

# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    # 属性来指定那些要使用其他字段来自动赋值的字段, 在admin里自动填写
    prepopulated_fields = {'slug': ('title',)}
# admin.site.register(Subject, SubjectAdmin)

# 将有外键的子类包含进视图
class ModuleInline(admin.StackedInline):
    model = Module
    # 显示多少个module
    extra = 1

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    # 将module包含进course页面
    inlines = [ModuleInline]
# admin.site.register(CourseAdmin)