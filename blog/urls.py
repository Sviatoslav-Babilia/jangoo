from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
#from .views import ContactCreate

urlpatterns = [
    path("", views.BlogView.as_view(), name="blog_index"),
    path("<int:pk>/", views.BlogDetailView.as_view(), name="blog_detail"),
    path("contact/", views.ContactCreate.as_view(), name="contact"),
    path("thanks/", views.thanks, name="thanks"),
    path("new_blog/", views.PostCreate.as_view(), name="new_blog"),
    path("new_comment/<int:pk>", views.CommentCreate.as_view(), name="new_comment"),
    path("<int:pk>/edit", views.BlogEditView.as_view(), name="blog_edit"),
    path("<int:pk>/delete", views.BlogDeleteView.as_view(), name="blog_delete"),
    path("delete_comment/<int:pk>", views.CommentDeleteView.as_view(), name="comment_delete"),
    path("<category>/", views.blog_category, name="blog_category"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)