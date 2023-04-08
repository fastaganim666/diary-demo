from django.urls import path
from .views import *

urlpatterns = [
    path('', MainBookmark.as_view(), name='bookmark_main'),
    path('<int:pk>/', EditBookmark.as_view(), name='bookmark_edit'),
    path('delete/<int:pk>/', DeleteBookmark.as_view(), name='bookmark_delete'),
    path('category/<int:pk>/', CategoryBookmark.as_view(), name='bookmark_category'),
    path('category/add/', AddCategory.as_view(), name='category_add'),
    path('category/delete/<int:pk>/', DeleteCategory.as_view(), name='category_delete'),
]