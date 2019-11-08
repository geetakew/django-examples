from django.conf.urls import url, include
from basicapp import views

# TEMPLATE URLS!
app_name = 'basicapp'

urlpatterns = [
    url('^register/', views.register, name='register'),
    url('^user_login/', views.user_login, name='user_login'),
]
