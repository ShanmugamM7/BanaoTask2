from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('patient_page/', views.patient_page, name='patient_page'),
    path('doctor_page/', views.doctor_page, name='doctor_page'),
    path('create_blog_post/', views.create_blog_post, name='create_blog_post'),
    path('blog_list/', views.blog_list, name='blog_list'),
    path('doctor/posts/', views.doctor_posts, name='doctor_posts'),
    path('patient/posts/', views.patient_posts, name='patient_posts'),
    path('blog_post_detail/<int:pk>/', views.blog_post_detail , name='blog_post_detail'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)