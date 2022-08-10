
from django.contrib import admin
from django.urls import path

from employee import views 

urlpatterns = [


    path('admin/', admin.site.urls),

    path('register/',views.registerPage,name = "register"),
    path('login/',views.loginPage,name = "login"),
    path('logout/',views.logoutUser,name = "logout"),

    path('',views.home,name = "home"),
    path('add/',views.addEmployee,name="add"),
    path('update/<str:pk>/',views.updateEmployee,name="update"),
    path('delete/<str:pk>/',views.deleteEmployee,name="delete"),
]
