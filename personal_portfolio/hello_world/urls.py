from django.urls import path 
from . import views 

#register the app namespace

app_name = 'lien_hello_world'

# url
urlpatterns = [

    path('',views.welcom_view, name="welcom"),
    path('extend/', views.extend_view, name="extend"),
    path('variable/',views.variable_view,name= "variable"),
]