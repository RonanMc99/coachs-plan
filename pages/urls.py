from django.urls import path

from .views import HomePageView, ContactPageView, profile_view

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('account/profile/', profile_view, name='profile'),
]
