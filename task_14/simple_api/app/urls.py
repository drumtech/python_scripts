from django.urls import path
from .views import ServerViewSet, ServerDetailView, ServerAddView, StateViewSet, AddInfoViewSet, AddInfoAddView, AddInfoDetailSet


urlpatterns = [
    path('servers/', ServerViewSet.as_view()),
    path('servers/<int:pk>', ServerDetailView.as_view()),
    path('servers/add', ServerAddView.as_view()),
    path('servers/status/', StateViewSet.as_view()),
    path('additional_information/', AddInfoViewSet.as_view()),
    path('additional_information/add', AddInfoAddView.as_view()),
    path('additional_information/<int:pk>', AddInfoDetailSet.as_view()),
]
