from django.contrib import admin
from blog.models import Post, Category, Comment, Headliner, Contacts


class PostAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


class HeadlinerAdmin(admin.ModelAdmin):
    pass


class ContactsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Headliner, HeadlinerAdmin)
admin.site.register(Contacts, ContactsAdmin)
