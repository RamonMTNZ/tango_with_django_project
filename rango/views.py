from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    # Construct a dict to pass to the template engine as its context
    # Note that the key boldmessage matches to {{ boldmessage }} in the template
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    # return a rendered response to send to the client
    # We want to make use of the shortcut function to make our lives easier
    # Note that the first parameter is the template we wish to use!
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    # Construct a dict to pass to the template engine as its context
    # Note that the key boldmessage matches to {{ boldmessage }} in the template
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    # return a rendered response to send to the client
    # We want to make use of the shortcut function to make our lives easier
    # Note that the first parameter is the template we wish to use!
    return render(request, 'rango/about.html', context=context_dict)
