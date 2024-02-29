# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', 'home_view, name=home'),
    path('post/<int:post_id>/', 'post_detail_view, name=post_detail'),
    path('create_post/', 'post_creation_view, name=create_post'),
    path('submit_comment/<int:post_id>/', 'comment_submission_view, name=submit_comment'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
