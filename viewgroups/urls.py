from django.urls import path

from . import views

urlpatterns = [
    
    #path('creategroup/', views.createGroupPageView, name='creategroup'),
    #path('newgroup/', views.createGroup, name='newgroup'),
    path('', views.groupsPageView, name='viewgroups'),
    
    
    path('editgroup/<int:groupID>/', views.editGroupPageView, name='editgroup'),
    path('editgroup/', views.editGroupPageView, name='newgroup'),
    path('newgroup/<int:groupID>/', views.newGroupView, name='finalizeNewGroupView'),
    path('newgroup/', views.newGroupView, name='newGroupView'),
       


    
]
