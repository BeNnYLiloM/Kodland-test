from django.shortcuts import render, redirect
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from .models import Blog


def index(request):
    new_article = Blog.objects.order_by('-pub_date')[:1]
    latest_articles_list = Blog.objects.order_by('-pub_date')[1:10]
    return render(request, 'blog/list.html', {'latest_articles_list': latest_articles_list, 'new_article': new_article})


def add_article(request):
    return render(request, 'blog/add-article.html')


def create_article(request):
    if request.method == 'POST':
        img = request.FILES.get('blog_img')
        fs = FileSystemStorage()
        img_name = fs.save(img.name, img)
        new_post = Blog(blog_title=request.POST['blog_title'],
                        blog_text=request.POST['blog_text'],
                        blog_image=fs.url(img_name),
                        pub_date=timezone.now())

        new_post.save()

    return redirect('/add-article')
