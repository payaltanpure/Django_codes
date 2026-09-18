from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.welcome3, name="welcome3"),
    path('wel4/', v.welcome4, name="welcome4"),
    path('getid/<int:id>/', v.details_by_id, name="details_by_id"),
    path('getuname/<str:uname>/', v.details_by_name, name="details_by_name"),
    path('getall/<int:id>/<str:name>/', v.mutiple_para, name= "multiple_para"),
    path('getallkwargs/<int:id>/<str:name>/', v.mutiple_para_kwargs, name= "multiple_para_kwargs"),

]
