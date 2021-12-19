from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('users/', views.UserList.as_view(), name='users'),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('posts/', views.PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('comments/', views.CommentList.as_view(), name='comment-list'),
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)