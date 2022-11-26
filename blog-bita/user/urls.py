from django.urls import path
from .views import register,login,allpost,index,profile,logouthere,post,readmore,profileview,profileedit,postedit,postdelete

urlpatterns = [
    path('register',register,name='register'),
    path('login',login,name='login'),
    path('profile',profile,name='profile'),
    path('profileedit',profileedit,name='profileedit'),
    path('profileview/<id>',profileview,name='profileview'),
    path('post',post,name='post'),
    path('postedit/<id>',postedit,name='postedit'),
    path('postdelete/<id>',postdelete,name='postdelete'),
    path('allpost',allpost,name='allpost'),
    path('logout',logouthere,name='logout'),    
    path('readmore/<id>',readmore,name='readmore'),    
    path('',index,name='index'),

]