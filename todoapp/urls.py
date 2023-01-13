from . import views
from django.urls import path

urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:updateid>/',views.update,name='update'),
    path('vbvhome/',views.Tasklistview.as_view(),name='vbvhome'),
    path('vbvdetail/<int:pk>/',views.Taskdetailview.as_view(),name='vbvdetail'),
    path('vbvupdate/<int:pk>/',views.Taskupdateview.as_view(),name='vbvupdate'),
    path('vbvdelete/<int:pk>/',views.Taskdeleteview.as_view(),name='vbvdelete'),
]
