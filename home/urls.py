from django.urls import path
from .views import CustomUserView, LoginView, CVCreateView, CVDetailView, LogoutView  # import LoginView

urlpatterns = [
    path('singup', CustomUserView.as_view(), name='signup'),
    path('', LoginView.as_view(), name='login'),  # use LoginView for 'login'
    path('logout/', LogoutView.as_view(), name='logout'),  
    path('cv/create/', CVCreateView.as_view(), name='cv_create'),
    path('cv/<int:pk>/', CVDetailView.as_view(), name='cv_detail'),
]

