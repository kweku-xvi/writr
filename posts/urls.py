from . import views
from django.urls import path


urlpatterns = [
    path('create', views.create_blog, name='create_blog'),
    path('<int:id>', views.get_blog_by_id, name='get_blog_by_id'),
    path('all', views.get_all_blogs, name='get_all_blogs'),
    path('update/<int:id>', views.update_blog, name='update_blog'),
    path('delete/<int:id>', views.delete_blog, name='delete_blog')
]