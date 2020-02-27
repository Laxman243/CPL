from django.urls import path
from . import views

# create your end points here
urlpatterns = [
    path("", views.index, name="index"),
    path('index/', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('recommend/', views.recommend, name='recommend'),
    # path('<int:movie_id>/', views.detail, name='detail'),
]

