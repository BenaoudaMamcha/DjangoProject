from django.urls import path
from .import views

# url name tag , uliliser avec la methode reverse (redirect)
app_name= 'cars'

urlpatterns = [
    path('rental_review/',views.rental_view, name='rental_review'),
    path('thank_you/',views.thank_you, name='thank_you')
]
