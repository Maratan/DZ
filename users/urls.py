from django.conf.urls import url
from users.views import logout, login_f, reg

urlpatterns = [
    url(r'^entry/$', login_f.as_view()),
    url(r'^exit/$', logout),
    url(r'^reg/$', reg.as_view()),
]