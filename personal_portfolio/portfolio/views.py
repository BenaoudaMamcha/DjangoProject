from django.http.response import HttpResponse
from django.shortcuts import render


def home_view(request):
    return HttpResponse("home page")


def my_coustom_page_not_find_view(request,exception):
    return render(request, 'error_view.html',status=404)
