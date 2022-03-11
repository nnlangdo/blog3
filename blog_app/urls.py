from django.urls import path
from . import views


app_name = 'blog_app'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('search/', views.post_search, name='post_search'),
    path('<slug:post>/', views.post_detail, name='post-detail'),
    path('category/<category>/', views.CatListView.as_view(), name='category'),    
]
