from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/',views.login, name="login"),
    path('Registration/', views.Registration, name="Registration"),
    path('', views.Registration),
    path('login_attempt/', views.login_attempt),
    path('register_attempt/', views.register_attempt),
    path('success/', views.success),

]
# print("hreloo")

