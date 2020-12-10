from django.urls import path 
from profiles_api import views

urlpatterns = [
    # when the urls match from profiles_project, is added to api/ the hello-view/ 
    # and setup the logic from the endpoint on the view HelloApiView
    path('hello-view/', views.HelloApiView.as_view()),
]