from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^get/', views.get_censo, name='get'),
    url(r'^filter/', views.filter_censos),
    url(r'^can_vote/', views.can_vote),
    url(r'^create/', views.create_censo),
    url(r'^update/', views.update_censo),
    url(r'^delete/', views.delete_censo, name='delete')
]
