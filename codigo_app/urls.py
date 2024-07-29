from django.urls import path
from codigo_app import views

urlpatterns = [
   path('', views.index, name='index'),  
   path('loginform',views.loginform, name='loginform'),
   path('logout', views.logout, name='logout'), 
   path('user_signup', views.user_signup, name='user_signup'),
   path('blog-deatail/<int:id>', views.blog_detail, name='blog_detail'),
   path('share_bog', views.share_blog, name='share_bog'),
 
]