from django.urls import path
from .views import blog_list
from . import views


urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('set-cookie/', views.set_cookie_view, name='set_cookie'),
    path('get-cookie/', views.get_cookie_view, name='get_cookie'),
    path('delete-cookie/', views.delete_cookie_view, name='delete_cookie'),
    path('visitor-count/', views.visitor_count_view, name='visitor_count'),
    
]
