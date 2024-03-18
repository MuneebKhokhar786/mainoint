from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('', include("django.contrib.auth.urls")),
]
