from django.urls import path
from App_Blog import views

app_name = 'App_Blog'

urlpatterns = [
  path('', views.blog_list, name='blog_list')
  path('write/', views.createBlog.as_view(), name='create_blog'),

]
