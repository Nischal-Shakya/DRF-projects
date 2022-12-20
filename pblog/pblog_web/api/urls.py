from django.urls import path
from pblog_web.api.views import id_list, id_details

urlpatterns = [
    path('list/', id_list, name='id-list'),
    path('<int:pk>', id_details, name='id-details'),
]
