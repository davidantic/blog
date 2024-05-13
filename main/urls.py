from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name ='sign_up'),
    path('create-post', views.create_post, name ='create_post'),
    path('update-post/<int:pk>', views.update_post, name ='update_post'),
    path('post/<int:pk>', views.view_post, name ='view_post'),
]
