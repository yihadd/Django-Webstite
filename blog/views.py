from django.shortcuts import render
from .models import BlogPost
from django.http import HttpResponse
from .models import Visitor


def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog_list.html', {'posts': posts})


def set_cookie_view(request):
    response = HttpResponse("Cookie Set!")
    
    response.set_cookie(
        key='user_id', 
        value='101010', 
        max_age=3600, 
        secure=True,    
        httponly=True,  
        samesite='Lax'         
    )
    
    return response


def get_cookie_view(request):
    user_id = request.COOKIES.get('user_id', 'No cookie found')
    
    return HttpResponse(f'User ID from cookie: {user_id}')


def delete_cookie_view(request):
    response = HttpResponse("Cookie Deleted!")
    response.delete_cookie('user_id')  
    return response


def visitor_count_view(request):
    visitor_count = Visitor.objects.count()  # Get total visitor count
    return render(request, 'blog_list.html', {'visitor_count': visitor_count})
