from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('' , views.apiAuthentication.as_view(), name ='hello'),
    path('createUser' , views.createUser.as_view() , name="create_user_details"),
    path('deleteUser' , views.deleteUser.as_view() , name="delete_user_details"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
