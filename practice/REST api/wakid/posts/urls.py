from django.urls import path, include
from . import views


urlpatterns = [
    path('posts/', views.PostList.as_view(), name='posts'),
    path('posts/<int:pk>/', views.PostRetrieveDestroy.as_view(), name='post'),
    path('posts/<int:pk>/vote/', views.VoteCreate.as_view(), name='vote_create')

]
