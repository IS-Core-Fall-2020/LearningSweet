from django.urls import path
from . import views

urlpatterns = [
    path('<int:groupID>/', views.assignPageView, name='viewassign'),
    path('edit/<int:assignID>/<int:groupID>/', views.editAssignPageView, name='editassign'),
    path('edit/<int:groupID>/', views.editAssignPageView, name='newassign'),
]   
