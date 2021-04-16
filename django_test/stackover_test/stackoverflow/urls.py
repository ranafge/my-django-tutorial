from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("show/", views.ApplicantListView.as_view(), name='applicant-list'),
    path("parts/", views.partList, name='part-list'),
    path("posts/", views.django_divisibleby_test, name='post-list'),
    path('like/', views.LikeView, name="like_post"),
    path('index/', views.IndexView.as_view(), name="index"),
    path('home/', views.home, name='home'),
    path('comment-form-view/', views.comment_form_view, name='comment-form-view'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('validate-username/', views.validate_username, name='validate-username'),
    path('username-exists/', views.username_exists, name='username-exists'),
    path('ajax-test/', views.ajax_test, name='ajax-test'),
    path('rooms/', TemplateView.as_view(template_name='stackoverflow/rooms.html'), name='rooms'),
    path('rooms/list/', views.RoomList.as_view(), name='room_list'),
    path('rooms/create/', views.RoomCreate.as_view(), name='room_create'),
    path('rooms/update/<int:pk>/', views.RoomUpdate.as_view(), name='room_update'),
    path('rooms/delete/<int:pk>/', views.RoomDelete.as_view(), name='room_delete'),
    path('rooms/<int:pk>/', views.RoomDetail.as_view(), name='room_detail'),
    path('sku/', views.new_item_view, name='sku-item'),
    path('permistion/', views.your_view, name='permission-deny'),
]
