from django.urls import path,include
from . import views
urlpatterns = [
path('', views.home_view, name='home'),
path("aboutpage/",views.about_view,name="about"),
path("contactpage/",views.contact_view,name="contact"),
path("logintpage/",views.login_view,name="login"),
path("registerpage/",views.register_view,name="register"),
path("useractivitypage/",views.user_dataview,name="user_register"),
path("user_homepage/",views.user_loginview,name="user_login"),
path("logout/",views.user_logoutview,name="user_logout"),
path("after_loginpage",views.after_loginhomeview,name="user_home"),
path("earn_moneypage/",views.earn_money_views,name="earn_money"),
path("offer_page/",views.offer_views,name="offer"),
path("profilepage/",views.profile_views,name="profile")
]