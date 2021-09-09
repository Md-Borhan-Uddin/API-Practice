from django.urls import path
from  .import genericviews
# from .import views
# from .import apiviews

urlpatterns = [
    # path("", views.Home.as_view(), name="home"),
    # path("info", apiviews.home, name="info"),
    # path("info/<int:pk>", apiviews.home, name="info"),
    # path("todo", apiviews.todoView, name="todo"),
    # path("todo", apiviews.ToDOView.as_view(), name="todo"),
    # path("todo/<int:id>", apiviews.todoView, name="todo"),
    # path("todo/<int:id>", apiviews.ToDOView.as_view(), name="todo"),
    # path("create", views.registration, name="create"),
    # path("update", views.infoupdate, name="update"),
    # path("delete", views.infodelete, name="delete"),
    
    
    
    
    path('listview/', genericviews.ListPerson.as_view(), name="listview")
]
