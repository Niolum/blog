from django.urls import path
from api.views.viewsdrf import (
    UserList, 
    UserDetail, 
    PostList, 
    PostDetail, 
    CommentList, 
    CommentDetail, 
    CategoryList, 
    CategoryDetail
)
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('users/', UserList.as_view(), name='users'),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view()),
    path('comments/', CommentList.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetail.as_view()),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)