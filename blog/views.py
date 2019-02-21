from django.shortcuts import render, get_object_or_404
from .models import Blog

def home(request):
    blogs = Blog.objects #쿼리셋 #메소드
    return render(request, 'home.html', {'blogs' : blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)

    return render(request, 'detail.html', {'blog':blog_detail})

# blog_detail = 이용자가 원한 몇 번 블로그 객체
# 쿼리셋과 메소드의 형식
# 모델.쿼리셋(objects).메소드