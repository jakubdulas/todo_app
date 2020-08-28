from django.urls import path
from . import views as v


urlpatterns = [
    path('', v.HomeView.as_view(), name="home"),
    path('add_task', v.add_task, name="add_task"),
    path('complete/<int:pk>', v.complete, name="complete"),
    path('delete/<int:pk>', v.delete, name="delete"),
    path('set_as_important/<int:pk>', v.set_as_important, name="set_as_important"),
]
