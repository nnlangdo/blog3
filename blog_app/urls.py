from django.urls import path
from . import views


app_name = 'blog_app'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('<slug:post>/', views.post_detail, name='post-detail'),
]
