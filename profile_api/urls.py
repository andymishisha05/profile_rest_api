from django.urls import path,include
from rest_framework.routers import DefaultRouter
from. import views

router = DefaultRouter();
router.register('hello-viewset',views.HelloViewSet,base_name = 'hello-viewset')
router.register('profile',views.UserProfileViewSet,base_name = 'profile')

urlpatterns = [

    path('hello/',views.HelloApiView.as_view()),
   #  path('profile/',views.UserProfileAPIView.as_view()),
    path('',include(router.urls)),
    path('index/',views.index)

]
