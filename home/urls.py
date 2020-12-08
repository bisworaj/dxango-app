from django.urls import path
from home import views


urlpatterns = [ 
    path('',views.index,name="home"),
    path('about',views.about,name="about"),
    path('docs',views.docs,name="docs"),
    path('auth',views.auth,name="auth"),
    path('contact',views.contact,name="contact"),
    path('confirmed',views.confirmed,name="confirmed")
]