from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index, name='index'),
    path('doc-list/', views.uploadView, name='upload-doc'),
    path('upload-create-view/', views.UploadView.as_view(), name='upload-doc')
]