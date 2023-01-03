from django.http import HttpResponse

def home(request):
    return HttpResponse('<center><h1 style="background-color:yellow;">Merhaba Backend API</h1></center>')