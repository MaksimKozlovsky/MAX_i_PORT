from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('news/', views.news),
    path('news/', views.comment_page),
    path('news/<int:id>/', views.comment_page),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
