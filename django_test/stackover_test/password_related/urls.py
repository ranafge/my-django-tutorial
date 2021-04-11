from django.urls import path
from . import views

urlpatterns =[

    path('resetpassword/', views.UserAccountResetPasswordView.as_view(), name='resetpassword'),

]
