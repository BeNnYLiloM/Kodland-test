from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('add-article', views.add_article, name='add_article'),
    path('create-article', views.create_article, name='create_article'),
]

# urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
