from django.urls import path
from . import views

#create url
urlpatterns = [
    path('home/', views.home),
    path('get_id/<int:id>',views.get_id),
    path('get_name/<str:name>', views.get_name),
    # with the specifier
    path('get_id_name/<int:id>/<str:name>', views.get_id_name),
    # without the specifier
    path('<int:id>/<str:name>', views.get_id_name),
]
