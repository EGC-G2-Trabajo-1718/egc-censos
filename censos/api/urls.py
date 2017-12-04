from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^get/', views.get_censo),
    url(r'^filter/', views.filter_censos),
    url(r'^can_vote/', views.can_vote),
    url(r'^create/', views.create_censo),
    url(r'^update/', views.update_censo),
    url(r'^delete/', views.delete_censo)
]
