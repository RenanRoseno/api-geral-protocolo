from django.urls import include, path
from rest_framework import routers

from api.viewsets.campusViewSet import *
from api.viewsets.cityViewSet import *
from api.viewsets.stateViewSet import *
from api.viewsets.swaggerView import swagger_view

route = routers.DefaultRouter()
route.register(r'states', StateViewSet)
route.register(r'campusq', CampusQuerySet, basename='campus')
route.register(r'cities', CitiesViewSet)



urlpatterns = [
    path('', include(route.urls)),
    path('api-alon/', swagger_view),
    path('campus/', CampusViewSet.as_view()),
    path('campus/<id>', CampusViewSet.as_view()),
    #path('cities/', CitiesListView.as_view()),
    #path('cities/<id>', CitiesViewSet.as_view()),
]