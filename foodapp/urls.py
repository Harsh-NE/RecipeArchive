from django.urls import path
from . import views
app_name='foodapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('additem/',views.add_item,name='additem'),
    path('details/<int:id>/',views.dishdetails,name='dishdetails'),
    path('removerecipe/<int:id>/',views.removerecipe,name='removerecipe'),
    path('updaterecipe/<int:id>/',views.updaterecipe,name='updaterecipe'),
]