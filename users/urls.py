from django.urls import path
from .views import RegisterView, AdminOnlyView, ModeratorOnlyView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('admin-only/', AdminOnlyView.as_view(), name='admin-only'),
    path('moderator-only/', ModeratorOnlyView.as_view(), name='moderator-only'),
]