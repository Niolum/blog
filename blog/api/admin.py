from django.contrib import admin
from .models import Post, Category, Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created")
    list_filter = ("title", "owner", "created")
    search_fields = ("title", "owner__username")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "owner")
    list_filter = ("name", "owner__username")
    search_fields = ("name", )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "owner", "post", "created")
    readonly_fields = ("owner", )



admin.site.site_title = "Blog"
admin.site.site_header = "Blog"