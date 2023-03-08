from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


def welcom_view(request):
    return render(request,'hello_world/index.html') # html

#---------------------------------------------------------

# create a function
def variable_view(request):
    # create a dictionary
    context = {
        "first_name" : "Naveen",
        "last_name"  : "Arora",
        "username"   : "Hitachi",
        'some_list': [1,2,3],
        'is_user_logged_in': True,
        'some_dic':{'inside_key': ' inside_value'}
    }
    # return response
    return render(request, "hello_world/variable.html", context)


#---------------------------------------------------------

# create a function
def extend_view(request):
 
    # return response
    return render(request, "hello_world/exemple.html")