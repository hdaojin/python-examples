from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'articles'

urlpatterns = [
#     path('list/', views.article_list, name='article_list'),
    path('detail/<int:article_id>/', views.article_detail, name='article_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)