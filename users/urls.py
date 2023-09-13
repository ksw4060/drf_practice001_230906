from django.urls import path
from users import views
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='sign_up_view'), # /users/signup/
    path('mock/', views.MockView.as_view(), name='mock_view'), # /users/signup/

    path('api/token/login/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
