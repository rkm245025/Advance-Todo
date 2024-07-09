from django.urls import path
from . import views



urlpatterns=[

    path("",views.home,name="home"),
    path("registration/",views.registration,name="registration"),
    path("profile/",views.profile,name="profile"),
    path("login_user/",views.login_user,name="login_user"),
    path('logout/',views.logout_user,name='logout_user'),
    path("task/",views.task,name="task"),
    path("delete/<int:pk>/",views.delete_task,name="delete"),
    path("update/<int:pk>/",views.update_task,name="update"),
    path("search/",views.search,name="search"),
    path("filter/",views.filter,name="filter"),
    path("about/",views.about,name="about")
]