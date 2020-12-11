from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

# create router 
router = DefaultRouter()
# register new viewset on route hello-viewset
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
# don't need to assign a base_name because django_framework does it for default, when the view class has a queryset
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    # when the urls match from profiles_project, is added to api/ the hello-view/ 
    # and setup the logic from the endpoint on the view HelloApiView
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    # 2 arguments: '' - all url base on urls.py file , include... - url list routes
    path('', include(router.urls))
]