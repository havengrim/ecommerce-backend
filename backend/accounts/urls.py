from django.urls import path
from .views import RegisterView, LoginView, LogoutView, UserListView

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='api-signup'),
    path('login/', LoginView.as_view(), name='api-login'),
    path('logout/', LogoutView.as_view(), name='api-logout'),
    path('users/', UserListView.as_view(), name='user-list'),
]
