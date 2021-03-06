from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.posts, name = 'posts'),
    path('<int:pk>', views.post, name = 'post'),
    path('post_create/', views.post_create, name = 'post_create'),
    path('<int:pk>/update/', views.post_update, name = 'post_update'),
    path('<int:pk>/delete/', views.post_delete, name = 'post_delete'),
    path('<int:pk>/photo/', views.photo_show, name = 'photo_show'),
    path('<int:pk>/delete/cushion/', views.cushion_delete, name = 'cushion_delete'),
]
