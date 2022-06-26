from django.urls import path, include
from api.views.views import (
    PostListView, 
    PostDetailView, 
    CategoryListView, 
    CategoryDetailView, 
    AddCommentView,
    AddCategoryView,
    AddPostView,
    SignUp,
) 


urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post'),
    path('category/', CategoryListView.as_view(), name='categories'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category'),
    path('add-comment/<int:pk>/', AddCommentView.as_view(), name='add_comment'),
    path('add-category/', AddCategoryView.as_view(), name='add_category'),
    path('add-post/', AddPostView.as_view(), name='add_post'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignUp.as_view(), name='signup')
]