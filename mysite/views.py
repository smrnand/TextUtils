# Sameer has created the file
# editing for git commit ver 2

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    #return HttpResponse("<h1>Hello Sameer</h1>")
    params = {'name': 'Sameer', 'place': 'Mars'}
    return render(request, 'index.html', params)


def about(request):
    f = open("D:/test/file_to_read.txt", 'r')
    data = f.read()
    return HttpResponse("About Sameer:" + data)


def analyze(request):
    mytext = request.GET.get('mytext', 'default')
    charcount = request.GET.get('charcount', 'off')
    wordcount = request.GET.get('wordcount', 'off')
    removepunc = request.GET.get('removepunc', 'off')
    params = {"charcount":0, "wordcount":0, "removepunc":mytext}
    if charcount == "on":
        params["charcount"] = len(mytext)
    if wordcount == "on":
        params["wordcount"] = len(mytext.split(" "))
    if removepunc == "on":
        pass
    return render(request, 'analyze.html', params)
