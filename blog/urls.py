from django.conf.urls import url


from . import views


urlpatterns = [
    url(r'^$', views.Indexpage.as_view(), name='index')
]



